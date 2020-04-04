# -*- coding: UTF-8 -*-

#不满足规则的会输出到第二个sheet页，需要手动处理一下；满足规则的会输出到第一个sheet页
import os
import os.path
import xlwt
import xlrd

base_path = r"D:\20200205\人脸属性信息测试\年龄图片信息搜集\100"
#print(basedir)

#  --- 创建表格 ---
getWordExcel=xlwt.Workbook()
#  --- 创建 Sheet ---
getTable1 = getWordExcel.add_sheet('getName',cell_overwrite_ok=True)

#  --- 行数 ---
index = 1
# --- 判断该表格是否存在 ---
if os.path.isfile(base_path+'/Name.xls'):
    os.remove(base_path+'/Name.xls')

lst = os.listdir(base_path)
# 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
# os.path.getmtime() 函数是获取文件最后修改时间
# os.path.getctime() 函数是获取文件最后创建时间
dir_list = sorted(lst,key=lambda x: os.path.getmtime(os.path.join(base_path, x)))
#print(dir_list)

for name in dir_list:
    #获取后缀为jpg的文件
    if name.endswith('.jpg'):
        getTable1.write(0, 0, 'ID')
        getTable1.write(0, 1, 'Name')

        # 写入表格第一列
        getTable1.write(index,0,index)
        getTable1.write(index,1,name)
        index += 1

    getWordExcel.save(base_path + '/Name.xls')