import random
import time

import requests
from bs4 import BeautifulSoup


# 爬取豆瓣爱情电影
def askUrl(url):
    # 伪装浏览器请求
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }

    resp = requests.get(url, headers=head)
    if resp.status_code != 200:
        print("请求错误")
        print(resp.content)
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 获取页面中的内容
    # print(soup.prettify())
    # 解析需要的数据
    tags = soup.find_all("div", class_='doulist-item')
    #
    for tag in tags:
        # 选择其中的一个标签
        titleTag = tag.select_one("div > div.bd.doulist-subject > div.title > a")
        # 选择其中的 评分
        ratingNum = tag.select_one("div > div.bd.doulist-subject > div.rating > span.rating_nums")
        # 选择评分人数
        ratingPeople = tag.select_one("div > div.bd.doulist-subject > div.rating > span:nth-child(3)")
        # 主演
        detailTage = tag.select_one(" div > div.bd.doulist-subject > div.abstract")
        detailInfo = detailTage.text.strip().replace('\n', ',').replace(' ', '').replace(',,', ',')

        (print
            (
            "标题：[%s], 评分:[%s], 评分人数:[%s], 详细信息:[%s]"
            %
            (titleTag.text.strip(), ratingNum.text.strip(), ratingPeople.text.strip(), detailInfo)
        ))


if __name__ == '__main__':
    # 伪装浏览器请求
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    # 爱情电影列表
    # url = "https://www.douban.com/doulist/30327/"
    # 8分日剧
    url = "https://www.douban.com/doulist/940176/"
    # 获取网页地址

    # 伪装浏览器请求
    resp = requests.get(url, headers=head)
    soup = BeautifulSoup(resp.text, 'html.parser')
    elements = soup.select("#content > div > div.article > div.paginator > a")
    list = [url]
    for element in elements:
        list.append(element['href'])

    # 获取详细信息
    for i, tempUrl in enumerate(list):
        askUrl(tempUrl)
        # 停顿 1~5秒
        if (i < len(list) - 1):
            randomInt = random.randint(1, 3)
            print("停顿 %s s" % (randomInt))
            time.sleep(randomInt)
