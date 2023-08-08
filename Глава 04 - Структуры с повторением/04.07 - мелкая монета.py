salary = 0.01
gross_salary = 0

days = int(input('Введите количество рабочих дней:\t'))

if days != 0:

    print('Day\tSalary')
    print('-' * 15)

    for d in range(1, days+1):
        print(f'{d}\t{salary:,.2f}')
        gross_salary += salary
        salary *= 2

    print(f'\t{gross_salary:,.2f} грн.')


