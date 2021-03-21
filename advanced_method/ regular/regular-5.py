
# @Time : 2020/12/9 下午4:30
# @Author : tongyue

import re

line1 = '你好房贷首付'
line2 = '你好 房贷首付'
line3 = 'study in 南京大学'
line4 = 'xxx出生在2011年'

regex_str1 = "([\u4e00-\u9fa5]+)"  #匹配1或多个汉字
regex_str2 = "([\u4e00-\u9fa5]+)"  #匹配1或多个连续汉字，遇到了非汉字则停止
regex_str3 = ".*?([\u4e00-\u9fa5]{1,}大学)"  #匹配出大学的名字,要加？号 取消贪婪匹配，否则只打印"京大学"。
regex_str4 = ".*?(\d+)年"  #取出数字， 左边d应该不贪婪 加?从左边取多个


result1 = re.match(regex_str1,line1).group(1)
result2 = re.match(regex_str2,line2).group(1)
result3 = re.match(regex_str3,line3).group(1)
result4 = re.match(regex_str4,line4).group(1)



print('匹配汉字:'+result1)
print('匹配汉字:'+result2)
print('匹配汉字:'+result3)
print('匹配汉字:'+result4)



# 常用正则
# 1. ^ $ * ? + {2} {2,} {2,5} |  限定出现次数， | 表示或者
# 2. [] [^] [a-z] .
# 3. \s \S \w \W
# 4. [\u4e00-\u9fa5] () \d