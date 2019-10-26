import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-10, 10))
    listSize -= 1


print("Исходный массив:", list)
repeats = 0

div3 = 0
sum = []
num = 0

for i in range(list.__len__()):
    if list[i] % 3 == 0:
        div3+=1
    if list[i] % 2 == 0:
        sum.append(list[i])

for i in range(sum.__len__()):
    num+=sum[i]

list.append(div3)

lastValue = list[list.__len__() - 1]
for i in range(list.__len__()):
    lastValue, list[i],  = list[i], lastValue

list.append(num /sum.__len__())

print("новый массив    ", list)
