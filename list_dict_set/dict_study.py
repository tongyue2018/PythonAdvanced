# @Time : 2020/4/13 15:16 
# @Author : tongyue
# update
dictData = {
    "name":"xiaoming",
    "age":20
}

print("-------------遍历------------")
for key,value in dictData.items():
    print("key是{}  value是{}".format(key,value))

print("-------------新增、修改都一样------------")
dictData['other'] = '无耻'
print(dictData)

print("-------------删除------------")
del(dictData['other'])
print(dictData)

print("-------------对value去重------------")
a = {'color': 'green', 'point': 5,'height':5}
# 循环遍历字典value（去重）
for value in set(a.values()):
    print(value)

print("-------------判断是否包含某个key------------")
print('color' in a.keys())