
#字典特性
#1.是mutable类型
#2.存储任意数量元素
#3.存储任何pythoness、数据类型
#    value可以是任何类型
#    key可以hash的类型，最常用的效率也是最高的是数字和字符串
#    key是唯一的

# list string tuple特性称之为sequence
# dict字典 特性称之为map（映射）

#初始化字典

students = {
    'Mike' : {
        'age':25,
        'height':180,
        'nikeName':'aMike'
    },
    'Douge': {
        'age':28,
        'height':150,
        'nikeName':'aDouge'
    }
}

#获取Douge的key age
#print(students['Douge']['age'])

#遍历所有值
for key,student in students.items():
    print(key+'的年龄：'+str(student['age']))#第一种打印方法
    print('%s的年龄是:%s' %(key,student['age']))#第二种打印方法

def func(arg) :
    arg={}
func(students)#不会被清空 arg和students同时指向对应对象，只是arg被清空
print(students)