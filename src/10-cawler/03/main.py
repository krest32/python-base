import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://www.python.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #  这段代码的输出前500个字符
    # print(soup.prettify()[:500])
    # 通过选择器打印
    elements = soup.select(
        "#content > div > section > div:nth-child(1) > div.small-widget.get-started-widget > p:nth-child(2)"
    )
    for element in elements:
        print(element.text)
