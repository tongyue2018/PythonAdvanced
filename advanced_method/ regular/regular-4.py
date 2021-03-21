# @Time : 2020/12/9 下午4:30 
# @Author : tongyue

import re

line1 = '你 好'
line2 = '你    好'
line3 = '你很好'
line4 = '你b好'

regex_str1 = '(你\s好)'  # \s表示1个空格，不能为0个空格
regex_str2 = '(你\s{1,}好)'  #\s{1,}表示1或多个空格
regex_str3 = '(你\S好)'  # \s表示1个非空格的字符，==1个，不能为0个
regex_str3 = '(你\S{0,}好)' #\S{0,}表示0或多个非空格字符
regex_str4 = '.*(你\w好).*'  # \w 等价于 [a-zA-Z0-0_], 表示1个字符。\W则是不符合这些字符的。


result1 = re.match(regex_str1,line1).group(1)
result2 = re.match(regex_str2,line2).group(1)
result3 = re.match(regex_str3,line3).group(1)
result4 = re.match(regex_str4,line4).group(1)

if result1 :
    print(result1)
    print(result2)
    print(result3)
    print(result4)




