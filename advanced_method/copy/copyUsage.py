
#深复制
listA = ['a','b']
listB = listA

listA.append('c')
listB.append('d')

print(listA,listB)

print(listA == listB)
print(id(listA),id(listB))

#浅复制
listC = listA[:]
listA.append('e')
print(listA == listC)
print(id(listA),id(listC))

#ß

