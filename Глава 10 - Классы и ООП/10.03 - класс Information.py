class Information:
    def __init__(self, name:str="", address:str="", age:int=0, phone:str=""):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address

    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age

    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone

def main():
    me = Information("Sergey", "Kharkiv", 46, "+380 50 328-55-66")
    wife = Information("Katia", "Lille", 47, "+380 95 350-50-50")

    name = input("Введите имя: ")
    address = input("Введите адрес: ")
    age = int(input("Введите возраст: "))
    phone = input("Введите номер телефона: ")
    son = Information()
    son.set_name(name)
    son.set_address(address)
    son.set_age(age)
    son.set_phone(phone)


if __name__ == '__main__':
    main()