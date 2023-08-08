import random

def main():
    numbers_quantity = int(input('Введите количество чисел:\t'))

    outfile = open(r'data\random_numbers.txt', 'w')

    for c in range(numbers_quantity):
        num = random.randint(1, 500)
        outfile.write(f'{num}\n')

    outfile.close()


if __name__ == '__main__':
    main()