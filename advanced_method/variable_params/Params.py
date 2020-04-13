# @Time : 2020/3/30 20:01 
# @Author : tongyue


print("----------可变参数-----------")
a = [1,2,3,4,5]
def cal(*numbers):#非必传
    total = 0
    for n in numbers:
        total = total + n * n
    return total
print('*numbers  直接传入参数可变的数字 cal(*a): %s' % cal(1,2,3,4)) #直接传入参数
print('*numbers  list类型传入 cal(*a): %s' % cal(*a)) #展开a列表

#参数 传入make(list[:]_表示传入list副本
def cal(numbers):
    total = 0
    for n in numbers:
        total = total + n * n
    return total
print('直接传入a的副本a[:]: %s' % cal(a[:]))

# make(**a)表示传入1个字典,非必填参数 但是传值一定是zidian = {'height': '200'}，不能只传zidian，可传**字典把参数展开
def register(name,age,**args):
    print('name:%s age:%s others:%s' % (name,age,args))
register('大牛',12)
register('大牛',12,zidian = {'height': '200'}) #不建议使用，这样的话相当于传入{'zidian': {'height': '200'}}
zidian = {'height': '200'}
#register('大牛',12,zidian )
register('大牛',12,**zidian) #字典的可变参数 需要把字典展开
register('大牛',12,a='a',b='b') #a='a',b='b'代表字典的两个内容，参数是x=xx时会传给**zidian

# def register(name,age,*args): #没多大意义
#     print('name:%s age:%s others:%s' % (name,age,args))
#     print(type(args))
#     print(args)
# zidian = {'height': '200'}
# register('大牛',12,zidian)#字典被转化成了元祖
#

