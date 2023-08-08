PAINT_CONSUMPTION_RATE = 5/10   # расход краски
TIME_CONSUMPTION_RATE = 8/10    # расход времени
LITERS_IN_JAR = 5               # емкость банки
HOURLY_COST = 2000              # стоимость часа работы

def main():
    wall_square = float(input('Введите площадь стен:\t\t'))
    paint_price = float(input('Введите цены банки краски:\t'))

    make_calculation(wall_square, paint_price)


def make_calculation(square, price):
    # требуется литров краски
    paint_needed = square * PAINT_CONSUMPTION_RATE
    print(f'Требуется краски:\t{paint_needed:.1f} литров')

    # требуется времени
    time_needed = square * TIME_CONSUMPTION_RATE
    print(f'Требуется времени:\t{time_needed:.1f} часов')

    # стоимость краски
    paint_cost = paint_needed / LITERS_IN_JAR * price
    print(f'Стоимость краски:\t{paint_cost:.2f} грн')

    # стоимость работы
    work_cost = time_needed * HOURLY_COST
    print(f'Стоимость работы:\t{work_cost:.2f} грн')

    # общая стоимость
    total_cost = paint_cost + work_cost
    print(f'Общая стоимость:\t{total_cost:.2f} грн')


main()