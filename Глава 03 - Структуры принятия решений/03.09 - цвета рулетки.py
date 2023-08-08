
while True:
    number = int(input('Введите номер кармана:\t'))
    if 0 <= number <= 36: break
    else: print('Неверный ввод, повторите')

if 1 <= number <= 10:
    if number % 2 == 0: print('black')
    else: print ('red')
elif 11 <= number <= 18:
    if number % 2 == 0: print('red')
    else: print('black')
elif 19 <= number <= 28:
    if number % 2 == 0: print('black')
    else: print ('red')
elif 29 <= number <= 36:
    if number % 2 == 0: print('red')
    else: print('black')
else: print('green')

