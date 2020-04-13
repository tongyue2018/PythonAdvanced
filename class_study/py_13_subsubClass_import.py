import sys
# sys.path.append('E:\\pythonProject\\python_study\\pythonStart\\初学(2)')
sys.path.append('../') #效果和上面绝对路径一致
print(sys.path)

from 类.py_12_subClass import MDog
class LDog(MDog):
    def __init__(self,name,age,height,width):
        super().__init__(name,age,height)
        self.width = width
    #父类的方法可重新定义
lDog = LDog('三牛','20','200',2000)

print("子子类name:" + lDog.getName('abc'))
print("子子类age:"+ str(lDog.age))
print("子子类height:" + str(lDog.height))
print("子子类height:" + str(lDog.width))
print("父类的共享属性:"+lDog.belongTo)
LDog.roar() #可用类直接调用
#LDog.getName() 不能直接调用实例方法 需要创建对象



