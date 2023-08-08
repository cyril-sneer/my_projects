summa = 0
number = 0

while number >= 0:
    summa += number
    number = float(input('Введите положительное число: '))


print(f'Сумма введенных чисел {summa:.2f}')