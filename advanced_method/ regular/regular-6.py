# @Time : 2020/12/9 下午4:30 
# @Author : tongyue

import re

line1 = 'xxx出生于2001年6月1日'
line2 = 'xxx出生于2001/6/1'
line3 = 'xxx出生于2001-6-1'
line4 = 'xxx出生于2001-06-01'
line5 = 'xxx出生于2001-06'
line6 = 'xxx出生于2001-6'

listStr = []
listStr.append(line1)
listStr.append(line2)
listStr.append(line3)
listStr.append(line4)
listStr.append(line5)
listStr.append(line6)

regex_str = '.*出生于?(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]|$))'

resultAll = []
for listS in listStr:
    result = re.match(regex_str,listS)
    resultTemp = (result.group(1))
    resultAll.append(resultTemp)

for i in resultAll:
    print(i)


# 常用正则
# 1. ^ $ * ? + {2} {2,} {2,5} |  限定出现次数， | 表示或者
# 2. [] [^] [a-z] .
# 3. \s \S \w \W
# 4. [u4E00-\u9FA5] () \d