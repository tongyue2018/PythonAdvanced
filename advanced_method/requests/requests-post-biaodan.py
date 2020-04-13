import requests,json,chardet


urlAddress = 'http://47.107.58.164:5000/regist'

params = {
    'username':'大牛',
    'passwd':'Qwe123%25%25%25'
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "headerName":"headerName"
}

#表单提交  注意:1."Content-Type": "application/x-www-form-urlencoded"
responseDataBiaodan = requests.post(url=urlAddress,data=params,headers=headers)
dataStr = responseDataBiaodan.json()

#直接打印中文乱码，json序列化可以解决, 简介的方法是responseDataJson.json()
# dic = json.loads(dataStr)
print(dataStr)