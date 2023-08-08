MONTHS = ('Январь', 'Февраль', "Март", "Апрель", "Май", "Июнь",
          "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")

mm_total = 0     # общее количество осадков
years = int(input('Введите количество лет:\t'))

for y in range(years):
    for m in MONTHS:
        mm = int(input(f'Год:\t{y+1},\tМесяц:\t{m},\tВведите количество осадков:\t'))
        mm_total += mm

months_total = years * len(MONTHS)

print(f'Всего месяцев: {months_total}')
print(f'Общее количество осадков: {mm_total}')
print(f'Среднее количество осадков: {mm_total/months_total:.2f}')


