INSURANCE_PERCENT = 0.8


def calculate_insurance(value):
    return value * INSURANCE_PERCENT


def main():
    value = float(input('Введите стоимость имущества, $:\t'))
    print(f'Стоимость страховки:\t\t${calculate_insurance(value):.2f}')


main()
