# costs = {'food':0, 'cloth':0, 'transport':0, 'house':0}
# costs = dict([('food', 0), ('cloth', 0), ('transport', 0), ('house', 0)])
costs = dict(food = 0, cloth = 0, transport = 0, house = 0)

budget = float(input('Введите месячный бюджет:\t'))
total = 0
spent = 1

for c in costs:
    costs[c] = float(input(f'Input you expenses for {c}: '))
    total += costs[c]

# while spent != 0:
#     spent = float(input('Input you expenses : '))
#     total += spent



# print(costs)
print(f'Ваши суммарные затраты составили: {total:.2f} грн.')

if total > budget:
    print(f'Вы превысили бюджет на {total - budget} грн.')
else:
    print('Бюджет не превышен')