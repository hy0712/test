import json

# json.dump()函数的使用，将json信息写进文件
json_info = "{'age':'12'}"
file = open('1.json', 'w', encoding='utf-8')
json.dump(json_info, file)