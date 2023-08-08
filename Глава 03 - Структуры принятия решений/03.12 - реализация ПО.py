PRICE = 99

while True:
    copies = int(input('Введите количество копий:\t'))
    if copies >= 0: break
    else: print('Неверный ввод')

if copies > 99 : discount = 0.40
elif copies > 49: discount = 0.30
elif copies > 19: discount = 0.20
elif copies > 9: discount = 0.10
else: discount = 0.00

full_price = copies * PRICE
discount_price = full_price * discount
total = full_price - discount_price


print(f'Ваша скидка:\t\t{discount:.0%}')
print(f'Сумма скидки:\t\t${discount_price:.2f}')
print(f'Итоговая стоимость:\t${total:.2f}')