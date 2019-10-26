import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-10, 10))
    listSize -= 1

print("Исходный массив:", list)

lPos = []
lNeg = []

for i in range(list.__len__()):
    if list[i] > 0:
        lPos.append(list[i])
    elif list[i] < 0:
        lNeg.append(list[i])


print("новый массив 1:", lPos)
print("новый массив 2:", lNeg)