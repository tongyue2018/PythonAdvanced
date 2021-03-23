import requests,json,chardet

urlAddress = 'https://httpbin.testing-studio.com/cookies'

headers = {
    "Cookie":"hogwarts=school; hogwarts1=school1",
    "accept": "application/json"
}

cookie_data = {
    "hogwarts":"school",
    "hogwarts1":"school1"
}

#方式1
responseData1 = requests.get(url=urlAddress,headers=headers)

#方式2
responseData2 = requests.get(url=urlAddress,cookies=cookie_data)

dataStr1 = responseData1.request.headers
dataStr2 = responseData2.request.headers


print(dataStr1)
print(dataStr2)