import math

a = int(input("переменная A  "))
h = int(input("переменная H  "))
r = int(input("переменная R  "))
m = int(input("переменная M  "))


if m < math.pi * r**2 * h and m < a**3:
    print("Поместится обе")
elif m < a**3:
    print("Поместится в 1")
elif math.pi * r**2 * h > m:
    print("Поместится во 2")
else:
    print("не Поместится обе")
