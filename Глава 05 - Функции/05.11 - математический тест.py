import random

def main():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)

    if math_test(num1, num2):
        print('Ответ правильный!')
    else:
        print('Вы ошиблись!')

def math_test(n1, n2):

    print(f'{n1:>6d}')
    print('+')
    print(f'{n2:>6d}')
    print('-' * 6)

    answer = int(input('? '))

    return True if answer == n1 + n2 else False


main()