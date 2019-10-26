import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-10, 10))
    listSize -= 1

print("Исходный массив:", list)
b = float(input("Число B  "))
c = float(input("Число C  "))

i =0
while i < list.__len__():
    if b>list[i] > c or b<list[i] < c:    
        del list[i]
        i-=1
    i+=1

print("новый массив: ", list)
