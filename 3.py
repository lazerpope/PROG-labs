import math

a = int(input("переменная А  "))
b = int(input("переменная B  "))
c = int(input("переменная C  "))

print("Периметр " + str(a+b+c))

p = (a+b+c)/2
print("Площадь " + str(math.sqrt(p*(p-a)*(p-b)*(p-c))))
