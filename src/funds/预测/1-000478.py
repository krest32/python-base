import re
import matplotlib.pyplot as plt
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def Get_html(fund_code, start_date, end_date, type_="lsjz", page=1, per=20):
    '''
        获取基金网页数据
    '''
    url = "http://fund.eastmoney.com/f10/F10DataApi.aspx?type={}&code={}&page={}&sdate={}&edate={}&per={}" \
        .format(type_, fund_code, page, start_date, end_date, per)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }
    HTML = requests.get(url, headers=headers)
    print(url)
    HTML.encoding = "utf-8"

    return HTML


def Get_pages(HTML):
    '''
        获取最大页数
    '''
    pages = re.findall(r'pages:(.*),', HTML.text)[0]

    return int(pages)


def Get_FundData_history(HTML):
    '''
        通过html获取基金历史数据
    '''
    soup = BeautifulSoup(HTML.text, 'html.parser')
    trs = soup.find_all("tr")
    res = []
    for tr in trs[1:]:
        date = tr.find_all("td")[0].text  # 净值日期
        unit_net = tr.find_all("td")[1].text  # 单位净值
        acc_net = tr.find_all("td")[2].text  # 累计净值
        fund_r = tr.find_all("td")[3].text  # 日增长率
        buy_status = tr.find_all("td")[4].text  # 申购状态
        sell_status = tr.find_all("td")[5].text  # 赎回状态
        res.append([date, unit_net, acc_net, fund_r, buy_status, sell_status])
    df = pd.DataFrame(res, columns=['净值日期', '单位净值', '累计净值', '日增长率', '申购状态', '赎回状态'])

    return df


def Get_FundData_main(fund_code, start_date, end_date):
    '''
        获取基金数据主函数（仅支持单基金）
    '''
    html = Get_html(fund_code, start_date, end_date)
    pages = Get_pages(html)
    res_df = pd.DataFrame()
    for page in range(1, pages + 1):
        html = Get_html(fund_code, start_date, end_date, "lsjz", page)
        df_ = Get_FundData_history(html)
        res_df = pd.concat([res_df, df_])

    res_df.insert(0, "基金代码", fund_code)

    return res_df


def un_linear_regression(x, y, degree):
    # 非线性回归
    # 根据degree的值转换为相应的多项式（非线性回归），也就是几级的 泰勒多项式
    ploy_feat = PolynomialFeatures(degree)
    x_p = ploy_feat.fit_transform(x)
    clf = LinearRegression()
    clf.fit(x_p, y)
    return clf, x_p


def test_func(clf, x):
    return clf.intercept_[0] + clf.coef_[0, 1] * (x ** 1) + clf.coef_[0, 2] * (x ** 2) + clf.coef_[0, 3] * (
            x ** 3) + clf.coef_[0, 4] * (x ** 4) + clf.coef_[0, 4] * (x ** 5) + clf.coef_[0, 6] * (x ** 6)
    # return clf.intercept_[0] + clf.coef_[0, 1] * (x ** 1) + clf.coef_[0, 2] * (x ** 2) + clf.coef_[0, 3] * (
    #            x ** 3) + clf.coef_[0, 4] * (x ** 4)
    # return clf.intercept_[0] + clf.coef_[0, 1] * (x ** 1) + clf.coef_[0, 2] * (x ** 2) + clf.coef_[0, 3] * (
    #         x ** 3) + clf.coef_[0, 4] * (x ** 4) + clf.coef_[0, 4] * (x ** 5)
    # return clf.intercept_[0] + clf.coef_[0, 1] * (x ** 1) + clf.coef_[0, 2] * (x ** 2) + clf.coef_[0, 3] * (x ** 3)


if __name__ == "__main__":
    # start_date = "2010-01-15"
    # end_date = "2023-10-16"
    # # codes = ['320007', '161725', '012723']  # 基金代码列表
    # # 建信 500 指数强
    # codes = ['000478']  # 基金代码列表
    # fund_df = pd.concat(
    #     list(map(partial(Get_FundData_main, start_date=start_date, end_date=end_date), codes)))  # 结合map方法获取多基金数据
    # print(fund_df)
    # ans_df = fund_df.sort_values('净值日期', ascending=True)
    # ans_df.to_csv('000478.csv')
    #
    # x_val = fund_df.loc[:, '净值日期']

    and_df = pd.read_csv('000478.csv')
    # 添加序号
    and_df.rename(columns={'index': '序号'}, inplace=True)
    and_df['序号'] = range(1, len(and_df) + 1)

    x = and_df.loc[:, '序号']
    y = and_df.loc[:, '单位净值']
    x = x.values.reshape(len(and_df), 1)
    y = y.values.reshape(len(and_df), 1)
    clf2, x_p = un_linear_regression(x, y, 6)

    plt.plot(x, y, label="实际数据")
    plt.plot(x, clf2.predict(x_p), label="非线性回归")

    print(test_func(clf2, 2344))
    plt.legend()
    plt.show()
