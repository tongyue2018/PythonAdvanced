

i = 0
while i < 10:
    i += 1#放到continue免会死循环
    if i % 2 == 0:
        continue
    print(i)

a = ['a',1,'b',2,'c']
b = []
while a :
    i = a.pop()
    b.append(i)
print(b)

a = ['a',1,'s',2,'s']
a.remove('s')#只能删除1个值不能删除所有
print(a)

#循环删除a中所有包含's'的值
a = ['a',1,'s',2,'s']
while 's' in a:
    a.remove('s')
print(a)

