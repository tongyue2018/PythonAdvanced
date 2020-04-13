

def fool(p1 = 2):
    # 缺醒参数，可不传参数，默认为2
    if p1 == 1:
        print('bar1')
    elif p1 ==2:
        print('bar2')
    else:
        print('bar3')

fool()

def make(p1):
    if p1 == 1:
        print('bar1')
    elif p1 ==2:
        print('bar2')
    else:
        print('bar3')
#make() 无默认值时一定要传参数


fool(1)
make(2)