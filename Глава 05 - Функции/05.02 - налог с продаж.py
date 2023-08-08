FEDERAL_TAX_RATE = 0.05
REGIONAL_TAX_RATE = 0.025

def federal_tax_func(p):
    return p * FEDERAL_TAX_RATE

def regional_tax_func(p):
    return p * REGIONAL_TAX_RATE

def main():
    purchase = float(input('Введите величину покупки: '))

    federal_tax = federal_tax_func(purchase)
    regional_tax = regional_tax_func(purchase)
    total_sum = purchase + federal_tax + regional_tax

    print(f'Сумма покупки: \t\t\t{purchase:.2f}')
    print(f'Федеральный налог: \t\t{federal_tax:.2f}')
    print(f'Региональный налог: \t{regional_tax:.2f}')
    print(f'Общий налог: \t\t\t{federal_tax + regional_tax:.2f}')
    print(f'Итоговая сумма: \t\t{total_sum:.2f}')

if __name__ == '__main__': main()