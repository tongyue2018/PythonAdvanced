# @Time : 2021/1/17 下午6:28 
# @Author : tongyue

from urllib import parse


urlPre = 'https://www.baidu.com'
url_a = '/abc/efg?parm=hij'
url_b = '//abc'
url_c = 'abc'
url_d = 'https://www.sina.com'



url_a_all = parse.urljoin(urlPre,url_a)
url_b_all = parse.urljoin(urlPre,url_b)
url_c_all = parse.urljoin(urlPre,url_c)
url_d_all = parse.urljoin(urlPre,url_d)

print('url_a如果不包含https://，则补充域名前缀-----'+url_a_all)
print('url_b如果不包含https，包含//，则补充域名前缀-----'+url_b_all)
print('url_c如果不包含前缀，则补充域名前缀-----'+url_c_all)
print('url_d如果包含https://，则不添加前缀，维持原样-----'+url_d_all)