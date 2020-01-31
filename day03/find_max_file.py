import os
# 寻找目录下最大的文件并输出其文件名和文件大小

max_size = 0
path_dir = "d:/test/"
for root,dirs,files in os.walk(path_dir,topdown=True):
    for file in files:
        path = os.path.join(root,file)
        file_size = os.path.getsize(path)
        # print(path,file_size)
        if file_size > max_size:
            max_size = file_size
            max_file = path
            print(max_file,max_size)

print(max_file,max_size)

