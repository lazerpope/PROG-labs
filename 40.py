import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-10, 10))
    listSize -= 1

#m = int(input("переменная M  "))
#k = int(input("переменная K  "))

print("Исходный массив:", list)

i = 0
while i < list.__len__():
    if list[i] < 0 and i != list.__len__()-1:
        list[i+1] = list[i]**2
        i+=2        
    else:
        i+=1    

print("Новый массив:   ", list)


