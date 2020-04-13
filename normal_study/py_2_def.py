print("===============自定义函数def===============")


def fool(p1):
    if p1 == 1:
        print('bar1')
    elif p1 ==2:
        print('bar3')
    else:
        print('bar3')
fool(1)
fool(2)
fool(3)
fool("a")

def fool(p1,p2):
    return p1**p2+p1+p2

a = fool(2.5,3)
print(a)

print("===============自带函数===============")
print(len([1,2,3]))
print(max([1,2,3]))
print(min([1,2,3]))
print(str(1))
print(float(1))
print(int(1.9))