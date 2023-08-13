import os.path

import requests
from bs4 import BeautifulSoup


def getImg(url):
    resp = requests.get(url)
    # 编码格式为 gbk
    resp.encoding = 'gbk'
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        src = img['src']
        if "upload" not in src:
            continue
        # string 前面加f，代表string中可以引用变量
        src = f"https://pic.netbian.com{src}"
        fileName = os.path.basename(src)
        print(fileName, src)
        # sb 代表写入二进制
        with open(f"美女图片/{fileName}", "wb") as fout:
            resp_img = requests.get(src)
            # 保存的是二进制流，所以是 content
            fout.write(resp_img.content)


if __name__ == '__main__':
    urls = (["https://pic.netbian.com/4kmeinv/"]
            + [
                # for 循环生成多个 url
                f"https://pic.netbian.com/4kmeinv/index_{i}.html"
                for i in range(2, 11)
            ])
    for url in urls:
        getImg(url)
