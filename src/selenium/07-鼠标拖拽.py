from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""
鼠标操作：
# 鼠标拖拽
action.drag_and_drop(source， target)
"""
if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get('file:///D:/%E6%A1%8C%E9%9D%A2/page/drag.html')

    red = driver.find_element(By.XPATH,'//*[@id="div1"]')
    blue = driver.find_element(By.XPATH,'//*[@id="div2"]')

    # 实例化鼠标
    action = ActionChains(driver)
    # 鼠标拖拽
    action.drag_and_drop(red, blue)
    # 鼠标执行
    action.perform()

    sleep(3)

    driver.quit()
