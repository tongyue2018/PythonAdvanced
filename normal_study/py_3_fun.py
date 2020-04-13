
print("===============内置函数常用方法===============")

a = "98765432123456789"
print(a.count("3-等待元素、frame、css选择"))#存在多少个XX字符串
print(a.startswith("3-等待元素、frame、css选择"))#是否以xx字符开头
print(a.endswith("4"))#是否以xx字符结尾
print(a.find("123"))#找到xx字符串所在位置（从0开始数）
print(a.find("1234"))#不存在则返回-1
print(a.find("8",3))#从下标3开始找包含下标3，找到"8"的位置
print(a.isalpha())#是否包含字母
print(a.isdigit())#是否包含数字


a = ['a','b','c']
b = ' '.join(a) #list生成1个字符串,不影响原list
b = ' -- '.join(a) #list生成1个字符串,不影响原list
print(b)
print(type(b))
print(a)

a = 'ab cd e'
b = a.split(" ")#字符串分割成list，不影响原字符串
c = a.split(" ")[-1]#字符串分割成list，并且取字符串最后1个字符
print(b)
print(a)
print(c)

print(a.lower())
print(a.upper())
print(a.replace("a","e"))
print(a)

a = '  ab cd e '
b = a.strip()
print(a)
print(b)
print(a.lstrip())
print(a.rstrip())

a = ['a','b','c']
print(a.pop(1))
print(a)
print(a.pop())
print(a)

a = "987654312123456789"
print(a.rfind("3-等待元素、frame、css选择",2))


