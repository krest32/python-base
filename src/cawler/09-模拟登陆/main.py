import requests
from bs4 import BeautifulSoup
import re

# 下载360极速浏览器对应的Chromedriver  https://blog.csdn.net/cz9025/article/details/70160273
if __name__ == '__main__':
    # 初始化Session对象，利用session维持一个会话
    session = requests.Session()

    # 设置请求表头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

    # 设置请求的URL
    url_login = 'https://accounts.douban.com/login'

    # 设置请求表单
    form_data = {
        'redir': 'https://www.douban.com',
        'form_email': '17610041263',
        'form_password': 'duxin199310',
        'login': u'登陆'
    }

    # 用Session对象的post()方法模拟登录
    response = session.post(url_login, data=form_data, headers=headers)
    if response.status_code != 200:
        print( response.text)

    # 当登陆需要验证码的时候，获取验证码
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    captcha = soup.find('img', id='captcha_image')
    if captcha:
        captcha_url = captcha['src']
        re_captcha_id = response
        captcha_id = re.findall(re_captcha_id, content)
    print(captcha_id)
    print(captcha_url)
    captcha_text = input('Please input the captcha:')
    form_data['captcha-solution'] = captcha_text
    form_data['captcha-id'] = captcha_id

    response = session.post(url_login, data=form_data, headers=headers)

    with open('contacts.html', 'w+', encoding='utf-8') as f:
        f.write(response.text)