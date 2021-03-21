# @Time : 2020/12/9 下午4:30 
# @Author : tongyue

import re

line = 'b1aooooooba123'
regex_str1 = '.*(a.*b).*'
regex_str2 = '.*?(b.*?a).*'
regex_str3 = '.*?(b.*a).*'
regex_str4 = '.*(b.*?a).*'
regex_str5 = '(.*?(b.*?b).*)'
result1 = re.match(regex_str1,line).group(1)
result2 = re.match(regex_str2,line).group(1)
result3 = re.match(regex_str3,line).group(1)
result4 = re.match(regex_str4,line).group(1)
result5 = re.match(regex_str5,line).group(1)


print('贪婪模式-从右往左匹配，现在右侧找到b，然后在右侧找到a:'+result1)
print('非贪婪模式-从左往右匹配:'+result2)
print('非贪婪模式-:最左侧匹配到b，最右侧匹配到a'+result3)
print('非贪婪模式-可以先不用此方式:'+result4)
print('非贪婪模式-从左往右匹配，group1、2，最外层的()是1:'+result5)


# 常用正则
# 1. ^ $ * ? + {2} {2,} {2,5} |  ---解释---  限定出现次数， | 表示或者，*表示0或多个，?表示0或1，+表示1或多个
# 2. [] [^] [a-z] .   ---解释---  [^a]表示不等于a  [abc-/]表示或的关系 选择其中1个字符，.表示匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。
# 3. \s \S \w \W    ---解释---  \s表示1个空格  \w 等价于 [a-zA-Z0-9_] 1个字符， 大写与之相反
# 4. [u4E00-\u9FA5] () \d