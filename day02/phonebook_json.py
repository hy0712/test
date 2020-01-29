#coding:utf-8

import json
record_list = []
record_id = 0

def input_record():
    name = input("请输入要添加的姓名：")
    phone_number = input("请输入手机号：")
    record = {"name":name,"phone_number":phone_number}
    return record

def add_record():
    record = input_record()
    global record_id
    record_id += 1
    record["record_id"] = record_id
    record_list.append(record)
    return "添加成功！"

def query_record(name):
    query_result = []
    query_ids = []
    for record in record_list:
        if record["name"] == name:
            query_ids.append(record["record_id"])
            query_result.append(record)
    return query_ids, query_result

def del_record(name):
    query_ids, query_result = query_record(name)
    if len(query_ids) == 0:
        print("要删除的姓名不存在！")
    else:
        if len(query_result)>1:
            for record in query_result:
                print("{}/{}/{}/".format(record["record_id"],record["name"],record["phone_number"]))
            record_id = input("请输入要删除的id：")
            if int(record_id) in query_ids:
                for record in query_result:
                    if int(record_id) == record["record_id"]:
                        record_list.remove(record)
            else:
                print("输入错误！")
        else:
            print("{}/{}/{}/".format(query_result[0]["record_id"],query_result[0]["name"],query_result[0]["phone_number"]))
            while True:
                s = input("是否确认删除信息(Y/N)?:")
                if s in ['Y','N','y','n']:
                    if s == 'Y' or s == 'y':
                        record_list.remove(query_result[0])
                        print("删除成功！")
                    elif s == 'N':
                        print("未删除")
                        pass
                    else:
                        print("未删除")
                        pass
                    break
                else:
                    print("输入错误！")
def change_record(name):
    query_ids, query_result = query_record(name)
    if len(query_ids) == 0:
        print("要修改的姓名不存在！")
    else:
        if len(query_result)>1:
            for record in query_result:
                print("{}/{}/{}/".format(record["record_id"],record["name"],record["phone_number"]))
            record_id = input("请输入要修改的id：")
            if int(record_id) in query_ids:
                for record in query_result:
                    if int(record_id) == record["record_id"]:
                        phone_number = input("请输入要修改的电话号码：")
                        record["phone_number"]=phone_number
                        name = input("请输入要修改的姓名：")
                        record["name"] = name
                        print("修改成功！")

            else:
                print("输入错误！")
        else:
            print("{}/{}/{}/".format(query_result[0]["record_id"], query_result[0]["name"], query_result[0]["phone_number"]))
            phone_number = input("请输入修改后的电话号码:")
            query_result[0]["phone_number"] = phone_number
            print("修改成功")

def phonebook_save(L):
        with open("./tmp/data.dat", "w") as f:
            json.dump(L, f)


#json.load()函数的使用，将读取json信息
def phonebook_load():
    global record_list
    with open("./tmp/data.dat", "r") as f:
        record_list = json.load(f)
        global record_id
        record_id = record_list[-1]["record_id"]

if __name__ == "__main__":
    try:
        phonebook_load()
    except Exception:
        print("数据文件不存在")
    while True:

        menu="""
        通讯录
        1.添加
        2.查找
        3.删除
        4.修改
        5.退出   
        """
        print(menu)
        s=input("请选择操作：")
        if s in ['1','2','3','4','5']:
            if s == '1':
                msg = add_record()
                print(msg)
            if s == '2':
                name = input("请输入要查找的姓名：")
                query_ids, query_results = query_record(name)
                if len(query_ids) == 0:
                    print("不存在")
                else:
                    for record in query_results:
                        print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            if s == '3':
                name = input("请输入要删除的姓名：")
                del_record(name)
            if s == '4':
                name = input("请输入要修改的姓名：")
                change_record(name)
            if s =="5":
                phonebook_save(record_list)
                break

        else:
            print("输入错误")
            continue
