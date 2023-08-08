mass = float(input('Введите массу тела в кг:\t'))
height = float(input('Введите рост в см:\t\t\t'))

height /= 100

imt = mass / (height**2)

print(f'Ваш ИМТ {imt:.1f}')

if imt > 25:
    print('Ваша масса БОЛЬШЕ нормы')
elif imt >= 18.5:
    print('Ваша масса В НОРМЕ')
else:
    print('Ваша маса МЕНЬШЕ нормы')

