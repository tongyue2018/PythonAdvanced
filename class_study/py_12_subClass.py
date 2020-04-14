
import sys
# sys.path.append('E:\\pythonProject\\python_study\\pythonStart\\初学(2)')
# sys.path.append('../') #效果和上面绝对路径一致
# print(sys.path)

from py_11_class import Dog #导入类
class MDog(Dog):
    def __init__(self,name,age,height):
        super().__init__(name,age)
        self.height = height
if __name__ == '__main__':#自己调用时True,被引用时为False
    niniDog = MDog('二牛', 10, 100)
    print("子类name:" + niniDog.name)
    print("子类age:" + str(niniDog.age))
    print("子类height:" + str(niniDog.height))
