import random

list = []
listSize = 11
while listSize > 0:
    list.append(random.randint(-3, 10))
    listSize -= 1


print("Исходный массив:", list)
repeats = 0

for i in range(list.__len__()):
    if list[i] < 0:       
        if i == 0:
            break
        if i == 1:
            repeats = 1
            break
        j = 2
        repeats = 1
        while list[i-j] > list[i+1-j]:
                repeats += 1
                j+=1
        break    

    elif i == list.__len__()-1:
        print("Отрицательных элементов нет")
        repeats = -1


if repeats == 0:
    print("Первый элемент - отрицательный")
elif repeats == 1:
    print("Последовательность не убывает")
elif repeats>=1:
    print("Последовательность убывает на протяжении  " + str(repeats)+ " элементов ")
