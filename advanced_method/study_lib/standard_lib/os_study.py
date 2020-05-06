# @Time : 2020/5/6 18:59 
# @Author : tongyue

import os

# 创建目录（tmp要为已有目录）
# os.mkdir('tmp/mulu1')

os.mkdir('tmp/mulu2')
# 删除目录
os.removedirs('tmp/mulu2')

# 获取当前目录
print('当前目录是:{}。{}'.format(os.getcwd(),"--结束"))

#目录tmp是否存在
if not os.path.exists('tmp'):
    os.mkdir('tmp')
elif not os.path.exists('tmp/tmp.txt'):
    with open('tmp/tmp.txt', 'w', encoding='utf-8') as f:
        f.write("a b c")