
#字典特性
#1.是mutable类型
#2.存储任意数量元素
#3.存储任何pythoness、数据类型
#    value可以是任何类型
#    key可以hash的类型，最常用的效率也是最高的是数字和字符串
#    key是唯一的

# list string tuple特性称之为sequence
# dict字典 特性称之为map（映射）

#初始化字典
a = {'color':'green','point':5}
print(a)
print(a['color'])
print(a['point'])

#添加 修改字典
a['heigh']=60
print(a)
a['heigh']=80
print(a)

#循环遍历字典key&value
for key,value in a.items():
    print("key: %s----value: %s" % (key,value))
# 循环遍历字典key
for key in a.keys():
    print(key)


#是否存在某个key
if  'color' in a.keys():
    print("有此key")

a = {'color':'green','point':5,'height':5}
# 循环遍历字典所有value
for value in a.values():
    print(value)

a = {'color': 'green', 'point': 5,'height':5}
# 循环遍历字典value（去重）
for value in set(a.values()):
    print(value)

print(type(set(a.values())))