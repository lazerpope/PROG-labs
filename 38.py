import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(1, 100))
    listSize -= 1

m = int(input("переменная M  "))
k = int(input("переменная K  "))

print("Исходный массив:", list)

for i in range(m):
    del list[i+k]

print("Новый массив:   ", list)


