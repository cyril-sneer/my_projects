import os #

def main():
    found = False

    students_file = open('students.txt', 'r')
    temp_file = open('temp.txt', 'w')

    name_for_change = 'Джулия Милан'

    name = students_file.readline().rstrip('\n')
    while name != '':
        score = students_file.readline().rstrip('\n')

        if name == name_for_change:
            score = '100'
            found = True

        temp_file.write(f'{name}\n')
        temp_file.write(f'{score}\n')

        name = students_file.readline().rstrip('\n')

    students_file.close()
    temp_file.close()

    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if found:
        print('Файл обновлен')
    else:
        print('Не найдено!')

if __name__ == '__main__':
    main()
