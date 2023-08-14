from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://192.168.103.98:18000/user/login')
    # 窗口最大化
    driver.maximize_window()

    # 获取登陆元素
    driver.find_element(
        By.XPATH,
        '//html/body/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/span/span/input'
    ).send_keys('tk0001')
    driver.find_element(
        By.XPATH,
        '/html/body/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/span/span/input'
    ).send_keys("aa111111")

    # 点击登陆
    driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/span/button'
    ).click()
    sleep(10)

    # 点击 产品生命周期管理
    driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div[1]/section/aside/div/div/div[2]/div/div[1]'
    ).click()
    sleep(1)

    # 鼠标悬浮 组合类资产
    combineButtonEle = driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div/div[1]/section/aside/div/div/div[2]/div/div[2]/div[1]'
    )
    # 移动到固定位置、执行
    ActionChains(driver).move_to_element(combineButtonEle).perform()
    sleep(1)

    # 跳转需求管理页面
    driver.find_element(
        By.XPATH,
        '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/span[1]'
    ).click()
    sleep(7)

    ActionChains(driver).move_to_element(driver.find_element(
        By.XPATH,
        '//*[@id="area"]/span/span[2]'
    )).perform()
    sleep(1)

    driver.find_element(
        By.XPATH,
        '/html/body/div[3]/div/div/ul/li'
    ).click()

    # 鼠标执行
    sleep(10)
    driver.quit()
