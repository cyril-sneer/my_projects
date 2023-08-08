WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

sales = []

for day in WEEK:
    sale = float(input(f'Input sales for {day}: '))
    sales.append(sale)

_sum = 0
for val in sales:
    _sum += val

print(f'Total sales for this week is {_sum}')
