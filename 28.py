
if int(input("Число A 1- true / 0 - false ")) == 0:
    a = bool("")
else:
    a = bool("1")

if int(input("Число B 1- true / 0 - false ")) == 0:
    b = bool("")
else:
    b = bool("1")

print("True") if a and b else print("false")
print("True") if a or b else print("false")
