from selenium import webdriver

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

driver.implicitly_wait(10) #隐士等待，全局设定，每半秒钟取一次元素，不需要在每个等待写time..sleep(2)

driver.get('https://www.baidu.com')  #自带驱动，会等待页面加载完成再执行下面代码

#还没开始学习
