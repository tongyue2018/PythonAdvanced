import requests,json


urlAddress = 'http://47.107.58.164:5000/regist'

params = {
    'username':'mirTong',
    'passwd':'Qwe123%25%25%25'
}

jsonData = {
	"jsonName":"jsonName哈啊哈",
	"jsonPasswd":"654321英文"
}

headers = {
    "Content-Type": "application/json",
    "headerName":"header"
}

#方法一、json提交，注意:1.json需要序列化才被python识别,  2."Content-Type": "application/json"
# responseDataJson = requests.post(url=urlAddress,data=json.dumps(jsonData),headers=headers)

#方法二、json=jsonData，headers=headers Content-Type": "application/json"
responseDataJson = requests.post(url=urlAddress,json=jsonData,headers=headers)


#直接打印中文乱码，json序列化可以解决, 简介的方法是responseDataJson.json()
# resultdata = responseDataJson.text
# print(json.loads(resultdata))

resultdata = responseDataJson.json()
print(resultdata)

