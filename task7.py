print("Введите X")
x = int(input("x: "))

if x > 0:
    y = 2*x - 10
    print(f"y = 2x – 10 = {y}")
elif x == 0:
    y = 0
    print(f"y = {y}")
else:
    y = 2*abs(x) - 1
    print(f"y = 2 * |x| – 1 = {y}")

