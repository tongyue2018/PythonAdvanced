# @Time : 2020/3/29 23:45 
# @Author : tongyue
import json

#list 或者 dict都可以

with open('../data/json.txt','r',encoding="utf-8") as f:
    data = f.read()
    dataChuli = json.loads(data)
    print(dataChuli)
