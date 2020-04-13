#使用异常可避免程序崩溃
try:
    print(5/0)
except ZeroDivisionError:
    print("被除数不能为0")


fileName = 'a.txt'
try:
    with open(fileName) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    print(fileName+"文件没找到")
else:
    print("如果文件存在，则开始操作")

fileName = 'a.txt'
try:
    with open(fileName) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    pass #站位，一声不吭
else:
    print("如果文件存在，则开始操作")
finally:
    print("有无异常都要执行")

#总异常
try:
    print(5/0)
except: #总异常
    print("no")

#获取哪种异常 Exception是所有异常的父类
try:
    print(5/0)
except Exception as e:
    print("unknow exception:",e)

import traceback  #打印异常信息
try:
    IMPO
except:
    print("异常信息："+traceback.format_exc())
print("继续执行")


#自定义异常
class NameToolLongError(Exception):
    pass
class NameToolShortError(Exception):
    pass
def inputname():
    name = input('请输入姓名:')
    if len(name) > 10:
        raise NameToolLongError
    if len(name) < 6:
        raise NameToolShortError
try:
    inputname()
except NameToolLongError:
    print("name too long")
except NameToolShortError:
    print("name too short")



