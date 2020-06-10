# калькулятор отрабатывающий сложение, вычитание, умножение и деление

number_1 = int(input("веедите число: "))
number_2 = int(input("веедите второе число: "))
action = input('действие ("+", "-", "*", "/"): ')
if action == "+":
    result = number_1 + number_2
elif action == "-":
    result = number_1 - number_2
elif action == "*":
    result = number_1 * number_2
elif action == "/" and number_2 != 0:
    result = number_1 / number_2
elif action == "/" and number_2 == 0:
    print("Ошибка! Попытка деления на 0")
else:
    print("Ошибка! Некоретное действие.")



