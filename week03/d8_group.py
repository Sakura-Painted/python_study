# 8.按班级分组统计人数
contacts = [
    {"name": "彭于晏","class_name": "高三五班"},
    {"name": "周润发","class_name": "高三四班"},
    {"name": "樵夫","class_name": "高三三班"},
    {"name" : "李四","class_name" : "高三三班"},
    {"name" : "张三" ,"class_name" : "高三三班"}
]
clas_shuliang={}
for i in contacts:
    clas=i['class_name']
    if clas in clas_shuliang:
        clas_shuliang[clas]+=1
    else:
        clas_shuliang[clas]=1
for key,value in clas_shuliang.items():
    print(key,value)