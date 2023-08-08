YELLOW = 'yellow'
RED = 'red'
BLUE = 'blue'

COLORS = (RED, BLUE, YELLOW)

while True:

    while True:
        color_1 = input('Введите ПЕРВЫЙ цвет:\t')
        if color_1 in COLORS: break
        else: print('Недопустимый ввод')

    while True:
        color_2 = input('Введите ВТОРОЙ цвет:\t')
        if color_2 in COLORS: break
        else: print('Недопустимый ввод')

    if color_1 != color_2: break
    else: print('Вы ввели два одинаковых цвета!')

if (color_1 == RED and color_2 == BLUE) or (color_1 == BLUE and color_2 == RED):
    print('Вы получите ФИОЛЕТОВЫЙ цвет')
elif (color_1 == RED and color_2 == YELLOW) or (color_1 == YELLOW and color_2 == RED):
    print('Вы получите ОРАНЖЕВЫЙ цвет')
elif (color_1 == BLUE and color_2 == YELLOW) or (color_1 == YELLOW and color_2 == BLUE):
    print('Вы получите ЗЕЛЕНЫЙ цвет')
else: print('Something goes wrong!')
