# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome drive 下载地址
if __name__ == '__main__':
    # 实例化浏览器
    driver = webdriver.Chrome()
    # 打开网址
    driver.get('https://www.baidu.com/')

    # 需求
    ele = driver.find_element(By.XPATH, '//*[@id="kw"]')
    ele.send_keys('易烊千玺')
    sleep(2)

    # 清空
    ele.clear()
    ele.send_keys('王嘉尔')

    # 时间轴看效果
    sleep(3)
    # 关闭页面
    driver.quit()

# 方法
"""
1、driver.maximize_window()  # 最大化浏览器
2、driver.set_window_size(w,h)  # 设置浏览器大小 单位像素 【了解】
3、driver.set_window_position(x,y)  # 设置浏览器位置  【了解】
4、driver.back() # 后退操作
5、driver.forward() # 前进操作
6、driver.refrensh() # 刷新操作
7、driver.close() # 关闭当前主窗口（主窗口：默认启动那个界面，就是主窗口）
8、driver.quit() # 关闭driver对象启动的全部页面
9、driver.title # 获取当前页面title信息
10、driver.current_url # 获取当前页面url信息
"""
