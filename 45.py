import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-10, 10))
    listSize -= 1


print("Исходный массив:", list)

num = 0
for i in range(list.__len__()):
    num += list[i]

if num != 0:
    list.append(-num)

print("новый массив: ", list)
