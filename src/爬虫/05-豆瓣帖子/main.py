import json
import time

import requests
from bs4 import BeautifulSoup

# 伪装浏览器请求
headers = {
    # 反爬虫 header 配置
    "Referer": "https://m.douban.com/tv/american",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Cookie": 'll="108288"; bid=cbhlRmu2TOY; __utmc=30149280; __utmz=30149280.1691905290.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23211; ap_v=0,6.0; __utma=30149280.164310908.1691905290.1691905290.1691922664.2"',
    "sec-ch-ua": '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"'
}


def getData(start, count):
    time.sleep(3)
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
    resp = requests.get(url_temp_list, headers=headers, params=params)
    # 字符串转义出来
    return resp.text.encode('utf-8').decode('raw_unicode_escape')


def getNote(noteId):
    time.sleep(1)
    url = f"https://www.douban.com/j/note/{noteId}/full"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return "请求错误"
    dict = json.loads(resp.content, strict=True)
    dataStr = dict["html"].encode('UTF-8', 'ignore').decode('UTF-8')
    soup = BeautifulSoup(dataStr, 'html.parser')
    return soup.text


if __name__ == '__main__':
    total = 20
    step = 20
    start = 0
    end = start + step
    dataList = []
    listHeader = ["序号", "用户编号", "网页地址", "城市", "介绍", "头像", "附件照片数量"]
    dataList.append(listHeader)
    print(listHeader)
    while start < total:
        resp = getData(start, end)
        # 加载成为字典
        data = json.loads(resp, strict=True)
        # 获取 item
        list = data["items"]
        count = len(list)
        # 开始遍历 items
        for i in range(0, count):
            # 正文内容
            # 判断字段中是否存在 status
            city = "未知"
            shardingUrl = "未知"
            if "status" in list[i]["target"]:
                text = list[i]["target"]["status"]["text"]
                avatar = list[i]["target"]["status"]["author"]["avatar"]
                authorId = list[i]["target"]["status"]["author"]["id"]
                shardingUrl = list[i]["target"]["status"]["sharing_url"]
                if "loc" in list[i]["target"]["status"]["author"]:
                    if list[i]["target"]["status"]["author"]["loc"] is not None and "name" in \
                            list[i]["target"]["status"]["author"]["loc"]:
                        city = list[i]["target"]["status"]["author"]["loc"]["name"]
                # 可能存在没有照片的情况
                imgs = list[i]["target"]["status"]["images"]
                imgCount = 0;
                # 获取图片
                if imgs:
                    imgCount = len(imgs)
                    imageUrls = []
                    j = 0;
                    while j < len(imgs):
                        imageUrls.append(imgs[j]['large']['url'])
                        j += 1
            else:
                noteId = list[i]["target"]["id"]
                text = getNote(noteId)
                avatar = list[i]["target"]["author"]["avatar"]
                shardingUrl = list[i]["target"]["sharing_url"]
                authorId = list[i]["target"]["author"]["id"]
                city = list[i]["target"]["author"]["loc"]["name"]
            # 获取头像
            tempList = [start + i, authorId, city, text.encode('UTF-8', 'ignore').decode('UTF-8'), avatar, imgCount]
            if city == "北京":
                dataList.append(tempList)
                print(tempList)

        # 重置查找的范围
        start = end
        end = start + step
