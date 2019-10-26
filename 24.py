

a = int(input("сторона A "))
b = int(input("сторона B  "))
c = int(input("сторона C  "))
d = int(input("сторона D  "))

if (a <= c and b <= d) or (a <= d and b <= c):
    print("Прямоугольник AB поместится в прямоугольник CD")
else:    
    print("Прямоугольник AB не поместится в прямоугольник CD")