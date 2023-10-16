import requests
import pandas as pd
import re


def GetAllFundCompany():
    '''
        功能：获取所有基金公司名称、代码，天天基金数据接口：http://fund.eastmoney.com/js/jjjz_gs.js
        传入：无
        返回：所有基金公司名称、代码
    '''
    url = "http://fund.eastmoney.com/js/jjjz_gs.js"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    res.encoding = "utf-8"
    list_ = eval(re.findall(r'\[.*\]', res.text)[0])
    df = pd.DataFrame(list_)
    df.columns = ['基金公司代码', '基金公司名称']

    return df


if __name__ == "__main__":
    fund_companies = GetAllFundCompany()
    print(fund_companies.items)
