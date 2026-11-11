# 2.末尾加一个人、删掉某个人
classmates = ['张三' , '李四' , '周润发' , '吴彦祖' , '樵夫']
#获取信息
delted_person = input ("请输入要删除人的姓名 : ")
new_person = input ("请输入要添加人的姓名 : ")

classmates.remove(delted_person)    #删除
classmates.append(new_person)       #添加

print (classmates)                    #验证