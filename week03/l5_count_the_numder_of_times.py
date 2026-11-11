# 5.统计某名字出现次数
name = ['张三' , '李四' , '樵夫', '周润发' , '吴彦祖' , '樵夫', '周润发', '周润发']
time = 0
query_name = input("请输入要查询的名字 : ")
for query in name:
    if query == query_name:
        time += 1

print(f"{query_name}出现了{time}次")