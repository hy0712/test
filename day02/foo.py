'''
 2 
 3 问题简述：一只小猴子吃桃子的问题。
 4 话说，一只小猴子第一天摘下若干个桃子，并吃了一半。
 5 感觉到吃的还不瘾，于是又多吃了一个；
 6 第二天早上，又将剩下的桃子吃掉一半，又多吃了一个。
 7 以后每天早上,都吃了前一天剩下的一半零一个。
 8 python问题：
 9 请问，到了第10天早上想再吃时，却发现只剩下一个桃子了。
10 求第一天共摘了多少？
11 
12 # 逆向思维
13 s2 = 1
14 for day in range(9,0,-1):
15     s1 = (s2 + 1)*2
16     s2 = s1
17 print(s1)
18 '''
# no 1
def foo(n=10, a=1): # n = 10 是因为 当n = 2的时候已经是答案了，但是此时的 获取不到a 要等 n==1 的时候去获取a
    if n == 1:
         return a
    a = (a + 1) * 2
    return  foo(n-1, a)

print((foo(10))) # 1534

# no 2    n只是一个循环条件
def foo(n=10):
    if n == 1:
        return 1
    return (foo(n-1) + 1) * 2

print(foo())

def foo(n=1):
     if n == 10:
         return 1
         return (foo(n+1) + 1) * 2

print(foo())