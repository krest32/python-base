import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 找到对应的网页
    resp = requests.get("http://www.poycode.cn/category/coding/python/")
    # 打印返回的 code
    # print(resp.status_code)
    # 解析该html文档，便能获取到一个BeautifulSoup对象。
    soup = BeautifulSoup(resp.content, features='html.parser')
    # 格式化html输出
    # print(soup.prettify())

    # 获取所有 class='entry-title' 的h2标签
    tags = soup.find_all('h2', class_='entry-title')

    for tag in tags:
        # 找到 a 标签
        a_tag = tag.find('a')
        # 找到标签的 text，标签中的某个 tag
        subUrl = a_tag['href']
        print('一级页面：Title:[%s], URL:[%s]' % (tag.text, subUrl))

        # 解析子网页面
        subResp = requests.get(subUrl)
        subSoup = BeautifulSoup(subResp.content, features='html.parser')
        element = subSoup.select_one('#post-464 > header > h1')
        print('内容：%s' % (element.text))
