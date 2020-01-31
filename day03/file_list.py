import os
#打印目录下的所有文件名
def listfile(dir):
    for file in os.listdir(dir):   #os.listdir()用于返回一个由文件名和目录名组成的列表
        path = os.path.join(dir,file)
        if not os.path.isdir(path):   #os.path.isdir()用于判断对象是否为一个目录
            print(path)
        else:
            listfile(path)
dir = "d:/test"
listfile(dir)

