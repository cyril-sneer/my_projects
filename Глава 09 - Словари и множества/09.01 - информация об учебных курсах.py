ROOMS_DICT = {"CS101":3040, "CS102":4501, "CS103":6755, "NT110":1244, "CM241":1411}
TEACHERS_DICT = dict(CS101 = "Хайнс", CS102 = "Альварадо", CS103 = "Рич",
                     NT110 = "Берк", CM241 = "Ли")
TIME_DICT = dict([("CS101", "8:00"), ("CS102", "9:00"), ("CS103", "10:00"),
                  ("NT110", "11:00"), ("CM241", "13:00")])

def main():
    course_no = input("Введите номер курса: ")
    course_no = course_no.upper()
    print(f"Данные для курса {course_no}: ")
    print(f"Номер аудитории: {ROOMS_DICT.get(course_no, 'Курс не найден!')}")
    print(f"Преподаватель: {TEACHERS_DICT.get(course_no, 'Курс не найден!')}")
    print(f"Время начала занятий: {TIME_DICT.get(course_no, 'Курс не найден!')}")

if __name__ == '__main__':
    main()