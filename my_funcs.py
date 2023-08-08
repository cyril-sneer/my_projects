#!/usr/bin/python
# -*- coding: utf-8 -*import

class TextMenu:
    def __init__(self, menu_items: dict[str:str], title: str = "Menu", sep: str = '-'):
        '''
        Класс, создающий текстовое меню

        :param menu_items: Словарь, где
                           ключ = вариант выбора,
                           значение = подпись к этому варианту
        :param title: Название меню
        :param sep: Символ-разделитель, используемый при отображении меню
        '''
        self.__menu_items = menu_items
        self.__title = title
        self.__sep = sep
        self.__choice = ''

    def __show(self):
        '''
        Рисует текстовое меню на экране из переданного словаря
        :return:
        '''
        print(self.__title)
        for key, value in self.__menu_items.items():
            print(f'{key} {self.__sep} {value}')

    def get_choice(self):
        '''
        Запрашивает выбор пользователя.
        Если выбран вариант не из словаря, просит повторить ввод
        :return: возвращает выбор пользователя
        '''
        while True:
            self.__show()
            choice = input('Сделайте ваш выбор:\t')
            if choice not in self.__menu_items.keys():
                print('\nНекорректный ввод, повторите..\n')
            else:
                break
        return choice

def show_menu(menu: dict[str:str], sep: str = '-') -> str:
    """
    Функция создания текстового меню.

    Получает на вход словарь,
    где ключ = вариант выбора, значение = подпись к этому варианту.
    Возвращает строковое значение - выбор пользователя.
    Блокирует ввод вариантов не из словаря.

    Можно также передать разделитель,
    который будет между вариантом и его подписью
    при отображении меню
    """

    while True:
        for key, value in menu.items():
            print(f'{key} {sep} {value}')
        choice = input('Сделайте ваш выбор:\t')
        if choice not in menu.keys():
            print('\nНекорректный ввод, повторите..\n')
        else:
            break
    return choice


def show_menu_from_list(menu_items: list) -> str:
    menu_dict = {str(key): val for key, val in enumerate(menu_items, start=1)}
    return show_menu(menu_dict)


def make_array(rows_quantity: int, cols_quantity: int, value=None) -> list:
    """
    Создает массив размером rows_quantity строк на cols_quantity столбцов
    и заполняет его значениями value.
    Возвращает созданный массив
    """

    my_array = []
    for r in range(rows_quantity):
        my_array.append([])  # Добавляем пустую строку rows_quantity раз
        for c in range(cols_quantity):
            my_array[r].append(value)  # Наполняем каждую добавленную строку cols_quantity значениями

    return my_array


def input_array(my_array: list):
    """
    Последовательно запрашивает у пользователя значения для заполнения массива
    Заполнение идет построчно начиная с [0][0], затем [0][1], [0][2] и т.д.
    """
    for row_num in range(len(my_array)):  # начинаем обход по строкам до кол-ва строк в массиве
        for col_num in range(len(my_array[row_num])):  # внутри строки идем по столбцам до длины строки
            my_array[row_num][col_num] = \
                input(f'Input value for [{row_num}, {col_num}]: ')  # запрашиваем и заполняем значения
    return


def print_array(my_array: list, sep=' '):
    """Печатает массив в табличной форме"""
    for row in my_array:  # Начинаем обход по строкам. Считываем строку целиком
        for col_num, value in enumerate(row):  # Внутри строки обход по столбцам. Считываем номер столбца и значение
            print(f'{value}', end='')  # печатаем значения
            if col_num < len(row) - 1:  # если значение не последнее в строке
                print(f'{sep}', end='')  # печатаем разделитель
        print()  # переходим к следующей строке


def is_prime(number: int) -> bool:
    """Проверяет, является ли число простым. Если да, возвращает True, иначе - False"""
    prime = True
    for n in range(2, abs(number)):  # проверяет все возможные делители от 2 до number-1
        if number % n == 0:  # если number делится без остатка на делитель,
            prime = False  # значит number не является простым
            break  # и дальше можно не проверять
    return prime


def valid_password(password):
    # Назначить булевым переменным значение False.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Приступить к валидации.
    # Начать с проверки длины пароля.
    if len(password) >= 7:
        correct_length = True

        # Проанализировать каждый символ и установить
        # соответствующий флаг, когда
        # требуемый символ найден.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

        # Определить, удовлетворены ли все требования.
        # Если это так, то назначить is_valid значение True.
        # В противном случае назначить is_valid значение False.
        if correct_length and has_uppercase and \
                has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False

        # Вернуть переменную is_valid.
        return is_valid


def print_sequence(input_sequence: list | tuple | set | str, columns: int = 10, sep: str = ", ") -> None:
    """
    Печатает последовательность элементов в несколько колонок
    :param input_sequence: последовательность, которую нужно напечатать
    :param columns: количество колонок (по умолчанию 10)
    :param sep: символ разделитель (по умолчанию ', '
    :return:
    """
    i = 1                               # установить индекс элемента в 1
    for item in input_sequence:
        print(item, end="")             # напечатать элемент
        if i % columns == 0:            # если это последняя колонка
            print()                     # перевести строку
        elif i < len(input_sequence):   # если колонка не последняя и не последний символ в последовательности
            print(sep, end="")          # напечатать разделитель
        else:                           # когда печать последовательности окончена
            print()                     # перевести строку
        i += 1                          # увеличить индекс элемента на 1


def print_list(input_sequence: list | tuple | str, columns: int = 10, sep: str = ", ") -> None:
    from math import ceil
    string_qty = ceil(len(input_sequence) / columns)
    for s in range(string_qty):
        print(*input_sequence[s * columns: s * columns + columns], sep=sep) # печать среза списка!!!


def sort_dict_rec(inbound_dict:dict) -> dict:
    """
    Сортировка словаря по ключу с помощью рекурсии
    :param inbound_dict: Словарь, который требуется отсортировать.
    :return: Возвращает отсортированный словарь
    """
    if not inbound_dict:
        return {}
    else:
        sorted_dict = {}
        min_key = min(inbound_dict.keys())
        sorted_dict[min_key] = inbound_dict.pop(min_key)
        sorted_dict.update(sort_dict_rec(inbound_dict))
        return sorted_dict


def sort_dict_iter(inbound_dict:dict) -> dict:
    """
    Сортировка словаря по ключу с помощью итерации
    :param inbound_dict:
    :return:
    """
    # sorted_keys =
    sorted_dict = {}
    for key in sorted(inbound_dict.keys()):
        sorted_dict[key] = inbound_dict[key]
    return sorted_dict


def counter(start: int = 0):
    """
    Функция счетчик, реализованная замыканием.
    Сначала нужно создать переменную,
    вызвав данную функцию и передав ей стартовое значение счетчика.
    В переменной сохранится ссылка на собственно функцию счетчик.
    Далее при каждом вызове этой переменной с (), счетчик будет увеличиваться на 1.

    :param start: Стартовое значение счетчика, по умолчанию 0.
    :return: Возвращает счетчик, увеличенный на 1.
    """

    def step():
        nonlocal start
        start += 1
        return start

    return step


def matrix(columns_qty: int = 1, rows_qty: int = 1, value=None) -> list[list[None]]:
    m = [[value for c in range(columns_qty)] for r in range(rows_qty)]
    return m

