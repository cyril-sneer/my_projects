def show_payments(credit, insurance, fuel, motor, tires, service):
    monthly_payment = credit + insurance + fuel + motor + tires + service
    print(f'Ежемесячные расходы:\t{monthly_payment:.2f}')
    print(f'Ежегодные расходы:\t\t{monthly_payment * 12:.2f}')


def main():
    credit_payment = float(input('Введите затраты на кредит:\t\t\t'))
    insurance_payment = float(input('Введите затраты на страховку:\t\t'))
    fuel_payment = float(input('Введите затраты на топливо:\t\t\t'))
    motor_oil_payment = float(input('Введите затраты на моторное масло:\t'))
    tires_payment = float(input('Введите затраты на шины:\t\t\t'))
    service_payment = float(input('Введите затраты на техобслуживание:\t'))

    print()

    show_payments(credit_payment, insurance_payment, fuel_payment,
                  motor_oil_payment, tires_payment, service_payment)


main()