# @Time : 2020/4/13 15:15 
# @Author : tongyue

print('----------遍历------------')
listData = ['daniu',1,"xiaoniu"]

for line in listData:
    print(line)

print('----------查找元素位置------------')
print(listData.index('daniu'))


print('----------新增------------')
a = 'wuchi'
listData.append(a)
print(listData)

print('----------删除remove------------')
a = ['a',1,'s',2,'s']
a.remove('s')#只能删除1个值不能删除所有
print(a)
#循环删除a中所有包含's'的值
a = ['a',1,'s',2,'s']
while 's' in a:
    a.remove('s')
print(a)

print('----------删除pop 有返回值------------')
a = ['a',1,'s',2,'s']
a.pop()
a.pop(0)
print(a)

print('----------修改------------')
listData[0]='daniu1'
print(listData)

print('----------insert------------')
listData.insert(0,"tong")
print(listData)


print('----------复制list------------')
listDataNew = listData[:]
print(listDataNew)

print('----------复制list一部分------------')
listDataNew = listData[0:2]
print(listDataNew)

print('----------排序sort------------')
a = ['a','b','s','d','g']
b = [5,4,3,2]
a.sort()
b.sort(reverse=True)
print(a)
print(b)