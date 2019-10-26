import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-5, 5))
    listSize -= 1

print("Исходный массив:", list)

for i in range(list.__len__()):
    if list[i] == 0 and i == 1:    
        list[i] = list[0]
    elif list[i] == 0 and i > 1:
        list[i] = list[i-1]+list[i-2]

print("новый массив: ", list)
