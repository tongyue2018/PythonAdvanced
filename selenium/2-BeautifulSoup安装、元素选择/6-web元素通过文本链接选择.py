from selenium import webdriver

#指定safira的驱动
#执行到这里时selenium会到指定路径将driver运行起来

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

#打开本地网页网址
driver.get('file:///G:\py\python_study\selenium\html文件\html1.html')

#通过连接文本内容找元素 一般不唯一，通过找多个元素
link = driver.find_element_by_link_text("转到百度")
links = driver.find_elements_by_link_text("转到百度")
#或者
from selenium.webdriver.common.by import By
link = driver.find_element(By.LINK_TEXT,"转到百度")
links = driver.find_elements(By.LINK_TEXT,"转到百度")

#模糊匹配某个字段可用另外一种方法
linkP = driver.find_element_by_partial_link_text("度")
linkP.click()

# 浏览器退出
# driver.quit()

