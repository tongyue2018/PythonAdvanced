
#增强版格式化输出功能，2种写法
name = '大牛'
age = 10
print('你是{name},你的年龄是{age}'.format(name=name,age=age))
print('你是{},你的年龄是{}'.format(name,age))


#精准控制格式化输出  %+-5s  %+-5d %+-5.5f  8进制：%+-5.5o  16进制：%+-5.5x
x = 5
print("|%6d|" % x) #左侧不足以空格补齐
print("|%-6d|" % x) #右侧不足以空格补齐

y = 10.5
print("|%6.2f|" % y) #6是总位数，包含小数点
print("|%-6.2f|" % y)

z = ("洪水发",98,90,188)
print("%3s %4d %4d %4d" % z)
print("%3s %4d %4d %4d" % z)
print("%3s %4d %4d %4d" % z)
