with open('../html文件/html1.html', encoding='utf8') as f:
    html_doc = f.read()

#导入BeautifulSoup
from bs4 import BeautifulSoup

#指定用html5lib来解析html文档
soup = BeautifulSoup(html_doc,'html5lib')

#可以根据标签获取元素
print(soup.find('title')) #或者  print(soup.title)  ##得到结果<title>三兄弟的故事</title>

#含有多个相同标签时，打印第一个
print(soup.find('p'))

#获取标签内的文本内容
print(soup.div.string) #返回直接包含的文字内容，不包含子节点
print(soup.div.getText()) #返回直接包含和子节点内容
print(soup.div.getText("|")) #text前后有|

#获取父文本整体内容
print(soup.title.parent)

#获取属性值（如果有多个，获取第一个标签的）
print(soup.div['id'])  #如果第一个div有id则正常，没有则报错
print(soup.div.get('id')) #第一个div没有则返回none

#返回所有p标签的列表
print(soup.find_all('p'))

#获取第二个p标签（n个）
print(soup.find_all('p')[1])

#根据元素属性去找
print(soup.find('div',id='shui'))

# 浏览器退出
# driver.quit()