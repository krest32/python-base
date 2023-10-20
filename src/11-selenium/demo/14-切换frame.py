from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
frame的切换
"""

if __name__ == '__main__':
    
    driver = webdriver.Chrome()
    driver.get('file:///D:/%E6%A1%8C%E9%9D%A2/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')

    # 切换到frame
    driver.switch_to.frame('idframe1')
    # 在frame表单中填写信息
    driver.find_element(By.ID, 'userA').send_keys('admin')

    sleep(3)

    driver.quit()
