dataA = {}
dataA['FIRST_NAME'] = 1
dataA['LAST_NAME'] = 2
dataA['AGE'] = 3
dataA['SEX'] = 4
dataA['INCOME'] = 5

dataList = dataA.keys()
print(type(dataList),dataList)
str = ','.join(dataList)
print(str)

valuesB = ['%s'] * 5
print(valuesB)

#常用，作用于列表
valuesA = ','.join(valuesB)
print(valuesA)
#字符转化成list
print(valuesA.split(','))

#作用不大
valuesC = ['%s'* 5]
print(valuesC)


