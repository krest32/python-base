import requests
from bs4 import BeautifulSoup


def getChapter_content(url):
    resp = requests.get(url)
    resp.encoding = "gbk"
    soup = BeautifulSoup(resp.text, 'html.parser')
    txt = (soup.find("div", id="content")
           .get_text()
           .replace(u'xa0', u' ')
           .replace('\xa0', " "))
    return txt


if __name__ == '__main__':
    # 获取所有的章节地址
    url = "http://www.quanben.cc/xiaoshuo/0/20/"
    # 请求头配置
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }

    resp = requests.get(url, headers=header)
    resp.encoding = "gbk"
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 抓取所有的 章节标题 和 url
    data = []
    for dd in soup.find_all("dd"):
        # 获取 a 标签
        link = dd.find("a")
        if not link:
            continue
        data.append(("http://www.quanben.cc/%s" % link['href'], link.get_text()))

    # 获取章节内容
    for datum in data:
        url, title = datum
        # 下载文本
        print(title, url)
        with open('全本小说/%s.txt' % title, 'w') as fout:
            fout.write(getChapter_content(url))
