
x = int(input("Число X "))

if x%4 == 0:
    print("Високосный год")
else:
    print("Невисокосный год")

print("Век  " + str(x//100+1))
