# @Time : 2020/3/30 11:18 
# @Author : tongyue

class Student:

    def __init__(self,name,__age__):
        self.name = name
        self.__age__ = __age__

    @property #函数编程 属性变量param_name
    def age(self):
        return self.__age__

    @age.setter #给属性变量param_name 赋值
    def age(self,age):
         self.__age__ = age + 20

    height = 20

stu = Student('daniu',20)
stu.age = 20 #表示要调用 setter方法，20传给参数age,age加工+20，传给__age__
print(stu.age)
