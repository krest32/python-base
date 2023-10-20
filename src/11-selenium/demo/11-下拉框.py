
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
"""
Select类方法：
需要实例化下拉框元素定位
"""
"""
、为什么单独使用下拉框？
1)、如果option选项没有value值的化，css定位或其他定位就不太方便。
2、使用Select类
1）、导包：from 11-selenium.webdriver.support.select improt Select
2）、实例化下拉框：s = Select(element)
3）、调用方法：s.select_by_index()索引从0开始
3、Select类提供的方法
1）、select_by_index() # 通过索引定位
2）、select _by_value() # 通过value值
3）、select_by_visible_text() # 显示文本
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('file:///D:/%E6%A1%8C%E9%9D%A2/page/%E6%B3%A8%E5%86%8CA.html')
    ele = driver.find_element(By.ID, 'selectA')

    # 实例化下拉框
    s = Select(ele)

    # index 索引方法
    s.select_by_index(1)
    sleep(1)

    # value 属性值选择目标元素
    s.select_by_value('sz')
    sleep(1)

    # text 采用文本的方式选择目标信息
    s.select_by_visible_text('A北京')

    sleep(3)

    driver.quit()
