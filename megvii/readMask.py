# -*- coding: UTF-8 -*-

#不满足规则的会输出到第二个sheet页，需要手动处理一下；满足规则的会输出到第一个sheet页
import os
import os.path
import xlwt
import xlrd

basedir = r"D:\20200205\20200225\C4S-222-X12定焦筒机\人脸属性\mask1\face"
#print(basedir)

#  --- 创建表格 ---
getWordExcel=xlwt.Workbook()
#  --- 创建 Sheet ---
getTable1 = getWordExcel.add_sheet('getMask1',cell_overwrite_ok=True)
getTable2 = getWordExcel.add_sheet('getMask2',cell_overwrite_ok=True)

#  --- 行数 ---
index = 1
index2 = 0
# --- 判断该表格是否存在 ---
if os.path.isfile(basedir+'/Mask.xls'):
    os.remove(basedir+'/Mask.xls')



for root, dirs, files in os.walk(basedir, topdown=False):
    for name in files:
        # #打印列表中每一个文件名
        totalFilePath = os.path.join(root,name)
        #获取后缀为jpg的文件
        if name.endswith('.jpg') and ("口罩" in name):
            getTable1.write(0, 0, 'ID')
            getTable1.write(0, 1, 'FaceId')
            getTable1.write(0, 2, '口罩')
            tmp = name.split("_")
            FaceId = tmp[3]  #id

            if "口罩" in tmp[6]:
                mask = tmp[6][3:]   #口罩


            # 写入表格第一列
            getTable1.write(index,0,index)
            getTable1.write(index,1,FaceId)
            getTable1.write(index,2,mask)
            index += 1


        else:
            # print(name)
            getTable2.write(index2,0,index2+1)
            getTable2.write(index2,1,name)
            index2 += 1
        getWordExcel.save(basedir + '/Mask.xls')