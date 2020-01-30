"""
练习：取出n层嵌套列表里的所有元素
提示 判断一个元素i是否是list 使用isinstance(i,list)函数
[1,2,3,[4,5,6]]
"""
def nest_list(L):
    for i in L:
        if  isinstance(i,list):
            nest_list(i)
        else:
            print(i)
if __name__ == "__main__":
    l = [1,2,3,[4,5,6]]
    nest_list(l)

