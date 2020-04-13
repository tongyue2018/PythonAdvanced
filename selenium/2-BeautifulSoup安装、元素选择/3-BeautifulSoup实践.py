from selenium import webdriver

#指定safira的驱动
#执行到这里时selenium会到指定路径将driver运行起来

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

#打开本地网页网址
driver.get('file:///G:\py\python_study\selenium\html文件\html1.html')

element = driver.find_element_by_id("choose_car")
carHtml = element.get_attribute("innerHTML")

#定义一个检验标准字典
toVerify = {
    'volvo':'沃尔沃',
    'corolla':'卡罗拉',
    'flat':'菲亚特',
    'audi':'奥迪',
}

from bs4 import  BeautifulSoup
soup = BeautifulSoup(carHtml,'html5lib')

#获取所有的option为bs里面的tag对象
#对每个tag对象进行分析

for option in soup.find_all('option'):
    #获取value属性
    k = option.get('value')
    #获取文本内容
    v = option.get_text()

    if k in toVerify:
        if v != toVerify[k]:
            print(toVerify[k]+':'+'文本匹配错误')
        else:
            print (toVerify[k] + ':' + '文本匹配正确')
    else:
        print (k + ':' + '属性value匹配错误')

# 浏览器退出
# driver.quit()