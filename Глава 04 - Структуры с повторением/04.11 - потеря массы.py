MASS_DECREMENT = 1.5

weight = float(input(('Введите свой вес: ')))

for m in range(6):
    weight -= MASS_DECREMENT
    print(f'Через {m+1} месяцев ваш вес составит: {weight:.2f} кг')