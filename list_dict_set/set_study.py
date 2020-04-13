# @Time : 2020/4/13 15:15 
# @Author : tongyue

print('----------定义集合------------')
a = {1,2,3,4}
print(type(a))

print('----------遍历集合------------')
for i in a:
    print(i)

print('----------新增------------')
a.add(5)
print(a)

print('----------删除------------')
a.remove(5)
print(a)


print('----------#集合去重------------')
set1={1,2,3,4,5,2}
print("set1去重后：",set1)

print('----------#列表去重------------')
list1 = [3,6,9,4,5,3,5,6,7]
new_list = list(set(list1))
print(new_list)

print('----------字典的key转化为set------------')
set4 = set({'name':'zhangsan','age':20,'weigh':50})
print(set4,type(set4))

