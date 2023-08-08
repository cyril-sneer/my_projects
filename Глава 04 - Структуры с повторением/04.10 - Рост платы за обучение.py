START_PAYMENT = 145000.0
YEAR_INCREMENT = 0.03

current_payment = START_PAYMENT

print('Год\tПлата за обучение')
print('-' * 20)

for y in range(5):
    current_payment = current_payment + current_payment*YEAR_INCREMENT
    print(f'{y+1}\t{current_payment:.2f} грн.')
