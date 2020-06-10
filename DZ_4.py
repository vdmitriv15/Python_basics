# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("введите число целое число, неравное 0: "))

if number == 0:
    print("число не должно быть равно 0")
else:
    max_digit = 1
    while number > 1:
        digit = number % 10
        if digit == 9:
            max_digit = 9
            break
        elif digit > max_digit:
            max_digit = digit
        number //= 10
    print(f"{max_digit} - самая большая цифра в вашем числе")




