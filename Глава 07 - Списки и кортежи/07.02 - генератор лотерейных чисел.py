import random

random_list = []
for i in range(7):
    random_list.append(random.randint(0, 9))

for i, v in enumerate(random_list):
    print(v, end='')
    if i < 6:
        print(', ', end='')


# # Упражнение по программированию 7.2
#
# # Генератор лотерейных чисел
#
# import random
#
#
# def main():
#     # Инициализировать список чисел.
#     number_list = [0, 0, 0, 0, 0, 0, 0]
#
#     # Присвоить списку случайные числа.
#     for i in range(7):
#         number_list[i] = random.randint(0, 9)
#
#     # Показать числа в одной строке.
#     for i in range(7):
#         print(number_list[i], end='')
#
#         # Отделить текущее число от следующего.
#         if i < 6:
#             print(', ', end='')
#
#
# # Вызвать главную функцию.
# main()