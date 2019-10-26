import random
import math

list = []
listSize = 10
while listSize > 0:
    list.append(random.randint(1, 100))
    listSize -= 1

print("Исходный массив:", list)

centralPoint = math.ceil(list.__len__()/2)
for i in range(math.floor(list.__len__()/2)):
    list[i+centralPoint], list[i],  = list[i], list[i+centralPoint]
    
print("Новый массив:   ", list)
