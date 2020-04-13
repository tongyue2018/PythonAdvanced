class Dog:
    belongTo = 'meet' #静态属性共享
    def __init__(self,name,age):#创建对象时自动执行
        self.name = name
        self.age = age
    def getName(self,atachInfo):
        return(self.name+atachInfo)

    def getName1(self):
        return("abc")

    @staticmethod
    def roar():  #不需要访问实例，所以不需要传入self
        print("wow!!!")

if __name__ == '__main__':#自己调用时True,被引用时为False
    myDog = Dog('大牛', 20)
    print("父类名字:" + myDog.getName("123"))
    myDog.getName()

# if __name__ == '__main__': 同时适用于函数，也可以防止测试代码被调用 引发生产bug


# 静态方法、静态变量调用，直接Dog.a 、 Dog.abc()
# 静态方法 参数里面不必要有self
# 动态方法 参数里面一定要有self
