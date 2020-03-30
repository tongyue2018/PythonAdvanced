# @Time : 2020/3/30 18:40 
# @Author : tongyue

books =[
    {
        "name":"kongzi",
        "publisher":"beijing"
    },
    {
        "name":"mengzi",
        "publisher":"shanghai"
    }
]

#遍历list和dict
for book in books:
    for key,value in book.items():
        print("key shi:{},    zhi shi:{}".format(key,value))


# 遍历set
setData = {11,22,33,44}
for data in setData:
    print(data)

#list去重 用set
listData = [1,2,2,3,4]
listSetData = set(listData)
listData = list(listSetData)
print(listData)

#两个字典合并
dict1 = {
        "name":"kongzi1",
        "publisher":"beijing1"
    }
dict2={
        "name":"mengzi2",
        "publisher":"shanghai2"
    }

dict1.update(dict2)
print(dict1)
