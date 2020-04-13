#message = input("input something:")
#print(message)

#message = '''
#if you tell usxxx
#what is your first name?'''

#message = input(message)
#print(message)0


i = 1
while i <= 5:
    print(i)
    i += 1

isTrue = True
while isTrue:
    message = input("请输入（quit结束 0退出循环）：")
    if message == 'quit':
        isTrue = False
    elif message == '0':
        break
    else:
        print(message)











