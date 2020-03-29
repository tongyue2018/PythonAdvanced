# @Time : 2020/3/29 23:45 
# @Author : tongyue
import json

#list 或者 dict都可以
data = [
    {
        "name":"xiaoming",
        "age":"10"
    },
    {
        "name":"daniu",
        "age":"20"
    }
]

data1 = {
        "name":"daniu",
        "age":"20"
}
with open('../data/json.txt','w',encoding="utf-8") as f:
    f.write(json.dumps(data,indent=2))
