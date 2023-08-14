from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
需要默认切换到frame
方法：driver.switch_to.default_content()
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('file:///D:/%E6%A1%8C%E9%9D%A2/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')

    driver.switch_to.frame('idframe1')
    driver.find_element(By.ID, 'userA').send_keys('admin')

    driver.switch_to.default_content()
    driver.switch_to.frame('myframe2')
    driver.find_element(By.ID, 'userB').send_keys('admin4')

    sleep(3)
    driver.quit()
