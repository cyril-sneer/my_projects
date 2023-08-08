numbers = []

for n in range(20):
    numbers.append(float(input(f'Please, input number {n+1} from 20: ')))

print(f'Наименьшее - {min(numbers)}')
print(f'Наибольшее - {max(numbers)}')
print(f'Сумма - {sum(numbers)}')
print(f'Ср арифмет {sum(numbers)/len(numbers)}')