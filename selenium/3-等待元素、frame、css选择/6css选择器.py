#什么是CSS选择器：是浏览器用来选择元素的
#内联（inline）样式
#样式表（内部、外部）
#执行效率高
#html中没有标记css修饰也可以用css选择器

#后代（descendant）选择器
# 选择元素 内部 的元素
# 语法
# <tag1> <tag2>
    #选择tag1元素，里面所有tag2元素可以选择
    #可以是直接子节点，也可以不是
    #比如
    #choose_car option
    #footer p
    #也可以很多级
    #ul ol li em {color:blue;}


#CSS选择元素的方法
    # 根据tag(标签)名
    # p{color:red;}

    # 根据ID
    # food{color:red;}

    # 根据class
    # .vegetable{color:red;}

    # 根据tag名和class组合写（如果多个）
    # span.vegetable{color:red;}

# 详细案例见./html_css1.html;

from selenium import webdriver

driver = webdriver.Chrome(r"G:\tools\PyCharm\web-Driver\chromedriver.exe")

driver.implicitly_wait(10) #隐士等待，全局设定，每半秒钟取一次元素，不需要在每个等待写time..sleep(2)

driver.get('file:///G:\py\py_pyCharm\selenium\html文件\html_css1.html')  #自带驱动，会等待页面加载完成再执行下面代码

# 根据tag(标签)名
# p{color:red;}
elemenmts = driver.find_elements_by_css_selector('p')
for elemenmt in elemenmts:
    print(elemenmt.get_attribute("outerHTML"))


print("=====================根据ID=================================")
elemenmts = driver.find_elements_by_css_selector('#head-paragraph')
for elemenmt in elemenmts:
    print(elemenmt.get_attribute("outerHTML"))

print("========================# 根据class==============================")
elemenmts = driver.find_elements_by_css_selector('.vegetable')#寻找class时具备2属性('.vegetable.good')
for elemenmt in elemenmts:
    print(elemenmt.get_attribute("outerHTML"))

print("=========================根据tag名和class组合写（如果多个）=============================")
elemenmts = driver.find_elements_by_css_selector('span.meet')
for elemenmt in elemenmts:
    print(elemenmt.get_attribute("outerHTML"))

print("=========================寻找同时具备2个属性的=============================")
elemenmts = driver.find_elements_by_css_selector ('span.vegetable.good')
for elemenmt in elemenmts:
    print (elemenmt.get_attribute ("outerHTML"))
print("======================================================")



