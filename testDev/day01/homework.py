import xlwt
import xlrd
import xlsxwriter
import os
import os.path
menu ="""
    通讯录
            1. 添加
            2. 查找
            3. 删除
            4. 修改
            5. 退出
    """
print(menu)


basedir =r"D:\test\testDev\day01"
# --- 判断该表格是否存在 ---
# if os.path.isfile(basedir+'/WordXls.xls'):
#     os.remove(basedir+'/WordXls.xls')

xls = xlsxwriter.Workbook(basedir+'./addrBook.xls')
sht1 = xls.add_worksheet('a')
    # 添加字段
sht1.write(0, 0, '序号')
sht1.write(0, 1, '姓名')
sht1.write(0, 2, '手机号')
index = 0 #行数

while True:
    operate = input("请输入操作:")

    def add():
        name = input("请输入姓名：")
        phone = input("请输入电话：")
        with open('addrBook.xls', 'a+', encoding='utf-8') as file:
        #写入数据
            global index
            sht1.write(index,0,index)
            sht1.write(index,1,name)
            sht1.write(index,2,phone)
            index = index + 1
            xls.close()
    def find():
        f_name = input("请输入要查找的姓名：")
        #打开文件
        workbook =xlrd.open_workbook("addrBook.xls")
        #获取sheet内容
        allSheetNames = workbook.sheet_names();
        # print(allSheetNames)
        for sheetName in allSheetNames:
            if sheetName == 'a':
                sheet_Content = workbook.sheet_by_name(sheetName)
            # sheet的名称，行数，列数
                print(sheet_Content.name,sheet_Content.nrows,sheet_Content.ncols);
                nrows = sheet_Content.nrows
                ncols = sheet_Content.ncols
                row = 0
            # 4. 获取整行和整列的值（数组）
                while True:
                    if  row < nrows:
                        print(sheet_Content.row_values(row)) #获取每一行的内容
                        row += 1
                    else:
                        return False
                # for col in ncols:
                #     print(sheet_Content.col_values(col)) #获取每一列的内容
    def delt():
        pass
    def modify():
        pass

    if operate == '1':
        add()
    elif operate == '2':
        find()
    elif operate == '3':
        delt()
    elif operate == '4':
        modify()
    elif operate == '5':
        break
    else:
        print("输入错误，程序退出")
        break

    #flag = False


if __name__ == '__main__':
    #addrBook()
    pass
