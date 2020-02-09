# -*- coding: UTF-8 -*-

#不满足规则的会输出到第二个sheet页，需要手动处理一下；满足规则的会输出到第一个sheet页
import os
import os.path
import xlwt
import xlrd

basedir = r"C:\Users\46114\Desktop\hat"
#print(basedir)

#  --- 创建表格 ---
getWordExcel=xlwt.Workbook()
#  --- 创建 Sheet ---
getTable1 = getWordExcel.add_sheet('getword',cell_overwrite_ok=True)
getTable2 = getWordExcel.add_sheet('getword2',cell_overwrite_ok=True)

#  --- 行数 ---
index = 1
index2 = 0
# --- 判断该表格是否存在 ---
if os.path.isfile(basedir+'/WordXls.xls'):
    os.remove(basedir+'/WordXls.xls')



for root, dirs, files in os.walk(basedir, topdown=False):
    for name in files:
        # #打印列表中每一个文件名
        totalFilePath = os.path.join(root,name)
        #获取后缀为jpg的文件
        if name.endswith('.jpg') and ("帽子" in name):
            getTable1.write(0, 0, 'ID')
            getTable1.write(0, 1, 'FaceId')
            getTable1.write(0, 2, '帽子')
            tmp = name.split("_")
            FaceId = tmp[3]  #id

            if "帽子" in tmp[9]:
                hat = tmp[9][3:]   #帽子


            # 写入表格第一列
            getTable1.write(index,0,index)
            getTable1.write(index,1,FaceId)
            getTable1.write(index,2,hat)
            index += 1


        else:
            # print(name)
            getTable2.write(index2,0,index2+1)
            getTable2.write(index2,1,name)
            index2 += 1
        getWordExcel.save(basedir + '/WordXls.xls')