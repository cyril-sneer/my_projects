import random

FILE_WITH_ANSWERS = r'data\8_ball_responses_ru.txt'

answers_file = open(FILE_WITH_ANSWERS, 'r')
answers = [ans.rstrip() for ans in answers_file.readlines()]
answers_file.close()

while True:
    quest = input('Введите ваш вопрос: ')
    if quest == '': break
    else: print(f'{random.choice(answers)}')
