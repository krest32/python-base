import time
from random import random

import cv2
import numpy as np
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("executable_path= r'C:\Krest WorkSpace\Program Files\py\chromedriver.exe'")

driver = webdriver.Chrome(options=options)
# 最大化窗口
driver.maximize_window()
driver.get(url='https://www.douban.com/')
driver.find_element(By.XPATH, "//*[@id='app']/html/body/div[1]/div[1]/ul[1]/li[2]")

