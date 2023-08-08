TIP_RATE = 0.18         # размер чаевых - 18%
TAX_RATE = 0.07         # налог с продаж - 7%

food = float(input('Введите стоимость блюд, грн.: '))
tip = food * TIP_RATE
tax = food * TAX_RATE
total = food + tip + tax

print(f'Чаевые: {tip:.2f} грн.')
print(f'Налог с продаж: {tax:.2f} грн.')
print(f'Всего: {total:.2f} грн.')
