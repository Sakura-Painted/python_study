unit_price = int(input("请输入商品单价: "))
quantity = int(input("请输入购买数量: "))

total_amount = unit_price * quantity


if total_amount >= 100:
    discount = total_amount * 0.9
    print(f"总金额: {discount}")
    
else:
    print(f"总金额: {total_amount}")
    