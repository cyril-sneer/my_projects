def calc_deposit(start_sum, month_rate, month_quantity):
    return start_sum * (1 + month_rate) ** month_quantity


def main():
    deposit_start_sum = float(input('Введите первоначальную сумму депозита, грн.:\t'))
    deposit_month_rate = float(input('Введите ежемесячную процентную ставку, %:\t'))
    deposit_month_rate /= 100
    deposit_month_quantity = int(input('Введите количество месяцев:\t'))

    deposit_end_sum = calc_deposit(deposit_start_sum, deposit_month_rate, deposit_month_quantity)

    print(f'Через {deposit_month_quantity} месяцев на вашем счету будет {deposit_end_sum:.2f} грн.')

main()