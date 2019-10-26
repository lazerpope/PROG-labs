import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(0, 3))
    listSize -= 1

print("Исходный массив:", list)

for i in range(list.__len__()):
    if i+1 < list.__len__():
        if  list[i] == 0 and list[i+1] == 0: 
            print("Есть! ")
            break
    elif i+1 == list.__len__():
        print("нет! ")
        break
      

