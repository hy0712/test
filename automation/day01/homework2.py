import json

flag = True
def go_on(no):
    if no in ('Y', 'y'):
        flag = True
    elif no in ('N', 'n'):
        flag = False
    else:
        print("您输入有误！程序结束")
        flag = False
    return flag

def zc(flag):
    if flag:
        print("=========注册=========")
        name = input("请输入您的用户名：").strip()
        passwd = input("请输入您的密码：").strip()
        passwd1 = input("请输入确认密码：")
        if not name or not passwd:
            print("用户名或密码不能为空！")
            no = input("是否需要继续注册？请输入Y或N：")
            go_on(no)
            zc(go_on(no))
        elif passwd != passwd1:
            print("密码和确认密码不一致")
            no1 = input("是否需要继续注册？请输入Y或N：")
            zc(go_on(no1))
        else:
            with open("time.txt",'a+',encoding='utf-8') as file:
                dic = {'name':name,'password':passwd}
                dic_info = json.dumps(dic)
                file.write(dic_info+'\n')
                file.close()
                no2 = input("注册成功!是否需要继续注册？请输入Y或N：")
                zc(go_on(no2))
def login(num):
    num1 = 1
    while num1 <= num:
        print("========登录=========")
        input_name = input("请输入您的用户名：")
        input_passwd = input("请输入您的密码：")
        with open('time.txt','r',encoding='utf-8') as file:
            lines = file.readlines()
            l = len(lines)
            read_num = 1
            for line in lines:
                #print("read_num%s"%read_num)
                json_info = json.loads(line) #将字符串转化为字典格式
                n = json_info['name']  #name
                p = json_info.get('password')  #pwd
                if read_num <= l:
                    if n == input_name and p == input_passwd:
                        print("登录成功")
                        return
                    else:
                        read_num = read_num+1
                        continue
            if num1 < num:
                print("您的用户名或密码输入错误，请重新输入！")
            else:
                print("您输入错误超过三次，账号已锁定")
                break
            num1 += 1
zc(True)
login(3)