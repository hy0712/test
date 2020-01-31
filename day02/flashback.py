#将一个数逆序放入列表中 如：1234----【4,3,2,1】

l='1234'
length =len(l)

def foo(length,lst=[]):
    if length == 0:
        return lst
    lst.append(l[length-1])
    return foo(length-1,lst)

print((foo(length)))