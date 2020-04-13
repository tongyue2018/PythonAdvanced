print("===============再识函数def===============")


#全局变量、局部变量同java

#函数改变全局变量的值
x = 2
def setX() :
    global  x
    x = 9
setX()
print(x)