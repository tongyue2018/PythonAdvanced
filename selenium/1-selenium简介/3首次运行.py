from selenium import webdriver

#指定safira的驱动
#执行到这里时selenium会到指定路径将driver运行起来

driver = webdriver.Chrome(r"D:\Users\tongyue\tools\chromedriver.exe")

driver.get('https://www.baidu.com')  #自带驱动，会等待页面加载完成再执行下面代码

print(driver.get_cookies())



# 找元素id方法一：
text = driver.find_element_by_id("kw")
text.send_keys("吉林") #输入文本

# 找元素id方法二：
# from selenium.webdriver.common.by import By
# text = driver.find_element(by = By.ID,value='kw')
# text.send_keys("吉林")

enter = driver.find_element_by_id("su") #百度一下按钮
enter.click();#点击按钮

import time #点击跳转事件到下个页面时需要等待，否则页面未加载完成就执行下面代码，找不到元素
time.sleep(2)

text2 = driver.find_element_by_id("5");
print(text2.text)


