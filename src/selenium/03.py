from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
driver.back()
driver.forward()
driver.refresh()
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get('https://www.sogou.com/')
    # 查询
    print("查询")
    driver.find_element(By.CSS_SELECTOR, '#query').send_keys('易烊千玺')
    driver.find_element(By.ID, 'stb').click()
    sleep(2)

    # 后退
    print("后退")
    driver.back()
    sleep(2)

    # 前进
    print("前进")
    driver.forward()
    sleep(2)

    # 刷新
    print("刷新")
    driver.refresh()

    # 退出
    print("退出")
    sleep(2)
    driver.quit()
