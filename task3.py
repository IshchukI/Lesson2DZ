x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))

if x < y:
    min = x
else:
    min = y

if z < min:
    min = z

print(f"Из числе {x}, {y}, {z} минимальное: {min}")