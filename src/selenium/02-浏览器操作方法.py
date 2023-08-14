from time import sleep
from selenium import webdriver

"""
应用：driver.maximize_windows()  # 窗口最大化
	 driver.set_window_size(w,h) # 设置浏览器大小 【了解】
	 driver.set_window_position(x,y) # 设置浏览器窗口位置 【了解】
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    # 窗口最大化
    driver.maximize_window()
    sleep(1)
    # 设置浏览器宽，高 【了解】
    driver.set_window_size(1000, 1000)
    sleep(1)
    # 设置窗口浏览器位置  【了解】
    driver.set_window_position(200, 200)

    # 退出
    sleep(3)
    driver.quit()
