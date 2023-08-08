ASSESSED_VALUE_PERCENT = 0.6
PROPERTY_TAX_RATE = 0.75 / 100

def main():
    fact_value = float(input('Введите фактическую стоимость имущества:\t'))
    calc_and_show_tax(fact_value)


def calc_and_show_tax(value):
    assessed_value = value * ASSESSED_VALUE_PERCENT
    property_tax = assessed_value * PROPERTY_TAX_RATE

    print(f'Оценочная стоимость:\t{assessed_value:,.2f}')
    print(f'Налог на недвижимость:\t{property_tax:.2f}')


main()