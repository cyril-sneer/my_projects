import my_funcs     # Из этого модуля берем функции создания, заполнения значениями и печати массива


def is_in_range(square: list) -> bool:          # Проверяет находятся ли значения в допустимом диапазоне
    for r in range(3):
        for c in range(3):
            if not (1 <= square[r][c] <= 9):
                return False
    return True


def is_unique(square: list) -> bool:            # Проверяет являются ли значения уникальными
    flat_list = [value for row in square for value in row]
    flat_set = set(flat_list)

    if len(flat_list) == len(flat_set): return True
    else: return False


def is_magic(square: list) -> bool:
    # Проверяет магичность по критерию равенства сумм строк, столбцов и диагоналей
    r_0_sum = sum(square[0])
    r_1_sum = sum(square[1])
    r_2_sum = sum(square[2])
    c_0_sum = square[0][0] + square[1][0] + square[2][0]
    c_1_sum = square[0][1] + square[1][1] + square[2][1]
    c_2_sum = square[0][2] + square[1][2] + square[2][2]
    d_1_sum = square[0][0] + square[1][1] + square[2][2]
    d_2_sum = square[0][2] + square[1][1] + square[2][0]

    if r_0_sum == r_1_sum == r_2_sum == c_0_sum == c_1_sum == c_2_sum == d_1_sum == d_2_sum:
        return True
    else:
        return False


def main():
    my_square = my_funcs.make_array(3, 3, 0)                # Создать массив 3 х 3
    my_funcs.input_array(my_square)                         # Ввести в него значения

    for r in range(3):                                      # Преобразовать элементы массива в числа
        for c in range(3):
            my_square[r][c] = int(my_square[r][c])

    my_funcs.print_array(my_square, '\t')                   # Напечатать массив для удобства

    if not is_in_range(my_square):                          # Проверить находятся ли значения в допустимом диапазоне
        print('Значения вне допустимого диапазона!')
    elif not is_unique(my_square):                          # Проверить являются ли значения уникальными
        print('Значения не являются уникальными!')
    else:
        if is_magic(my_square):                             # Проверить является ли квадрат магическим
            print('Это магический квадрат Ло Шу!')
        else:
            print('Это обычный квадрат. Никакой магии (')


if __name__ == '__main__':
    main()
