start = float(input('Введите стартовое количество организмов: '))
inc = float(input('Введите ежесуточный прирост в %: '))
days = int(input('Введите количество дней наблюдения: '))

population = start

print('Day\tPopulation')
print('-' * 20)

for d in range(1, days+1):
    print(f'{d}\t{population}')
    population += population*(inc/100)