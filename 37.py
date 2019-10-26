import random

list = []
listSize = 5
while listSize > 0:
    list.append(random.randint(-100, 100))
    listSize -= 1

print("Исходный массив:", list)

sum = 0
pos = 0
for i in range(list.__len__()):
    sum += list[i]
    if list[i]>0:
        pos+=1

list[0] = sum
list[1] = pos
print("Новый массив:   ", list)
