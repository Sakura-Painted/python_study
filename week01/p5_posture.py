height = int(input("请输入身高: "))
weight = int(input("请输入体重: "))
print(f"你的BMI指数是: {weight / (height / 100) ** 2}")