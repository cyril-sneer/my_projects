import random


class Question:
    def __init__(self, question: str = '',
                 answer1: str = '', answer2: str = '', answer3: str = '', answer4: str = '',
                 right_answer_num: int = 1):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__right_answer = right_answer_num

    def set_question(self, question: str):
        self.__question = question
    def get_question(self):
        return self.__question

    def set_answer1(self, answer):
        self.__answer1 = answer
    def get_answer1(self):
        return self.__answer1

    def set_answer2(self, answer):
        self.__answer2 = answer
    def get_answer2(self):
        return self.__answer2

    def set_answer3(self, answer):
        self.__answer3 = answer
    def get_answer3(self):
        return self.__answer3

    def set_answer4(self, answer):
        self.__answer4 = answer
    def get_answer4(self):
        return self.__answer4

    def set_right_answer(self, right_answer_num):
        self.__right_answer = right_answer_num
    def get_right_answer(self):
        return self.__right_answer

    def __str__(self):
        string = f"{self.__question}\n" \
                 f"1 - {self.__answer1}\n" \
                 f"2 - {self.__answer2}\n" \
                 f"3 - {self.__answer3}\n" \
                 f"4 - {self.__answer4}\n"
        return string


"""
Самая длинная река?                 - Днепр/Нил/Амазонка/Миссисипи              - 2
Столица Франции?                    - Париж/Рим/Осло/Варшава                    - 1
В каком году образовалась Украина?  - 1985/2000/1991/1993                       - 3
Как называется спутник Земли?       - Фобос/Ганимед/Каллисто/Луна               - 4
День Независимости Украины?         - 4 июля/16 октября/24 августа/7 января     - 3
Самое глубокое озеро?               - Титикака/Байкал/Мичеган/Синевир           - 2
Где живут кенгуру?                  - Австралия/Севрная Америка/Европа/Африка   - 1
Самый большой океан?                - Атлантический/Индийский/Тихий/Сев.Ледов   - 3 
Чьи спутники Ио и Европа?           - Марс/Сатурн/Венера/Юпитер                 - 4
Самая высока гора?                  - Эверест/Монблан/Говерла/Килиманджаро      - 1
"""

def main():
    quiz = [Question("Самая длинная река?", "Днепр", "Нил", "Амазонка", "Миссисипи", 2),
            Question("Столица Франции?", "Париж", "Рим", "Осло", "Варшава", 1),
            Question("В каком году образовалась Украина?", "1985", "2000", "1991", "1993", 3),
            Question("Как называется спутник Земли?", "Фобос", "Ганимед", "Каллисто", "Луна", 4),
            Question("День Независимости Украины?", "4 июля", "16 октября", "24 августа", "7 января", 3),
            Question("Самое глубокое озеро?", "Титикака", "Байкал", "Мичеган", "Синевир", 2),
            Question("Где живут кенгуру?", "Австралия", "Севрная Америка", "Европа", "Африка", 1),
            Question("Самый большой океан?", "Атлантический", "Индийский", "Тихий", "Сев.Ледовитый", 3),
            Question("Чьи спутники Ио и Европа?", "Марс", "Сатурн", "Венера", "Юпитер", 4),
            Question("Самая высока гора?", "Эверест", "Монблан", "Говерла", "Килиманджаро", 1)]

    player_1 = 0
    player_2 = 0
    random.shuffle(quiz)
    for number, question in enumerate(quiz, start=1):
        if number % 2 != 0:
            player_1 += set_question(1, question)
        else:
            player_2 += set_question(2, question)

    print(f"\nИгра окончена!\nПолучено правильных ответов: игрок 1 - {player_1}, игрок 2 - {player_2}")
    if player_1 == player_2:
        print("Ничья!")
    elif player_1 > player_2:
        print("Победил игрок 1!")
    else:
        print("Победил игрок 2!")

def set_question(player: int, question: Question):
    q = input(f"Вопрос игроку {player}\n{question}: ")
    if int(q) == question.get_right_answer():
        print("Это ПРАВИЛЬНЫЙ ответ!\n")
        return 1
    else:
        right_answer_num = question.get_right_answer()
        right_answer_text = eval("question.get_answer" + str(right_answer_num) + "()")
        print(f"Вы ошиблись! Правильный ответ: {right_answer_num} - {right_answer_text}\n")
        return 0

if __name__ == '__main__':
    main()