'''
用while循环实现：
用户登录需求：
1.输入用户名和密码；
2.判断用户名和密码是否正确（name='wusir',passwd='admin123'）
3.登录仅有三次机会，超过3次会报错
'''

name = 'wusir'
passwd = 'admin123'

num = 1
while num <=3:
    input_name = input("请输入您的用户名：")
    input_passwd = input("请输入您的密码：")
    if input_name == name and input_passwd == passwd:
        print("登录成功")
        break
    elif input_name != name or input_passwd != passwd:
        if num < 3:
            print("您的用户名或密码输入错误，请重新输入！")
        else:
            print("您的输入错误超过三次，账号已锁定")
            break
        num = num +1
    else:
        pass










