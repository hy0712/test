#coding:utf-8
import json
# json.loads函数的使用，将字符串转化为字典
json_info = '{"age":"12"}'
print("json_info的类型"+str(type(json_info)))
print("json_info内容为："+json_info)

#使用json.loads()函数将字符串格式转化成字典格式
print("通过json.loads()函数处理后：")
dict_info = json.loads(json_info)
print("dict_info的类型"+str(type(dict_info)))
print("dict_info内容为："+str(dict_info))