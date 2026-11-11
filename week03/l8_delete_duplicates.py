# 8.去掉重复元素
name = ['张三' , '李四' , '樵夫', '周润发' , '吴彦祖' , '樵夫', '周润发', '周润发']
new_name = []    #初始化新的列表，存放没有重复的元素

for new in name:
    if new not in new_name:    #如果遍历出来的元素在new_name找不到
        new_name.append(new)   #添加

print(new_name)