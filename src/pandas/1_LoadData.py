import pandas as pd

if __name__ == '__main__':
    # 导入CSV或者xlsx文件：
    df1 = pd.DataFrame(pd.read_csv('name.csv', header=1))
    df2 = pd.DataFrame(pd.read_excel('name.xlsx'))
