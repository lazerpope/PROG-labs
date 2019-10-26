
a = int(input("переменная А  "))
b = int(input("переменная B  "))
c = int(input("переменная C  "))

max = a if a > b else b

print(max) if max > c else print(c)
