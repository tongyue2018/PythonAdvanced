import requests,json,chardet
from requests.auth import HTTPBasicAuth
urlAddress = 'https://httpbin.testing-studio.com/basic-auth/banana/123'

#有的接口需要认证才可以访问
responseData1 = requests.get(url=urlAddress,auth=HTTPBasicAuth("banana","123"))
print(responseData1.text)
