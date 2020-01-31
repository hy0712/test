import os
# 寻找目录下最小的文件并输入文件名和其大小

min_size = 1
path_dir = "d:/test/"

for root,dirs,files in os.walk(path_dir,topdown=True):
    for  file in files:
        path = os.path.join(root,file)
        file_size = os.path.getsize(path)
        if file_size < min_size:
            min_size = file_size
            min_file = path
print(min_file,min_size)