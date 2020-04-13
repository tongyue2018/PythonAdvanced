# @Time : 2020/3/29 23:55 
# @Author : tongyue
import threading


def login():
    print('我先登录')

def register():
    print('我先注册')


def index():
    print('我先进入主页')

#函数参数有无()都正确了
tr1 = threading.Thread(target=login)
tr2 = threading.Thread(target=register())
tr3 = threading.Thread(target=index)

tr1.start()
tr2.start()
tr3.start()