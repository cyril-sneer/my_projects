import my_funcs

DATA_FILE_NAME = r"data\pbnumbers.txt"

# def get_frequency(number_info:list[int, int, int]) -> int:
#     return number_info[1]
#
# def get_day(number_info:list[int, int, int]) -> int:
#     return number_info[2]

def main():
    numbers = my_funcs.make_array(70, 3, 0)      # числа = список для каждого числа[значение, количество вхождений, день розыгрыша]
    pb_numbers = my_funcs.make_array(27, 3, 0)   # power ball числа = список [значение, количество вхождеий, день розыгрыша]
    # массивы создаем на 1 строку больше, чтобы в последствии выпавшее число совпадало с индексом соотв строки массива

    data_file = open(DATA_FILE_NAME, "r")                                   # читаем файл с результатами
    draw_results = [string.rstrip() for string in data_file.readlines()]    # построчно в список draw_results
    data_file.close()
    draw_results.insert(0, "")  # в результыты розыгрышей тоже добавляем пустую строку в начало для совпадения индексов

    for draw_day in range(1, len(draw_results)):                      # для каждого дня розыгрыша
        draw_numbers = list(map(int, draw_results[draw_day].split()))  # получаем список из выпавших номеров в день draw_day
        for num in draw_numbers[:-1]:           # для каждого из 5 выпавших номеров вносим в соотв строку массива numbers
            numbers[num][0] = num               # собственно число
            numbers[num][1] += 1                # увеличиваем на 1 кол-во вхождений этого числа
            numbers[num][2] = draw_day          # номер дня розыгрыша
        pb_number = draw_numbers[-1]            # число power ball равно последнему элементу списка выпавших номеров
        pb_numbers[pb_number][0] = pb_number    # вносим в соотв строку массива pb_numbers само число
        pb_numbers[pb_number][1] += 1           # увеличиваем на 1 кол-во вхождений этого числа
        pb_numbers[pb_number][2] = draw_day     # номер дня розыгрыша

    del numbers[0]        # удаляем пустые элементы массивов чисел чтобы не мешали при сортировке. Они больше не нужны
    del pb_numbers[0]     # удаляем пустые элементы массивов чисел чтобы не мешали при сортировке. Они больше не нужны

    # определяем 10 наименее и наиболее распространенных чисел.
    # Для этого сортируем список numbers с информацией по выпавшим числам по частоте вхождения чисел
    # частота вхождения - это элемент [1] вложенных списков number_info,
    # содержащих информацию про конкретные числа
    numbers.sort(key = lambda number_info: number_info[1])

    # 10 наиболее распространенных чисел - берем 10 чисел с конца списка
    most_frequently_numbers = []
    for i in range(len(numbers)-1, len(numbers)-11, -1):
        most_frequently_numbers.append(numbers[i][0])
    # 10 наименее распространенных чисел
    less_frequently_numbers = []
    for i in range(10):
        less_frequently_numbers.append(numbers[i][0])

    # определяем 10 наиболее "созревших" чисел.
    # Для этого сортируем список numbers с информацией по выпавшим числам по дню,
    # когда это число в последний раз выпало - это элемент [2] вложенных списков number_info,
    # содержащих информацию про конкретные числа
    numbers.sort(key=lambda number_info: number_info[2])

    # 10 наиболее "созревших" чисел
    mature_numbers = []
    for i in range(10):
        mature_numbers.append(numbers[i][0])

    print(f'10 наиболее распространенных чисел {most_frequently_numbers}')
    print(f'10 наименее распространенных чисел {less_frequently_numbers}')
    print(f'10 наиболее "созревших" чисел {mature_numbers}')

    # для вывода списка чисел с частотой их вхождения, сортируем список numbers
    # по самим числам - это элемент [0] вложенных списков number_info,
    # содержащих информацию про конкретные числа
    numbers.sort(key=lambda number_info: number_info[0])

    # выводим список на печать
    print("Список чисел и их частота вхождения:")
    for num in numbers:
        print(f'{num[0]}  -  {num[1]}')

    print("Список power ball чисел и их частота вхождения:")
    for num in pb_numbers:
        print(f'{num[0]}  -  {num[1]}')


if __name__ == '__main__':
    main()





