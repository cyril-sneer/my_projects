ridge_length = float(input('Введите длину гряды в метрах: '))
pillar_space = float(input('Введите пространство, занимаемое концевой опорой в метрах: '))
vines_distance = float(input('Введите расстояние между виноградными лозами в метрах: '))

vines_quantity = int((ridge_length - 2 * pillar_space) // vines_distance)

print(f'У вас достаточно места для {vines_quantity:d} виноградных лоз')
