# @Time : 2020/3/30 20:09 
# @Author : tongyue

listData = [1,2,3,4,5]
def myData(x):
    return x >= 10

#不对原始数据产生影响
listData_new1 = [i**2 for i in listData]
listData_new2 = filter(myData,listData_new1) #返回一个对象

print(listData_new1)
print(list(listData_new2))

