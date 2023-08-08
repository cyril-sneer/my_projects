mass = float(input('Введите массу пакета в граммах:\t'))

price = 0

if mass > 1000: price = 475
elif mass > 600: price = 400
elif mass > 200: price = 300
else: price = 150

cost = (mass / 100) * price

print(f'Стоимость доставки:\t{cost:.2f} грн.')