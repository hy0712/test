import json
#json.dumps（）函数的使用，将字典格式转换成字符串

dict1 = {"age":"12"}
print(dict1)
print(type(dict1))
json_info = json.dumps(dict1)
print(json_info)
print(type(json_info))

#将字符串转化成字典格式
dict_info = json.loads(json_info)
print(type(dict_info))
print(dict_info)

