RiGHT_ANSWERS: list[str] = ['A', 'C', 'A', 'A', 'D',
                            'B', 'C', 'A', 'C', 'B',
                            'A', 'D', 'C', 'A', 'D',
                            'C', 'B', 'B', 'D', 'A']
ANSWERS_FILE: str = r'data\student_solution.txt'

def compare_lists(list1:list, list2:list)->list:
    list3 = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            list3.append(True)
        else:
            list3.append(False)
    return list3

def main():
    student_file = open(ANSWERS_FILE, 'r')
    student_answers = [answer.rstrip() for answer in student_file.readlines()]
    student_file.close()

    results = compare_lists(student_answers, RiGHT_ANSWERS)

    right_answers_q = results.count(True)
    wrong_answers_q = results.count(False)

    if right_answers_q >= 15:
        print('Экзамен сдан!')
    else:
        print('Экзамен НЕ сдан!!!')
    print(f'Правильных ответов - {right_answers_q}, НЕправильных - {wrong_answers_q} \n')

    print(f'  № | Правильный ответ | Ваш ответ | Результат')
    print('-' * 47)
    for answer in range(len(student_answers)):
        print(f'{(answer + 1):^4}|'
              f'{RiGHT_ANSWERS[answer]:^18}|'
              f'{student_answers[answer]:^11}|'
              f'{"+" if results[answer] else "ошибка!":^10}')


if __name__ == '__main__':
    main()