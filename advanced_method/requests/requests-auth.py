import requests,json,chardet
from requests.auth import HTTPBasicAuth
urlAddress = 'https://httpbin.testing-studio.com/basic-auth/banana/123'

#方式1
responseData1 = requests.get(url=urlAddress,auth=HTTPBasicAuth("banana","123"))
print(responseData1.text)
