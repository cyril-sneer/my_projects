fio_full = input('Введите ФИО полностью: ')

fio_sep = fio_full.split()

fio_short = ""
for name in fio_sep:
    fio_short += name[0] + '.'

print(fio_short)
