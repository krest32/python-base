import os
import datetime
import torch
import torchtext
import torchkeras
import numpy as np
import pandas as pd
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from torch.utils.data import Dataset, DataLoader
from torch import nn
from torchkeras import summary
import sys, time
from tqdm import tqdm
import torchmetrics

from copy import deepcopy

torch.manual_seed(42)

# mac系统上pytorch和matplotlib在jupyter中同时跑需要更改环境变量
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

MIN_FREQ = 30  # 仅考虑词频超过30的词
MAX_LEN = 200  # 每个样本保留200个词的长度
BATCH_SIZE = 20
PAD_IDX, UNK_IDX = 0, 1
special_symbols = ['<pad>', '<unk>']


# 打印时间
def print_bar():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========" * 8 + "%s" % now_time)


def load_data():
    dftrain = pd.read_csv(
        "./data/imdb/train.csv",
        sep="\t",
        header=None,
        names=["label", "text"]
    )
    dfval = pd.read_csv(
        "./data/imdb/test.csv", sep="\t",
        header=None,
        names=["label", "text"]
    )
    return dftrain, dfval


def yield_tokens(dfdata, tokenizer):
    for text in dfdata["text"]:
        yield tokenizer(text)


def create_dict(dftrain, tokenizer):
    vocab = build_vocab_from_iterator(
        yield_tokens(dftrain, tokenizer),
        min_freq=MIN_FREQ,
        specials=special_symbols,
        special_first=True)

    vocab.set_default_index(UNK_IDX)
    vocab_size = len(vocab)
    print("vocab_size =" + str(vocab_size))

    # 查看词典前20个词
    # itos: index to string
    # stoi: string to index
    print("vocab.get_itos():\n", vocab.get_itos()[:20])
    print("vocab.get_stoi()['<pad>']:\n", vocab.get_stoi()['<pad>'])
    return vocab, vocab_size


def pad(seq, max_length, pad_value=0):
    n = len(seq)
    result = seq + [pad_value] * max_length
    return result[:max_length]


def text_pipeline(text, vocab):
    words = tokenizer(text)
    tokens = vocab(words)
    result = pad(tokens, MAX_LEN, PAD_IDX)
    return result


class ImdbDataset(Dataset):
    def __init__(self, df):
        self.df = df

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        text = self.df["text"].iloc[index]
        label = torch.tensor([self.df["label"].iloc[index]]).float()
        tokens = torch.tensor(text_pipeline(text, vocab)).int()
        return tokens, label


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        # 设置padding_idx参数后将在训练过程中将填充的token始终赋值为0向量
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=3, padding_idx=0)

        self.conv = nn.Sequential()
        self.conv.add_module("conv_1", nn.Conv1d(in_channels=3, out_channels=16, kernel_size=5))
        self.conv.add_module("pool_1", nn.MaxPool1d(kernel_size=2))
        self.conv.add_module("relu_1", nn.ReLU())
        self.conv.add_module("conv_2", nn.Conv1d(in_channels=16, out_channels=128, kernel_size=2))
        self.conv.add_module("pool_2", nn.MaxPool1d(kernel_size=2))
        self.conv.add_module("relu_2", nn.ReLU())

        self.dense = nn.Sequential()
        self.dense.add_module("flatten", nn.Flatten())
        self.dense.add_module("linear", nn.Linear(6144, 1))

    def forward(self, x):
        x = self.embedding(x).transpose(1, 2)  # 交换通道维度到前面, Batch,Channel,Time
        x = self.conv(x)
        y = self.dense(x)
        return y


def printlog(info):
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========" * 8 + "%s" % nowtime)
    print(str(info) + "\n")


class StepRunner:
    def __init__(self, net, loss_fn, stage="train", metrics_dict=None,
                 optimizer=None, lr_scheduler=None
                 ):
        self.net, self.loss_fn, self.metrics_dict, self.stage = net, loss_fn, metrics_dict, stage
        self.optimizer, self.lr_scheduler = optimizer, lr_scheduler

    def __call__(self, features, labels):
        # loss
        preds = self.net(features)
        loss = self.loss_fn(preds, labels)

        # backward()
        if self.optimizer is not None and self.stage == "train":
            loss.backward()
            self.optimizer.step()
            if self.lr_scheduler is not None:
                self.lr_scheduler.step()
            self.optimizer.zero_grad()

        # metrics
        step_metrics = {self.stage + "_" + name: metric_fn(preds, labels).item()
                        for name, metric_fn in self.metrics_dict.items()}
        return loss.item(), step_metrics


class EpochRunner:
    def __init__(self, steprunner):
        self.steprunner = steprunner
        self.stage = steprunner.stage
        self.steprunner.net.train() if self.stage == "train" else self.steprunner.net.eval()

    def __call__(self, dataloader):
        total_loss, step = 0, 0
        loop = tqdm(enumerate(dataloader), total=len(dataloader))
        for i, batch in loop:
            if self.stage == "train":
                loss, step_metrics = self.steprunner(*batch)
            else:
                with torch.no_grad():
                    loss, step_metrics = self.steprunner(*batch)
            step_log = dict({self.stage + "_loss": loss}, **step_metrics)

            total_loss += loss
            step += 1
            if i != len(dataloader) - 1:
                loop.set_postfix(**step_log)
            else:
                epoch_loss = total_loss / step
                epoch_metrics = {self.stage + "_" + name: metric_fn.compute().item()
                                 for name, metric_fn in self.steprunner.metrics_dict.items()}
                epoch_log = dict({self.stage + "_loss": epoch_loss}, **epoch_metrics)
                loop.set_postfix(**epoch_log)

                for name, metric_fn in self.steprunner.metrics_dict.items():
                    metric_fn.reset()
        return epoch_log


class KerasModel(torch.nn.Module):
    def __init__(self, net, loss_fn, metrics_dict=None, optimizer=None, lr_scheduler=None):
        super().__init__()
        self.history = {}

        self.net = net
        self.loss_fn = loss_fn
        self.metrics_dict = nn.ModuleDict(metrics_dict)

        self.optimizer = optimizer if optimizer is not None else torch.optim.Adam(
            self.parameters(), lr=1e-2)
        self.lr_scheduler = lr_scheduler

    def forward(self, x):
        if self.net:
            return self.net.forward(x)
        else:
            raise NotImplementedError

    def fit(self, train_data, val_data=None, epochs=10, ckpt_path='checkpoint.pt',
            patience=5, monitor="val_loss", mode="min"):

        for epoch in range(1, epochs + 1):
            printlog("Epoch {0} / {1}".format(epoch, epochs))

            # 1，train -------------------------------------------------
            train_step_runner = StepRunner(net=self.net, stage="train",
                                           loss_fn=self.loss_fn, metrics_dict=deepcopy(self.metrics_dict),
                                           optimizer=self.optimizer, lr_scheduler=self.lr_scheduler)
            train_epoch_runner = EpochRunner(train_step_runner)
            train_metrics = train_epoch_runner(train_data)

            for name, metric in train_metrics.items():
                self.history[name] = self.history.get(name, []) + [metric]

            # 2，validate -------------------------------------------------
            if val_data:
                val_step_runner = StepRunner(net=self.net, stage="val",
                                             loss_fn=self.loss_fn, metrics_dict=deepcopy(self.metrics_dict))
                val_epoch_runner = EpochRunner(val_step_runner)
                with torch.no_grad():
                    val_metrics = val_epoch_runner(val_data)
                val_metrics["epoch"] = epoch
                for name, metric in val_metrics.items():
                    self.history[name] = self.history.get(name, []) + [metric]

            # 3，early-stopping -------------------------------------------------
            if not val_data:
                continue
            arr_scores = self.history[monitor]
            best_score_idx = np.argmax(arr_scores) if mode == "max" else np.argmin(arr_scores)
            if best_score_idx == len(arr_scores) - 1:
                torch.save(self.net.state_dict(), ckpt_path)
                print("<<<<<< reach best {0} : {1} >>>>>>".format(monitor,
                                                                  arr_scores[best_score_idx]), file=sys.stderr)
            if len(arr_scores) - best_score_idx > patience:
                print("<<<<<< {} without improvement in {} epoch, early stopping >>>>>>".format(
                    monitor, patience), file=sys.stderr)
                break

        self.net.load_state_dict(torch.load(ckpt_path))
        return pd.DataFrame(self.history)

    @torch.no_grad()
    def evaluate(self, val_data):
        val_step_runner = StepRunner(net=self.net, stage="val",
                                     loss_fn=self.loss_fn, metrics_dict=deepcopy(self.metrics_dict))
        val_epoch_runner = EpochRunner(val_step_runner)
        val_metrics = val_epoch_runner(val_data)
        return val_metrics

    @torch.no_grad()
    def predict(self, dataloader):
        self.net.eval()
        result = torch.cat([self.forward(t[0]) for t in dataloader])
        return result.data


class Accuracy(torchmetrics.Accuracy):
    def __init__(self, dist_sync_on_step=False):
        super().__init__(dist_sync_on_step=dist_sync_on_step)

    def update(self, preds: torch.Tensor, targets: torch.Tensor):
        super().update(torch.sigmoid(preds), targets.long())

    def compute(self):
        return super().compute()


if __name__ == '__main__':
    print("torch.__version__ = ", torch.__version__)
    print("torchtext.__version__ = ", torchtext.__version__)
    print("torchkeras.__version__ = ", torchkeras.__version__)
    print_bar()

    """
        数据说明
        imdb数据集的目标是根据电影评论的文本内容预测评论的情感标签。
        训练集有20000条电影评论文本，测试集有5000条电影评论文本，其中正面评论和负面评论都各占一半。
        文本数据预处理较为繁琐，包括文本切词，构建词典，编码转换，序列填充，构建数据管道等等。
    """
    # 1.1 加载数据
    dftrain, dfval = load_data()

    # 1.2 文本切词
    tokenizer = get_tokenizer('basic_english')

    # 构建词典
    vocab, vocab_size = create_dict(dftrain, tokenizer)

    # 1.3 填充序列  1.4 编码转换
    print(text_pipeline("this is an example!", vocab))

    # 1.5 构建管道
    ds_train = ImdbDataset(dftrain)
    ds_val = ImdbDataset(dfval)

    dl_train = DataLoader(ds_train, batch_size=50, shuffle=True)
    dl_val = DataLoader(ds_val, batch_size=50, shuffle=False)

    # 定义模型
    net = Net()
    print(net)

    # summary(net, input_data=features);
    # 训练模型
    model = KerasModel(
        net,
        loss_fn=nn.BCEWithLogitsLoss(),
        optimizer=torch.optim.Adam(net.parameters(), lr=0.005),
        metrics_dict={"acc": Accuracy(task='multiclass', num_classes=6)}
    )

    model.fit(
        train_data=dl_train,
        val_data=dl_val,
        epochs=10,
        ckpt_path='checkpoint.pt',
        patience=3,
        monitor='val_acc',
        mode='max')
