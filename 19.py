

a = int(input("сторона A "))
b = int(input("сторона B  "))
c = int(input("сторона C  "))

if a+b>c and a-b<c:
    if c**2 == a**2+b**2:
        print ("Существует, прямоугольный")
    else:
        print ("Существует, не прямоугольный")
else:
    print ("не существует")
