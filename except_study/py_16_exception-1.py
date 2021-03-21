

#自己不处理异常 可以向上抛出
def calB():
 try:
     print(5 / 0)
 except ZeroDivisionError:
     raise
     print("B处理了异常")

def calA():
    try:
        calB()
    except ZeroDivisionError:
        print("A处理了异常")
calA()

# update