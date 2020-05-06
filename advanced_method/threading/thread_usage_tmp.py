# @Time : 2020/3/29 23:55 
# @Author : tongyue
import threading
import time


def login():
    time.sleep(2)
    print('我先登录:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

def register():
    time.sleep(2)
    print('我先注册:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))


def index():
    time.sleep(2)
    print('我先进入主页:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

def my_main(tr1,tr2,tr3):
    # 函数参数有无()都正确了,但是不写()运行的更快些，更像多线程成
    tr1.start()
    tr2.start()
    tr3.start()

if __name__ == '__main__':
    tr1 = threading.Thread(target=login)
    tr2 = threading.Thread(target=register)
    tr3 = threading.Thread(target=index)
    my_main(tr1,tr2,tr3)

