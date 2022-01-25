n = float(input("Введите скорость автомобиля: "))
m = float(input("Введите длинну маршрута: "))

if n <= 0:
    print("Скорость должна быть больше 0")
elif m <= 0:
    print("Длина маршрута должна быть больше 0")
else:
    days = m / n
    hours = round((m / n - m // n) * 24, 2)
    print(f"На маршрута длинной {m} км при скорости автомобиля {n} км/ч необходимо {int(days)} дней и {hours} часов")





