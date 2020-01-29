import json

# json.load()函数的使用，将读取json信息

file = open('1.json', 'r', encoding='utf-8')
info = json.load(file)
print(info)