contacts = [
    {"name": "彭于晏","telephone": "66666666666","class_name": "高三五班"},
    {"name": "周润发","telephone": "55555555555","class_name": "高三四班"},
    {"name": "樵夫","telephone": "88888888888","class_name": "高三三班"},
    {"name" : "李四" ,"telephone" : "11111111111","class_name" : "高三二班"},
    {"name" : "张三" ,"telephone" : "77777777777","class_name" : "高三一班"}
]

def menu():
    # 显示控制台菜单
    print ("\n1. 显示全部")
    print ("2. 按姓名查询")
    print ("3. 新增")
    print ("4. 退出\n")

def main():
    while True:
        menu()
        choice = int (input("请输入功能序号(1-4): ").strip())

        if choice == 1:
            # 1 显示全部
            print ("\n 功能1 显示全部功能 所有同学信息 ")
            if len(contacts) == 0:    #排除列表为空的概率
                print ("通讯录为空")
            else:
                for student in contacts:    #循环打印所以信息
                    print (f"姓名: {student['name']}, 电话: {student['telephone']}, 班级: {student['class_name']}")

        elif choice == 2:
            # 2 按姓名查询功能
            print ("\n功能2 按姓名查询功能")
            search_name = input ("请输入要查询的姓名: ").strip()
            for student in contacts:
                if student["name"] == search_name:     #寻找
                    print (f"姓名: {student['name']}, 电话: {student['telephone']}, 班级: {student['class_name']}")
                    break  # 找到了就跳出循环，此时不会执行 else 里的代码
            else:
                print ("查无此人")

        elif choice == 3:
            # 3 新增功能
            print ("\n 功能3 新增功能 ")
            new_name = input ("请输入姓名: ").strip()
            new_telephone = input ("请输入电话: ").strip()
            new_class = input ("请输入班级: ").strip()

            # 创建新字典
            new_student = {
                "name": new_name,
                "telephone": new_telephone,
                "class_name": new_class
            }
            contacts.append(new_student)          #追加到列表中
            print(f"新增成功 已添加同学：{new_name}")

        elif choice == 4:
            # 4 退出功能
            print ("\n 退出成功 ")
            break     #跳出循环
        else:
            # 处理不是1~4的整数
            print ("\n请输入 1~4 之间的整数字")


if __name__ == "__main__":
    main()