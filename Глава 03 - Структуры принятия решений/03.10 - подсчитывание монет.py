coin5 = int(input('Введите кол-во монет 5 копеек:\t'))
coin10 = int(input('Введите кол-во монет 10 копеек:\t'))
coin50 = int(input('Введите кол-во монет 50 копеек:\t'))

summa = coin5 * 5 + coin10 * 10 + coin50 * 50

if summa < 100: print('Сумма меньше 1 грн')
elif summa > 100: print('Сумма больше 1 грн')
else: print('Поздравляю! Сумма = 1 грн!')