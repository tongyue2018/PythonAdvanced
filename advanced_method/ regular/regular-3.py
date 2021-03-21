# @Time : 2020/12/9 下午4:30 
# @Author : tongyue

import re

line1 = 'eboobby123'
line2 = '18719078990'
line3 = '18729078990'
line4 = '***.....'

regex_str1 = '.*([abcd]oob)'  # [abcd] 符合abcd任意1个字符
regex_str2 = '(1[48357][0-9]{9})'  #14x、18x、13x、15x、17x的 手机号
regex_str3 = '(1[48357][^1]{9})'  # 不等于1出现9次
regex_str4 = '.*([.*]{3}).*'  # 符合 * 和 .中的任何1个字符,[]里面的特殊符号不会有特殊意义



result1 = re.match(regex_str1,line1).group(1)
result2 = re.match(regex_str2,line2).group(1)
result3 = re.match(regex_str3,line3).group(1)
result4 = re.match(regex_str4,line4).group(1)


if result1 and result2 and result3:
    print('符合[abcd]中任何1哥字符:'+result1)
    print('符合规则的手机号：'+result2)
    print('符合规则的手机号：'+result3)
    print('符合 * 和 .中的任何1个字符：'+result4)



