import math

a = int(input("сторона X "))
b = int(input("сторона Y  "))

if a>b:
    print (math.sqrt(a*b))    
else:
    print (math.log(a+b))
