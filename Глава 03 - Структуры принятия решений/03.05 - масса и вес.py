mass = float(input('Введите массу тела:\t'))

weight = mass * 9.8

if weight < 100:
    print('Тело слишком легкое')
elif weight > 500:
    print('Тело слишком тяжелое')
