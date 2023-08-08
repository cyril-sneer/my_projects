import random

STONE = 'камень'
SCISSORS = 'ножницы'
PAPER = 'бумага'
GAME = {1:STONE, 2:SCISSORS, 3:PAPER}
COMP_WINS = 'Компьютер выиграл!'
USER_WINS = 'Вы выиграли!'
DRAW = 'Ничья!'

def make_choice()->int:
    right_choices = (0, *GAME.keys())

    while True:
        for key, val in GAME.items():
            print(f'{val}\t-\t{key}')
        choice = int(input('СДЕЛАЙТЕ ВАШ ВЫБОР (0 - выход):\t'))

        if choice not in right_choices: print('Некорректный ввод, повторите')
        else: return choice


def game_func(comp:int, user:int)->str:
    if GAME[comp] == STONE:
        if GAME[user] == STONE: return DRAW
        if GAME[user] == SCISSORS: return COMP_WINS
        if GAME[user] == PAPER: return USER_WINS
    if GAME[comp] == SCISSORS:
        if GAME[user] == STONE: return USER_WINS
        if GAME[user] == SCISSORS: return DRAW
        if GAME[user] == PAPER: return COMP_WINS
    if GAME[comp] == PAPER:
        if GAME[user] == STONE: return COMP_WINS
        if GAME[user] == SCISSORS: return USER_WINS
        if GAME[user] == PAPER: return DRAW


def main():
    while True:
        comp_choice = random.randint(1, 3)
        user_choice = make_choice()
        if user_choice == 0: break
        who_wins = game_func(comp_choice, user_choice)
        print(f'Компьютер - {GAME[comp_choice].upper()}, Ваш выбор - {GAME[user_choice].upper()}, {who_wins}\n')

main()