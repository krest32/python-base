import pandas as pd

if __name__ == '__main__':
    # 导入CSV或者xlsx文件：
    df1 = pd.DataFrame(pd.read_csv('excel_to_python.csv', header=1))
    df2 = pd.DataFrame(pd.read_excel('excel_to_python.xlsx'))

    print(df1.values)
    print(df2.values)
