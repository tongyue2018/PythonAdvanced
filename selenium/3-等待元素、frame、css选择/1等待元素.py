from selenium import webdriver
driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

# 选择一个元素的时候
#     代码设定一个最大等待时长
#     周期性（每隔半秒钟）重新寻找该元素，直到该元素找到（返回）
#     或者超出指定最大等待时长（返回空列表或者抛出异常）
#s
# 一、隐士等待（全局）：实现上午方案常用方法一,，在打开网页之后设定即可
driver.implicitly_wait(10)
#     全局设定，
#     后面所有的选择元素的代码都不需要单独的指定周期性等待了

# 二、显示等待（局部）：为一个操作专门指定等待时间
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
#等待一个id是username的元素出现,返回对象是一个list
elements =  WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.ID,'username')))
print(elements[0].text)