from selenium import webdriver

#指定safira的驱动
#执行到这里时selenium会到指定路径将driver运行起来

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

#打开本地网页网址
driver.get('file:///G:\py\python_study\selenium\html文件\html1.html')

element = driver.find_element_by_id("food")

#打印 id：food下所有text内容
print(element.text)
print('style属性值：'+element.get_attribute('style'))
#获取元素属性值一（一般用于打印片段帮组分析问题、 内部元素id位置，全部取出处理）
print('打印整个html片段（包含获得id那一段）:'+element.get_attribute('outerHTML'))
print('打印内部html片段（不包含获得id那一段）:'+element.get_attribute('innerHTML'))

#获取元素属性值二
element = driver.find_element_by_id("baidulink1")
print('href属性值：'+element.get_attribute('href'))

