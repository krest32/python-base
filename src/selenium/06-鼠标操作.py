from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""
1、context_click(element) # 右击
2、double_click(element)  #双击
3、double_and_drop(source, target)  # 拖拽
4、move_to_element(element)  # 悬停 【重点】
5、perform()  # 执行以上事件的方法 【重点】
"""
"""
鼠标操作：
context_click() 右键
double_click() 鼠标双击
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    # 定位目标
    ele = driver.find_element(By.ID, 'kw')
    # 实例化 鼠标对象
    action = ActionChains(driver)

    # 鼠标右键
    action.context_click(ele)
    # 鼠标双击
    action.double_click(ele)

    # 鼠标执行操作！！！不执行没效果
    action.perform()
    sleep(3)
    driver.quit()
