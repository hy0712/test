s = '中国'
print(s.encode('utf-8'))
# b'\xe4\xb8\xad\xe5\x9b\xbd'

#对参数（key=value）编码
from urllib.parse import urlencode
data = {
    'kw' : '中国'
}
print(urlencode(data))
# kw=%E4%B8%AD%E5%9B%BD

#对字符进行编码
from urllib.parse import quote
print(quote('中国'))
# %E4%B8%AD%E5%9B%BD

