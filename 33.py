import random

list = []
listSize = 5
while listSize > 0:
    list.append(random.randint(1, 100))
    listSize -= 1

print("Исходный массив:", list)

lastValue = list[list.__len__() - 1]
for i in range(list.__len__()):
    lastValue, list[i],  = list[i], lastValue
    
print("Новый массив:   ", list)
