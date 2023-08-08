import random

def higher_then_n(_list: list, number: float) -> list:
    return [n for n in _list if n > number]

def main():
    number_list = [random.randint(1, 100) for i in range(30)]

    number = float(input('Введите число от 1 до 100: '))
    print(f'Случайные числа: {number_list}')
    print(f'Из них больше {number}: {higher_then_n(number_list, number)}')


if __name__ == '__main__':
    main()
