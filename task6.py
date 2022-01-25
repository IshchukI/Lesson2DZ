print("Введите коэфициенты квадратного уравнения")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

discrim = b ** 2 - 4 * a * c

if discrim > 0:
    x1 = (-b + discrim ** 0.5) / (2 * a)
    x2 = (-b - discrim ** 0.5) / (2 * a)
    print(f"{a}*x2 + {b}*x + {c} = 0")
    print(f"x1 = {x1}\nx2 = {x2}")
elif discrim == 0:
    x1 = (-b + discrim ** 0.5) / (2 * a)
    print(f"{a}*x2 + {b}*x + {c} = 0")
    print(f"x1 = x2 ={x1}")
else:
    print(f"Квадратное уравнение {a}*x2 + {b}*x + {c} = 0  не имеет действительных решений")
