import math

a = float(input("Диаметр поперечного сечения = "))
b = int(input("Ширина квадратного бруса = "))
#c = int(input("переменная C  "))

if a >= b * math.sqrt(5):
    print("Можно")
else:
    print("Нельзя")
