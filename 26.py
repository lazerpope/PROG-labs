

x = int(input("Число X "))


if  x<=0:
    print("f("+str(x)+")="+str(0))
elif 0 < x < 1:
    print("f("+str(x)+")="+str(x))
else:
    print("f("+str(x)+")="+str(x**4))
