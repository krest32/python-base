from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
CONTROL: Ctrl键
BACK_SPACE : 等价于 BACKSPACE （删除）
其他：可以藏奥Keys底层的定义

应用
# 单键
element.send_keys(Keys.XXX)
# 组合键
element.send_keys(Keys.XXX, 'a') # 注意这里的组合键都是小写
"""

"""
键盘操作
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')

    ele = driver.find_element(By.ID, 'kw')

    ele.send_keys('易烊千玺')
    sleep(1)
    # 回退
    ele.send_keys(Keys.BACK_SPACE)
    sleep(1)
    # 组合键 Ctrl + a 全选 ，注意这里的组合键都是小写
    # 全选
    ele.send_keys(Keys.CONTROL, 'a')
    sleep(1)

    # 剪切
    ele.send_keys(Keys.CONTROL, 'x')
    sleep(1)

    # 黏贴
    ele.send_keys(Keys.CONTROL, 'v')

    sleep(3)
    driver.quit()
