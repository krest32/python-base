from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
验证码：
{'name':'BDUSS',
'value':'............................'}
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.douban.com/')
    driver.maximize_window()

    # 1、整理cookie信息为字典数据，对应的是name和value，保存的一个变量中
    # 豆瓣 登陆 cookies
    cookie_value = {
        'name': 'dbcl2',
        'value': '。。。'
    }

    # 2、调用方法添加cookie
    driver.add_cookie(cookie_value)

    # 3、刷新页面 -->发送cookie给服务器验证
    driver.refresh()
    element = driver.find_element(By.XPATH, '//*[@id="statuses"]/div[2]/div[1]/div/div/div[1]/div[2]/a')
    print(element.text)
    sleep(10)

    driver.quit()
