from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
多窗口切换
driver.current_window_handle  获取当前的句柄值
driver.window_handles  获取driver启动的所有窗口句柄
driver.switch_to.window(handles[-1]) 切换窗口操作
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get('file:///D:/%E6%A1%8C%E9%9D%A2/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')

    driver.find_element(By.ID, 'ZCB').click()
    # 1、获取当前的句柄值
    # print("当前的句柄值是：", driver.current_window_handle)

    # 2、
    # 1).切换窗口操作,driver.window_handles 获取driver启动的所有窗口句柄
    handles = driver.window_handles

    # 2).切换窗口工作
    driver.switch_to.window(handles[-1])
    driver.find_element(By.ID, 'userB').send_keys('admin9')

    sleep(3)

    driver.quit()
