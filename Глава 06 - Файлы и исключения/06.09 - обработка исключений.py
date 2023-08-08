def main():
    file_name = r'data\numbers.txt'

    try:
        numbers_file = open(file_name, 'r')
        summa = 0
        count = 0
        for line in numbers_file:
            summa += int(line)
            count += 1
        numbers_file.close()

        print(f'Среднее арифметическое равно {summa / count}')
    except IOError:
        print('Ошибка поиска файла')
    except ValueError:
        print('Ошибка значения в файле')
    except ZeroDivisionError:
        print('Файл пустой')


if __name__ == '__main__':
    main()
