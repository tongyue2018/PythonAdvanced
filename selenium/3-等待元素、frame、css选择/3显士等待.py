from selenium import webdriver

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

driver.implicitly_wait(10) #隐士等待，全局设定，每半秒钟取一次元素，不需要在每个等待写time..sleep(2)


driver.get('https://www.baidu.com')  #自带驱动，会等待页面加载完成再执行下面代码



print(driver.get_cookies())

# 找元素id方法一：
text = driver.find_element_by_id("kw")
text.send_keys("吉林") #输入文本

enter = driver.find_element_by_id("su") #百度一下按钮
enter.click();#点击按钮

# import time #点击跳转事件到下个页面时需要等待，否则页面未加载完成就执行下面代码，找不到元素
# time.sleep2)
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
#等待一个id是username的元素出现，返回对象是一个list
elements =  WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.ID,'5')))
print(elements[0].text)

