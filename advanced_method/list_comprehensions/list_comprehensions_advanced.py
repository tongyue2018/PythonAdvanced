# @Time : 2020/3/30 19:24 
# @Author : tongyue

print('-----------普通列表推导式------------')
a = [i**2 for i in range(1,6)]
print(a)

print('-----------带if列表推导式------------')
a = [i**2 for i in range(1,6) if i != 1]
print(a)

print('-----------嵌套循环列表推导式------------')
a = [i*j for i in range(1,6) for j in range(1,6)]
print(a)