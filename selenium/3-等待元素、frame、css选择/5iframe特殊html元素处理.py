from selenium import webdriver

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

driver.implicitly_wait(10) #隐士等待，全局设定，每半秒钟取一次元素，不需要在每个等待写time..sleep(2)

driver.get('https://music.163.com/#/discover/toplist')  #自带驱动，会等待页面加载完成再执行下面代码

#id = auto-id-qrn024mDeCqOZhsi 不能用，后面的字母是随机生成的，每次打开会变化

# iframe的不能像下面这么调用
# div = driver.find_element_by_id("song-list-pre-cache")

#什么是iframe ： http://www.w3school.com.cn/html/html_frames.asp

#寻找iframe元素方法如下：
#切换到frame里面三种写法
driver.switch_to.frame("contentFrame")
#driver.switch_to.frame(0)
#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    #contentFrame可以是frame元素的name属性或者ID属性（常用）
    #contentFrame可以填写索引值（从0开始）：0
    #contentFrame可以填写frame所对应的WebElement:driver.find_element_by_tag_name("iframe")
div = driver.find_element_by_id("song-list-pre-cache")
print(div.text)

#切换到frame里面以后无法找导航栏内容

print("============================================================")
#切换回主html页面，才能找导航栏（iframe以外的内容）
driver.switch_to.default_content()
element = driver.find_element_by_id("g_nav2")
print(element.text)
driver.quit()

driver.quit()
