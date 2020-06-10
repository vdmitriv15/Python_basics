# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("введите время в секундах: "))

if time <= 0:
    print("введите число больше 0")
else:
    hours = time // 3600
    if hours < 10:
        hours = str(hours)
        hours = '0' + hours

    minutes = time % 3600 // 60
    if minutes < 10:
        minutes = str(minutes)
        minutes = '0' + minutes

    seconds = time % 3600 % 60
    if seconds < 10:
        seconds = str(seconds)
        seconds = '0' + seconds

    print(f"ответ: {hours}:{minutes}:{seconds}")


