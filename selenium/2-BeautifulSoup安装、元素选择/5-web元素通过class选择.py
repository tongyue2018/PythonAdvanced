from selenium import webdriver

#指定safira的驱动
#执行到这里时selenium会到指定路径将driver运行起来

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

#打开本地网页网址
driver.get('file:///G:\py\python_study\selenium\html文件\html1.html')

#通过class找元素 一般不唯一，通过找多个元素
cheeses = driver.find_elements_by_class_name("cheese")
#或者
from selenium.webdriver.common.by import By
cheeses = driver.find_elements(By.CLASS_NAME,"cheese")

for ch in cheeses:
    print(ch.get_attribute("outerHTML"))

# 浏览器退出
# driver.quit()