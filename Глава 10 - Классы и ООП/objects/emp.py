class Employee:
    def __init__(self, name: str = '', id_num: str = '', dept: str = '', position: str = ''):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__position = position

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_id_num(self, id_num):
        self.__id_num = id_num
    def get_id_num(self):
        return self.__id_num

    def set_dept(self, dept):
        self.__dept = dept
    def get_dept(self):
        return self.__dept

    def set_position(self, position):
        self.__position = position
    def get_position(self):
        return self.__position

    def __str__(self):
        result = f"{'Имя: ' + self.__name:<30}" \
                 f"{'ID номер: ' + self.__id_num:<30}" \
                 f"{'Отдел: ' + self.__dept:<30}" \
                 f"{'Должность: ' + self.__position:<30}"
        return result
