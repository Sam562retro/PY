def checkneon(x):
    sq = x * x
    sum_digits = 0
    while sq != 0:
        sum_digits = (sum_digits + sq) % 10
        sq = sq // 10
    if x == sum_digits:
        print(str(x) + " is neon")
    else:
        print(str(x) + " is not neon")


a = int(input("enter the number you want to check is neon "))
checkneon(a)
