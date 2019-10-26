import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-10, 10))
    listSize -= 1

print("Исходный массив:", list)

num = 0
for i in range(list.__len__()):
    if list[i] > 0:
        num += 1
    elif list[i] < 0:
        num -= 1

if num < 0:
    for i in range(-num):
        list.append(random.randint(1, 10))
elif num > 0:
    for i in range(num):
        list.append(random.randint(-10, -1))

print("новый массив: ", list)
