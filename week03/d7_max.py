#列表套字典存 5 个学生,找分数最高的
contacts=[
    {50:'周润发'},
    {60:'樵夫'},
    {70:'李四'},
    {80:'张三'},
    {90:'周杰伦'}
]

list=[]
for dic in contacts:

    for key , value in dic.items():
        list.append(int(key))

b = max(list)
for f in contacts:
    if b in f:
        print(f[b],'分数最高',b)