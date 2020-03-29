# @Time : 2020/3/30 0:07 
# @Author : tongyue

# 函数如果实现了 __enter__, __exit__两个函数，就可以用with语句，with会自动在执行内容前后调用这2个方法

#常用于 执行sql，需要释放资源

class shangxue():
    def __enter__(self):
        print('代码执行前------------')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('代码执行后------------')

with shangxue():
    print('代码执行中')