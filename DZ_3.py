# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn

n = input("введите положительное число: ")
if int(n) <= 0:
    print("число должно быть положительным")
else:
    nn = n + n
    nnn = n + n + n
    sum = int(n) + int(nn) + int(nnn)
    print(f"результат {sum}")