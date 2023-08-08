while True:
    leap = False
    year = int(input('Введите год:\t'))
    if year == 0: break

    if year % 400 == 0: leap = True
    elif year % 100 == 0: leap = False
    elif year % 4 == 0: leap = True
    else: leap = False

    if leap: print('Введенный вами год високосный, в феарале 29 дней')
    else: print('Введенный вами год НЕ високосный, в феарале 28 дней')