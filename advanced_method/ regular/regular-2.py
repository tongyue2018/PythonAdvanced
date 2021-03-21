# @Time : 2020/12/9 下午4:30 
# @Author : tongyue

import re

line = 'boobby123'
regex_str1 = '(boob|boobby)'
regex_str2 = '(boobby|boob)'
regex_str3 = '(boobby|boob)123'
result1 = re.match(regex_str1,line).group(1)
result2 = re.match(regex_str2,line).group(1)
result3 = re.match(regex_str3,line).group(1)


print('先匹配到谁打印谁:'+result1)
print('先匹配到谁打印谁:'+result2)
print('先匹配到谁打印谁:'+result3)
