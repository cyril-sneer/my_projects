SALE_TAX = 0.07

price1 = float(input('Введите цену товара 1: '))
price2 = float(input('Введите цену товара 2: '))
price3 = float(input('Введите цену товара 3: '))
price4 = float(input('Введите цену товара 4: '))
price5 = float(input('Введите цену товара 5: '))

total_price = price1 + price2 + price3 + price4 + price5
total_tax = total_price * SALE_TAX
total_sum = total_price + total_tax

print(f'Общая стоимость покупки: {total_price:.2f}, налог: {total_tax:.2f}, всего: {total_sum:.2f} ')
