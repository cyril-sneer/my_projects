class Employee:
    def __init__(self, id_num=0, name=''):
        self.__id_num = id_num
        self.__name = name
    
    def set_id_num(self, id_num):
        self.__id_num = id_num
    
    def get_id_num(self):
        return self.__id_num
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name


class ProductionWorker(Employee):
    def __init__(self, id_num=0, name="", shift=1, hourly_rate=0.00):
        Employee.__init__(self, id_num, name)
        self.__shift = shift
        self.__hourly_rate = hourly_rate
    
    def set_shift(self, shift):
        self.__shift = shift
    
    def get_shift(self):
        return self.__shift
    
    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate
    
    def get_hourly_rate(self):
        return self.__hourly_rate
    
    def __str__(self):
        result = f"Данные сотрудника:\n" \
                 f"ID номер: {self.get_id_num() :10}\n" \
                 f"Имя: {self.get_name()}\n" \
                 f"Номер смены: {self.get_shift()}\n" \
                 f"Оплата труда: {self.get_hourly_rate():.2f}"
        return result


class ShiftSupervisor(Employee):
    def __init__(self, id_num=0, name='', year_salary=0.00, year_bonus=0.00):
        Employee.__init__(self, id_num, name)
        self.__year_salary = year_salary
        self.__year_bonus = year_bonus
    
    def set_year_salary(self, year_salary):
        self.__year_salary = year_salary
    
    def get_year_salary(self):
        return self.__year_salary
    
    def set_year_bonus(self, year_bonus):
        self.__year_bonus = year_bonus
    
    def get_year_bonus(self):
        return self.__year_bonus
    
    def __str__(self):
        result = f"Данные сотрудника:\n" \
                 f"ID номер: {self.get_id_num() :10}\n" \
                 f"Имя: {self.get_name()}\n" \
                 f"Годовая зарплата: {self.get_year_salary():.2f}\n" \
                 f"Годовой бонус: {self.get_year_bonus():.2f}"
        return result