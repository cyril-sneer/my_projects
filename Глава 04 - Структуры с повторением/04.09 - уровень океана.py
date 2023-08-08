YEAR_INC = 1.6
rise = 0

for y in range(25):
    rise += YEAR_INC
    print(f'Год: {y + 1}\t{(y + 1) * YEAR_INC:.2f} мм')
    #print(y+1, ' ', rise)

