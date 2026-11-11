# 2.统计一段字符串里每个字出现的次数
time_string = {}
string_at = input("请输入字符串 ：")

for i in string_at :
    if i in time_string:
        time_string[i] += 1

    else:
        time_string[i] = 1

print (time_string)