filename = input(f'Введите имя файла:\t')
infile = open(filename, 'r')

str_number = 1
for line in infile:
    print(f'{str_number}:\t{line.rstrip()}')
    str_number += 1

infile.close()