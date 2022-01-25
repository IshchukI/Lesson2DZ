year= int(input("введите год: "))

if year < 0:
    print("введите год больше 0")
else:
    if year % 4 == 0:
        print(f"{year} - высокосный год")
    else:
        print(f"{year} - не высокосный год")
