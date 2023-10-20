from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
方法：
1、text 获取元素的文本； 如：driver.text
2、size 获取元素的大小： 如：driver.size
3、get_attribute 获取元素属性值；如：driver.get_attribute("id") ,传递的参数是元素的属性名
4、is_displayed 判断元素是否可见 如：element.is_displayed()
5、is_enabled 判断元素是否可用 如：element.is_enabled()
6、is_selected 判断元素是否被选中 如：element.is_selected()
"""

"""
text  获取元素文本 ,没有（）
size  获取元素大小 ，没有（）
get_attribute("属性名") 获取的是属性值
"""

if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get('https://www.sogou.com/')
    # 获取元素的数据信息
    ele = driver.find_element(By.ID, 'query')
    print("目标元素尺寸：", ele.size)

    new_ele = driver.find_element(By.ID, 'hanyu')
    print("目标元素文本：", new_ele.text)

    link = driver.find_element(By.LINK_TEXT, "图片")
    print("目标元素属性值：", link.get_attribute('id'))

    ele = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/div[2]/input')
    print(ele.get_attribute("value"))

    sleep(3)


    # 关闭浏览器驱动对象的所有页面
    driver.quit()
