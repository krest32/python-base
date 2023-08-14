from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
步骤：
1、需要切换到对话框
	driver.switch_to.alert
2、处理对话框
	alert.text # 获取文本
	alert.accept() # 接受
	alert.dismiss() # 拒接
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('file:///D:/%E6%A1%8C%E9%9D%A2/page/%E6%B3%A8%E5%86%8CA.html')
    driver.find_element(By.ID, 'confirma').click()

    # 切换对话框
    alert = driver.switch_to.alert
    print("文本内容是：", alert.text)
    sleep(2)

    # 拒绝
    alert.dismiss()

    # 同意
    # alert.accept()

    sleep(3)
    driver.quit()
