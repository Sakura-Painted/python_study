# 求最大值
def max(args):

    if not args:
        return None

    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value


if __name__ == "__main__":
    args = [1, 2, 3, 4, 17, 25, 29]
    print( max( args ) )
