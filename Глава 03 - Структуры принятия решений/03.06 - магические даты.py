while True:
    day = int(input('Введите день:\t'))
    if 1 <= day <= 31: break
    else: print('Недопустимый ввод!')

while True:
    month = int(input('Введите месяц:\t'))
    if 1 <= month <= 12: break
    else: print('Недопустимый ввод!')

while True:
    year = int(input('Введите год:\t'))
    if 1 <= year <= 99: break
    else: print('Недопустимый ввод!')

if day * month == year:
    print('Вы ввели МАГИЧЕСКУЮ дату!!!')
else:
    print('Дата НЕ является магической!')
