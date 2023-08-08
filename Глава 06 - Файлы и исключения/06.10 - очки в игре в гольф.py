import my_funcs
import os

class Consts:
    # EXIT = '0'
    # INPUT = '1'
    # OUTPUT = '2'
    MY_MENU = {'1': 'Ввод данных игроков',
               '2': 'Вывод результатов',
               '3': 'Очистить данные',
               '0': 'Выход'}
    DATA_FILE = r'data\golf.txt'

# def show_menu() -> str:
#
#     # while True:
#     #     print('1 - Ввод данных игроков')
#     #     print('2 - Вывод результатов')
#     #     print('0 - Выход')
#     #     choice = input('Сделайте ваш выбор:\t')
#     #     if choice not in (Consts.EXIT, Consts.INPUT, Consts.OUTPUT):
#     #         print('Некорректный ввод..\n')
#     #     else: break
#     # return choice
#
#     while True:
#         print('1 - Ввод данных игроков')
#         print('2 - Вывод результатов')
#         print('0 - Выход')
#         choice = input('Сделайте ваш выбор:\t')
#
#         match choice:
#             case Consts.EXIT | Consts.INPUT | Consts.OUTPUT:
#                 return choice
#             case _:
#                 print('Некорректный ввод..\n')


def input_data(): # Ввод данных игроков
    print()
    print('- ВВОД ДАННЫХ ИГРОКОВ -')
    work_file = open(Consts.DATA_FILE, 'a')
    while True:
        name = input('Введите имя игрока, пустая строка - выход:\t')
        if name == '': break
        score = input('Введите количество очков:\t')
        work_file.write(f'{name}\n')
        work_file.write(f'{score}\n')
    print()
    work_file.close()


def output_data(): # Вывод результатов
    print()
    print('- ВЫВОД РЕЗУЛЬТАТОВ -')
    work_file = open(Consts.DATA_FILE, 'r')

    name = work_file.readline().rstrip()
    while name != '':
        score = work_file.readline().rstrip()
        print(f'{name} - {score}')
        name = work_file.readline().rstrip()

    print()
    work_file.close()


def main():
    while True:
        choice = my_funcs.show_menu(Consts.MY_MENU)
        if choice == '1': input_data()
        elif choice == '2':
            try: output_data()
            except IOError: print('\nОШИБКА! отсутствует файл с данными!\n')
        elif choice == '3':
            try: os.remove(Consts.DATA_FILE)    # удаление файла с данными
            except IOError: print('\nОШИБКА! отсутствует файл с данными!\n')
            else: print('\nДанные очищены..\n')
        else: print('bye, bye...'); break       # Выход


if __name__ == '__main__':
    main()
