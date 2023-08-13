import requests
import pandas as pd


# 爬去对应年份和月份的数据
def crawTable(year, month):
    # 请求头配置
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }

    # 天气地址接口
    url = "https://tianqi.2345.com/Pc/GetHistory"
    # 请求参数
    params = {
        "areaInfo[areaId]": "54511",
        "areaInfo[areaType]": "2",
        "date[year]": year,
        "date[month]": month
    }

    resp = requests.get(url, headers=header, params=params)
    # 打印其中的内容
    # print(resp.content)
    # data 中是 Json 数据，直接可以获取
    data = resp.json()['data']
    # print(data)

    # pandas 解析 html 中的表格
    # 如果缺少 lxml， 那么就进行安装 py -m pip install lxml
    df = pd.read_html(data)[0]
    # 可以用表格的方式打印出数据
    # print(df.head())
    return df


if __name__ == '__main__':
    df_list = []
    for year in range(2011, 2022):
        for month in range(1, 13):
            print("爬取：", year, month)
            df = crawTable(year, month)
            # 数据保存在 df 中
            df_list.append(df)

    # pd 拼接数据到 excel 中
    # 如果缺少 openpyxl， py -m pip install openpyxl
    pd.concat(df_list).to_excel("北京10年天气数据.xlsx", index=False)
