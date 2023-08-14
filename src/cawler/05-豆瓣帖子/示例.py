# coding=utf-8
import requests
import json


class DoubanSpider():
    """豆瓣爬虫"""

    def __init__(self):
        self.url_temp_list = [
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/gallery/topic/51644/items?from_web=1&sort=new&start=0&count=20&status_full_text=1&guest_only=0&ck=XI4u",
                "country": "UK"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/gallery/topic/51644/items?from_web=1&sort=new&start=0&count=20&status_full_text=1&guest_only=0&ck=XI4u",
                "country": "CN"
            }
        ]
        self.headers = {"Referer": "https://m.douban.com/tv/american",
                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

    def parse_url(self, url):
        # 获取数据
        print(url)
        response = requests.get(url, headers=self.headers)
        print("data")
        # 字符串处理
        s = response.text.encode('utf-8').decode('unicode_escape')
        # 如果是json的话，转化为json
        json1 = json.loads(s, strict=False)
        print(json1)
        return response.content.decode()

    def get_content_list(self, json_str):
        # 提取数据
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"]
        return content_list, total

    def save_content_list(self, count_list,country):
        # 储存数据
        with open("file/douban_tv.txt", "a", encoding='utf-8') as f:
            for count in count_list:
                count["country"]=country
                f.write(json.dumps(count, ensure_ascii=False))
                f.write("\n")
        print("数据保存成功")

    def run(self):
        """主要逻辑的实现"""
        for url_temp in self.url_temp_list:
            num = 0
            total = 100
            while num < total + 18:
                # 1. start_url
                url = url_temp["url_temp"].format(num)
                # 2. 获取数据
                json_str = self.parse_url(url)
                # 3. 提取数据
                content_list, total = self.get_content_list(json_str)
                # 4. 保存数据
                self.save_content_list(content_list,url_temp["country"])
                # if len(count_list)<18:
                #     break
                # 5. 创建下一个url
                num += 18


if __name__ == '__main__':

    douban = DoubanSpider()
    douban.run()

