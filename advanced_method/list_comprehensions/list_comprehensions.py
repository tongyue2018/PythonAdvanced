# @Time : 2020/3/30 19:24 
# @Author : tongyue



############### 案例1 ###################
a = 1
b = a if not a else None
print(b) # 结果是None

############### 案例2 ###################

books =[
    {
        "name":"kongzi",
        "publisher":"beijing"
    },
    {
        "name":"mengzi",
        "publisher":"shanghai"
    }
]

def updateData(book):
    book['name'] = book['name']+"_new"
    book['publisher'] += "_new"
    return book
#列表推导式 [updateData(book) for book in books if book.xx==xx]
books2 = [updateData(book) for book in books] #批量处理 生成新的list 这里的book可以写成函数
print(books2)
