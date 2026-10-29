# 判断质数
def is_prime(num):
    # 排除负数和1
    if num <= 1:
        return False
    #num ** 0.5 是 num开根号
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 10, 25, -29]
    for n in test_nums:
        if is_prime(n):
            print(f"{n} 是质数")
        else:
            print(f"{n} 不是质数")