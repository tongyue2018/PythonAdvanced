
print("python3 除法不同之处1=======================================")
print(9/4) #浮点数
print(9//4) #取整
print(2**4) #次方


print("字符串三引号，单双引号不能换行=======================================")
a = '''python is\ncool
'''
print(a)


print("字符串连接=======================================")
print("nihao\n" * 3)  #3个相同的连接在一起
print('nihao'+str(1)) #字符串合正数相连，整数需转化


print("字符序列=======================================")
a = 'abcd'
print(a[0],a[1],a[2],a[3])
print(a[-4],a[-3],a[-2],a[-1])
print(a[1:1+2]) #不包含末尾
print(a[-1+2:-1]) #不包含末尾
print(a[2:])
print(a[:2])

print("元祖=======================================")
a = tuple()
a = ('3-等待元素、frame、css选择+2','a','abc',['c','d','efg'])
print(a[3])
print(a[3][2])
print(a[3][2][1])
print(a)

print("list 查询和修改=======================================")
a=list()
a = ['3-等待元素、frame、css选择+2','a','abc',['c','d','efg']]
print(a[3])
print(a[3][2])
print(a[3][2][1])
a[3] = 0
print(a)

print("list 新增 删除=======================================")
a = ['3-等待元素、frame、css选择+2','a','abc',['c','d','efg']]
a.append('append1')
print(a)
a.insert(1,'append2')
print(a)
del(a[0])
a.remove('append2')
print(a)
b = a.pop()
print(a)
print(b)

print("list 排序 不同类型不能排序=======================================")
a = ['b','a','c']
a.sort()
a = ['b','a','c']
b = sorted(a)
print(b)
print(a)
print(len(a))
print(a.__len__())
print('=========')


print("for 循环=======================================")

a = ['b','a','c']
for i in a:
    print(i)
a = ['b','a','c']
b = list()
for i in a:
    b.append(i)
print(b)
for i in range(1,3):
    print(i)
a = list(range(1,3))
print(a)
a = list(range(2,11,2))
print(a)

b=[]
for i in range(1,10):
    b.append(i**2)
print(b)

a = [1,2,3]
print(max(a))
print(min(a))
print(sum(a))


a = [i**2 for i in range(1,10)]
print(a)

b = a[:]
print(b)

a = [i**3 for i in range(1,10)]
print(a)

a = 59
if  a > 90:
    print("成绩A")
elif a > 60:
    print("成绩B")
else:
    print("勉强及格C")

