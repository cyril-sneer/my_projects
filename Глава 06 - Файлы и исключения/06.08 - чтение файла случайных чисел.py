def main():
    infile = open(r'data\random_numbers.txt', 'r')

    numbers_quantity = 0
    numbers_sum = 0

    for line in infile:
        numbers_sum += int(line)
        numbers_quantity += 1

    print(f'Было считано {numbers_quantity} чисел. \nСумма равна {numbers_sum}')

if __name__ == '__main__':
    main()
