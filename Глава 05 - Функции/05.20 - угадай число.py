import random


def check_guess(hidden_number:int, guess_number:int)->bool:
    if guess_number > hidden_number:
        print('<---')
        return False
    elif guess_number < hidden_number:
        print('--->')
        return False
    else:
        print('ВЫ УГАДАЛИ', end=' ')
        return True


def main():
    guess = -1
    while guess != 0:
        hid_num = random.randint(1, 100)
        print('Я загадал число от 1 до 100, угадай!')
        guess = int(input('Введите число, 0 - выход:\t'))
        if guess == 0: break
        attempts_counter = 1
        while not check_guess(hid_num, guess):
            guess = int(input('Введите число, 0 - выход:\t'))
            if guess == 0: break
            attempts_counter += 1
        else: print(f'с {attempts_counter:d} попытки!\n')


main()

