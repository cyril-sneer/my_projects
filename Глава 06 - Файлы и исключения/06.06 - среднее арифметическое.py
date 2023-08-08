file_name = r'data\numbers.txt'

numbers_file = open(file_name, 'w')
for i in range(1,101):
    numbers_file.write(f'{str(i)}\n')
numbers_file.close()

numbers_file = open(file_name, 'r')
summa = 0
count = 0
for line in numbers_file:
    summa += int(line)
    count += 1
numbers_file.close()

print(summa/count)