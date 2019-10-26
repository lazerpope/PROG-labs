import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-10, 10))
    listSize -= 1

print("Исходный массив:", list)
t = float(input("Число T  "))

num = 0

for i in range(list.__len__()):
    if list[i] > 0:    
        num += list[i]

for i in range(list.__len__()):
    if list[i] > 0:    
        list[i]+= t*list[i]/num

print("новый массив: ", list)
