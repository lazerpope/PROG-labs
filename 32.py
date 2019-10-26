import random

list = []
listSize = 22
i = int(listSize/2)
while listSize > 0:
    list.append(random.randint(1, 100))
    listSize -= 1

print("Исходный массив:", list)

while i > 0:
    a = list[i*2-1]
    list[i*2-1] = list[i*2-2]
    list[i*2-2] = a
    i -= 1

print("Новый массив:   ", list)
