# 密码错 3 次锁定
password = "123"
attempts = 0

while attempts < 3:
    pwd = input("请输入密码: ")
    if pwd == password:
        print("密码正确")
        break
    else:
        attempts += 1
        print("密码错误")
else:
    print("密码错误3次，已锁定！")