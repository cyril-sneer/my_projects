A_PRICE = 20
B_PRICE = 15
C_PRICE = 10

def main():
    a_quantity = int(input('Введите количество мест класса A:\t'))
    b_quantity = int(input('Введите количество мест класса B:\t'))
    c_quantity = int(input('Введите количество мест класса C:\t'))

    total_value = calc_value(a_quantity, b_quantity, c_quantity)

    print(f'Суммарный доход:\t{total_value:.2f}')


def calc_value(a, b, c):
    return a * A_PRICE + b * B_PRICE + c * C_PRICE


main()
