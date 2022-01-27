number = int(input("Введите трехзначное число: "))
LOW_LIMIT = 100
HI_LIMIT = 999

if number < LOW_LIMIT or number > HI_LIMIT:
    print("Необходимо ввести трехзначное число")
else:
    firstDigitOfNumber = number % 10
    secondDigitOfNumber = (number % 100) // 10
    thirdDigitOfNumber = number // 100
    sum = firstDigitOfNumber + secondDigitOfNumber + thirdDigitOfNumber
    print(f"{firstDigitOfNumber} + {secondDigitOfNumber} + {thirdDigitOfNumber} = {sum}")
