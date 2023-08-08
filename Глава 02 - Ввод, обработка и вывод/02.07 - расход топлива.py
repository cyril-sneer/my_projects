kms = float(input('Введите количество пройденных километров: '))
litres = float(input('Введите количество литров топлива: '))

litres_per_100km = litres / kms * 100
km_per_liter = kms / litres

print(f'Ваш расход {litres_per_100km:.2f} л/100 км, вы проехали {km_per_liter:.2f} км на 1 л топлива.')
