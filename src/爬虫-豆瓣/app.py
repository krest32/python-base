# 解析网页数据工具
from bs4 import BeautifulSoup
import re  # 正则表达式
import xlwt
import urllib.request, urllib.error

findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 忽略换行符
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findIBD = re.compile(r'<p class="">(.*?)</p>', re.S)


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    savePath = r".\moiveInfo.xls"

    # 爬取网页
    dataList = getDataUrl(baseUrl)
    print("获取数据完成")
    # 保存数据
    saveDataList(dataList, savePath)


# 保存数据
def saveDataList(dataList, savePath):
    print("saving...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        # print("第%d条" %(i+1))
        data = dataList[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    # 保存文档
    book.save(savePath)


# 得到特点的网页信息
def askUrl(url):
    # 伪装浏览器请求
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        # 接收请求，进行处理
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 获取数据
def getDataUrl(baseUrl):
    print("获取基本数据中...")
    dataList = []
    for i in range(0, 10):
        # 调用获取页面信息的函授 共10次
        url = baseUrl + str(i * 25)
        html = askUrl(url)
        # 逐个分析数据
        soup = BeautifulSoup(html, "html.parser")
        # 查找符合要求的字符串形成列表
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            # 用正则表达式进行规则匹配
            # 获取电影的网页连接
            link = re.findall(findLink, item)[0]
            data.append(link)
            image = re.findall(findImgSrc, item)[0]
            data.append(image)
            titles = re.findall(findTitle, item)  # 片名只有一个中文名
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")  # 留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                data.append(inq[0].replace("。 ", ""))
            else:
                data.append(" ")

            bd = re.findall(findIBD, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())  # 去掉空格
            dataList.append(data)

    return dataList


if __name__ == "__main__":
    print("开始爬取任务")
    main()
    print("保存文件成功")
