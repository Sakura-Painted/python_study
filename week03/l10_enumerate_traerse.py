# 10.用 enumerate 输出"1. 张三"这样的编号列表
names = ['张三' , '李四' , '樵夫', '周润发' , '吴彦祖' , '樵夫', '周润发', '周润发']
start = 1    #初始化
# 使用 enumerate 遍历，并设置 start=1 让序号从 1 开始
for index, name in enumerate(names, start):
    print(f"{index}. {name}")