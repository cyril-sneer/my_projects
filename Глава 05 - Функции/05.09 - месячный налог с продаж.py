FEDERAL_TAX_RATE = 0.05
LOCAL_TAX_RATE = 0.025


def main():
     sales = float(input('Введите общий объем продаж:\t'))
     calculate_taxes(sales)


def calculate_taxes(value):
    # рассчитать и показать федеральный налог
    federal_tax = value * FEDERAL_TAX_RATE
    print(f'Федеральный налог:\t{federal_tax:.2f}')

    # рассчитать и показать региональный налог
    local_tax = value * LOCAL_TAX_RATE
    print(f'Региональный налог:\t{local_tax:.2f}')

    # рассчитать и показать общий налог
    total_tax = federal_tax + local_tax
    print(f'Общий налог:\t\t{total_tax:.2f}')


if __name__ == '__main__':
    main()