
#普通函数
def oddfn(x):
    return x if (x == 2) else False

#anonymous function匿名函数  lambda

square = lambda x, y, z: x ** 2 + y ** 2 + z**2

print(square(1, 2, 3))

#filter() 过滤  #高级用法  用于过滤不存在的变量  intros = filter(lambda x: True if x else False,[self.author,self.publisher,self.price])
myList = [1, 2, 3, 4, 5]
filter_obj1 = filter(oddfn,myList)
filter_obj2 = filter(lambda x: x ** 2 == 4, myList)
print([i for i in filter_obj1])
print([i for i in filter_obj2])

#map输出结果
filter_obj3 = map(lambda x: x ** 2 == 4, myList)
filter_obj4 = map(lambda x: x ** 2, myList)
print([i for i in filter_obj3])
print([i for i in filter_obj4])
filter_obj5 = map(oddfn, myList)