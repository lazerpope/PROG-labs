

a = int(input("Сторона А  "))
b = int(input("Сторона B "))
c = int(input("Сторона C "))
m = int(input("Сторона M "))
k = int(input("Сторона K "))

if a*b <= m*k:
    print("Пройдет")
elif c*b <= m*k:
    print("Пройдет")
elif a*c <= m*k:
    print("Пройдет")

else:
    print("не пройдет")
