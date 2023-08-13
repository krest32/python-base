import json
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
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 获取页面中的内容
    # print(soup.prettify())
    # 解析需要的数据
    tags = soup.find_all("div", class_='doulist-item')
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


def getData(start, count):
    # 伪装浏览器请求
    params = {
        "from_web": 1,
        "sort": "new",
        "start": start,
        "count": count,
        "status_full_text": 1,
        "guest_only": 0,
        "ck": "XI4u"
    }

    url_temp_list = "https://m.douban.com/rexxar/api/v2/gallery/topic/51644/items"

    # 伪装浏览器请求
    headers = {
        # 反爬虫 header 配置
        "Referer": "https://m.douban.com/tv/american",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

    resp = requests.get(url_temp_list, headers=headers, params=params)
    # 字符串转义出来
    return resp.text.encode('utf-8').decode('raw_unicode_escape')


if __name__ == '__main__':
    resp = getData(0, 50)
    # 加载成为字典
    data = json.loads(resp, strict=True)
    print(data)
    list = data["items"]
    print(len(list))
    # 正文内容
    text = list[3]["target"]["status"]["text"]
    # 获取头像
    avatar = list[3]["target"]["status"]["author"]["avatar"]
    print(avatar)
    # 可能存在没有照片的情况
    imgs = list[3]["target"]["status"]["images"]
    # 获取图片
    if imgs:
        imageUrls = []
        i = 0;
        while i<len(imgs):
            imageUrls.append(imgs[i]['large']['url'])
            i += 1


