num = int(input("请输入一个三位数:"))
print(f"百位数是: {num // 100}\n十位数是: {(num // 10) % 10}\n个位数是: {num % 10}")