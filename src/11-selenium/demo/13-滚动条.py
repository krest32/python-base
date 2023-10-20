from time import sleep
from selenium import webdriver

"""
滚动条：selenium中没有滚动条方法，需要js代码实现
1、准备js代码："window.scrollTo(0, 1000)"
2、执行js代码：driver.execute_script(js的变量)
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.csdn.net/')

    # 1、准备js代码
    js_down = "window.scrollTo(0, 1000)"
    # 2、执行js代码，向下滚动 1000
    driver.execute_script(js_down)
    print("js 执行完毕")
    sleep(3)
    driver.quit()
