from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
1.、为什么要设置元素等待
由于电脑配置或网络原因，在查找元素时，元素代码未在第一时间内被加载出来，而抛出未找到元素异常。
2、什么是元素等待
元素在第一次未找到时，元素等待设置的时长被激活，如果在设置的有效时长内找到元素，继续执行代码，如果超出设置的时长未找打元素，抛出未找到元素异常。
3、元素等待分类
隐式等待：针对全局元素生效；（讲这个）
显示等待：稍微麻烦，有兴趣的可以下去了解，他是针对单个元素生效。
"""

"""
隐式等待
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 1、获取浏览器驱动对象
    driver.get('file:///D:/%E6%A1%8C%E9%9D%A2/page/%E6%B3%A8%E5%86%8CA%E7%AD%89%E5%BE%85.html')
    # 2、窗口最大化
    driver.maximize_window()
    # 3、设置隐式等待
    driver.implicitly_wait(30)
    ele = driver.find_element(By.ID, 'userA')
    ele.send_keys('admin')

    sleep(3)

    driver.quit()
