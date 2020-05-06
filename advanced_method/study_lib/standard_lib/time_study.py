# @Time : 2020/5/6 19:18 
# @Author : tongyue

import time

print("国外时间:{}".format(time.asctime()))

print("时间戳:{}".format(time.time()))

print("睡眠1s...")
time.sleep(1)

print('时间转化成时间元祖')
print(time.localtime())

print("当前时间转化成带格式的时间")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

now_time = time.time()
two_time_before = now_time - 24*60*60*2
two_time_before_tuple = time.localtime(two_time_before)
two_time_before_strf = time.strftime("%Y-%m-%d %H:%M:%S",two_time_before_tuple)
print("两天前的时间：{}".format(two_time_before_strf))
