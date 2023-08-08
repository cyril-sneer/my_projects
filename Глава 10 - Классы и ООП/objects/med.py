class Procedure:
    def __init__(self, title:str = '', date:str = '', doctor:str = '', cost:float = 0.00):
        self.__title = title
        self.__date = date
        self.__doctor = doctor
        self.__cost = cost

    def set_title(self, title: str):
        self.__title = title
    def get_title(self):
        return self.__title

    def set_date(self, date: str):
        self.__date = date
    def get_date(self):
        return self.__date

    def set_doctor(self, doctor: str):
        self.__doctor = doctor
    def get_doctor(self):
        return self.__doctor

    def set_cost(self, cost: float):
        self.__cost = cost
    def get_cost(self):
        return self.__cost

    def __str__(self):
        res = f"{self.__title} - {self.__date} - {self.__doctor} - {self.__cost}"
        return res


class Patient:
    def __init__(self, name: dict = {}, address: dict = {}, phone: str = '', extra: dict = {}):
        self.__name: dict = name
        self.__address: dict = address
        self.__phone: str = phone
        self.__extra: dict = extra
        self.__procs: list = []
        self.__treatment_cost: float = 0

    def set_name(self, fst_name: str, scnd_name: str, fath_name: str):
        self.__name = dict(first_name=fst_name,
                           second_name=scnd_name,
                           father_name=fath_name)

    def set_address(self, addr: str, city: str, reg: str, ind: int):
        self.__address = dict(address=addr,
                              city=city,
                              region=reg,
                              post_index=ind)

    def set_phone(self, ph: str):
        self.__phone = ph

    def set_extra(self, name: str, phone: str):
        self.__extra = dict(name=name,
                            phone=phone)

    def __str__(self):
        res = f"Имя: {self.__name['first_name']} \t " \
              f"Фамилия: {self.__name['second_name']} \t " \
              f"Отчество: {self.__name['father_name']} \n" \
              f"Адрес: {self.__address['address']} \t " \
              f"Город: {self.__address['city']} \t " \
              f"Регион: {self.__address['region']} \t " \
              f"Индекс: {self.__address['post_index']} \n" \
              f"Телефон: {self.__phone} \n" \
              f"Экстра контакт: {self.__extra['name']} \t {self.__extra['phone']} "
        return res

    def add_proc(self, proc:Procedure):
        self.__procs.append(proc)
        self.__treatment_cost += proc.get_cost()

    def get_procs(self):
        return self.__procs

    def get_treatment_cost(self):
        return self.__treatment_cost
