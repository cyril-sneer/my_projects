class Person:
    def __init__(self, name: str = 'John Dow', address: str = "unknown", phone: str = "000-00-00"):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone


class Customer(Person):
    def __init__(self, name: str = 'John Dow', address: str = "unknown", phone: str = "000-00-00",
                 client_num: int = 0, in_mailing_list: bool = False):
        Person.__init__(self, name, address, phone)
        self.__client_num = client_num
        self.__in_mailing_list = in_mailing_list

    def set_client_num(self, client_num):
        self.__client_num = client_num

    def get_client_num(self):
        return self.__client_num

    def set_in_mailing_list(self, in_mailing_list):
        self.__in_mailing_list = in_mailing_list

    def get_in_mailing_list(self):
        return self.__in_mailing_list


def main():
    name = input("Введите имя покупателя: ")
    address = input("Введите адрес покупателя: ")
    phone = input("Введите номер телефона: ")
    client_num = int(input("Введите ID номер клиента: "))
    answer = ""
    while answer not in ['Д', 'Н']:
        answer = input("Присылать ли рассылки? (Д/Н): ").upper()
    in_mailing_list = True if answer == 'Д' else False

    customer = Customer(name, address, phone, client_num, in_mailing_list)

    print()
    print("Информация про клиента: ")
    print(f"Имя: {customer.get_name()}")
    print(f"Адрес: {customer.get_address()}")
    print(f"Телефон: {customer.get_phone()}")
    print(f"ID клиента: {customer.get_client_num()}")
    print(f"В списке рассылки: {'Да' if customer.get_in_mailing_list() else 'Нет'}")

if __name__ == '__main__':
    main()
