FEDERAL_TAX_RATE = 0.05
REGIONAL_TAX_RATE = 0.025

purchase = float(input('Введите величину покупки: '))

federal_tax = purchase * FEDERAL_TAX_RATE
regional_tax = purchase * REGIONAL_TAX_RATE
total_sum = purchase + federal_tax + regional_tax

print(f'Сумма покупки: \t\t\t{purchase:.2f}')
print(f'Федеральный налог: \t\t{federal_tax:.2f}')
print(f'Региональный налог: \t{regional_tax:.2f}')
print(f'Общий налог: \t\t\t{federal_tax + regional_tax:.2f}')
print(f'Итоговая сумма: \t\t{total_sum:.2f}')
