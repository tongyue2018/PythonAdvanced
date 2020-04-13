from selenium import webdriver

#指定safira的驱动
#执行到这里时selenium会到指定路径将driver运行起来

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

#打开本地网页网址
driver.get('file:///G:\py\python_study\selenium\html文件\html1.html')

#通过tag名找元素 一般不唯一，通过找多个元素
frame = driver.find_element_by_tag_name("iframe")
frames = driver.find_elements_by_tag_name("iframe")
#或者
from selenium.webdriver.common.by import By
frame = driver.find_element(By.TAG_NAME,"iframe")
frames =  driver.find_elements(By.TAG_NAME,"iframe")

print(frames)

# 浏览器退出
# driver.quit()
