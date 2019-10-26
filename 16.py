import random

a = int(random.randint(1, 9999))
print("Число   " + str(a))

if a//500 > 0:
    print(str(a//500)+" по 500")

a = a % 500
if a//100 > 0:
    print(str(a//100)+" по 100")

a = a % 100
if a//10 > 0:
    print(str(a//10)+" по 10")

a = a % 10
if a//2 > 0:
    print(str(a//2)+" по 2")
