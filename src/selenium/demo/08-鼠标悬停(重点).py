from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""
鼠标操作：
# 鼠标悬停 【重点】
action.move_to_element(element)
注意：
    selenium 框架虽然提供了 鼠标右键方法，但是没有提供选择右键菜单方法，
    可以通过键盘快捷键操作实现
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.maximize_window()
    # 用戶屏幕顶端
    ele = driver.find_element(By.ID, 's-usersetting-top')

    # 实例化鼠标
    action = ActionChains(driver)
    # 鼠标悬停
    action.move_to_element(ele)
    # 鼠标执行
    action.perform()

    sleep(3)

    driver.quit()
