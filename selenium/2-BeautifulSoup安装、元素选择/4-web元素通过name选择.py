from selenium import webdriver

#指定safira的驱动
#执行到这里时selenium会到指定路径将driver运行起来

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

#打开本地网页网址
driver.get('file:///G:\py\python_study\selenium\html文件\html1.html')

#通过name找元素 方法一
text1 = driver.find_element_by_name("wenben1")   #如果找不到name则程序异常,如果多个返回第一个
carHtml = text1.get_attribute("outerHTML")
print(carHtml)
print(text1.text)

#通过name找元素 方法二
from selenium.webdriver.common.by import  By
text2 = driver.find_element(By.NAME,"wenben2") #如果找不到name则程序异常,如果多个返回第一个

#通过name返回所有元素list ,如果找不到不会抛出异常,返回空list
text=driver.find_elements_by_name("button3")
for textC in text:
    print(textC.text)

text=driver.find_elements_by_name("button4")
#判断页面是否有button4
#方法一(查询所有)
text=driver.find_elements_by_name("button4")
if text == []:
    print("无name是button4的元素")

#方法二（查询单个）
try:
    text = driver.find_element_by_name ("button4")
except:
    print("无name是button4的元素")

# 浏览器退出
# driver.quit()