# -*- coding: utf-8 -*-
import os
base_path = r'D:\20200205\人脸属性信息测试\年龄图片信息搜集\100'

lst = os.listdir(base_path)
file_name = "name.txt"
path = os.path.join(base_path,file_name)

dir_list = sorted(lst,key=lambda x: os.path.getmtime(os.path.join( base_path, x)))
#print(dir_list)


if not os.path.exists(base_path):
    os.makedirs(base_path)
try:
    with open(file_name,'w',encoding="utf-8") as f:
        for dir in dir_list:
            if dir.endswith('jpg'):
                f.write(dir+'\r')
        f.close()
except Exception  as e:
    print("保存失败")


