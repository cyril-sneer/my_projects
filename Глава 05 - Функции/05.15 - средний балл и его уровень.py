def calc_average(marks: list) -> float:
    marks_sum = 0
    for i in range(len(marks)):
        marks_sum += marks[i]
    average_mark = marks_sum / len(marks)
    return average_mark


def determine_grade(m):
    grade = ''
    if m >= 90:
        grade = 'A'
    elif m >= 80:
        grade = 'B'
    elif m >= 70:
        grade = 'C'
    elif m >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def read_marks(marks: list):
    while True:
        mark = int(input('Введите оценку от 1 до 100, 0 - конец ввода:\t'))
        if mark == 0:
            break
        elif 1 <= mark <= 100:
            marks.append(mark)
        else:
            print('Недопустимый ввод!')


def print_marks(marks: list, average_mark: float):
    for m in range(len(marks)):
        print(f'Оценка {m + 1} = {marks[m]} --> {determine_grade(marks[m])}')

    print(f'\nВаш средний бал = {average_mark:.2f} --> {determine_grade(average_mark)}')


def main():
    mark_list = []  # список оценок
    read_marks(mark_list)

    if len(mark_list) == 0:
        print('Вы не ввели ни одной оценки!')
        return

    print()
    print_marks(mark_list, calc_average(mark_list))


main()
