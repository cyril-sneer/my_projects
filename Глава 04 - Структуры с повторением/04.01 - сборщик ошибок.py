errors = 0
for i in range(5):
    errors_today = int(input(f'День {i+1:d}, введите количество ошибок: '))
    errors += errors_today

print(f'Общее количество ошибок: {errors:d}')
