import os

for root,dirs,files in os.walk("d:/test/",topdown=True):
    for file in files:
        print(os.path.join(root,file))
    for dir in dirs:
        print(os.path.join(root,dir))