from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
driver.close() # 关闭当前主窗口，默认启动的界面就是主窗口
driver.quit() # 关闭全部页面
driver.title  # 获取页面标题
driver.current_url  # 获取页面地址 
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()

    # 查找文件图片链接
    driver.get('https://www.sogou.com/')
    driver.find_element(By.LINK_TEXT, '图片').click()

    # 这两个属性可以用来做断言使用
    print("当前页面标题：", driver.title)
    print("当前页面的url：", driver.current_url)

    # 这里关闭的是原始页面，而不是新的页面，只有完成页面切换才可以关闭新的页面
    # 场景：关闭单个页面使用
    driver.close()
    sleep(3)

    # 关闭浏览器驱动对象的所有页面
    driver.quit()
