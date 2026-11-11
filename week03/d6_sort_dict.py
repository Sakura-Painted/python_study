# 6.字典排序输出
contacts={0:'周润发',6:'樵夫',10:'李四',8:'张三'}
lise=[]

for key,value in contacts.items():
    lise.append(key)
lise.sort()

for i in lise:
    print(contacts[i])