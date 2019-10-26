import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(0, 3))
    listSize -= 1

#m = int(input("переменная M  "))
#k = int(input("переменная K  "))

print("Исходный массив:", list)

i = 0
j = list.__len__()
while i < j:
    if list[i] == 0:
        del list[i]
        j-=1
    else:
        i+=1    

print("Новый массив:   ", list)


