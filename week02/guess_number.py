import random
#number 1~100随机的数字
number = random.randint(1, 100)

#初始化猜的次数
time = 0


#用while 循环进行循环判断
while True:
    #计数猜的次数
    time += 1

    #输入用户猜的数字
    guess = int(input("请输入1~100的数字："))

    #进行猜7次后输出正确答案的判断
    if time == 7:
        print (f"正确答案是{number}")

    #进行大小判断
    elif guess == number:
        print (f"恭喜猜中,你用了{time}次")
    elif guess > number:
        print ("太大了")
    elif guess < number:
        print ("太小了")