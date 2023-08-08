import my_funcs
import pickle


FILE_NAME = r"data\e-mails.dat"
MENU = {"1": "Найти",
        "2": "Добавить",
        "3": "Изменить",
        "4": "Удалить",
        "5": "Показать",
        "0": "Выход"}


def main():

    try:
        data_file = open(FILE_NAME, "rb")
        phonebook = pickle.load(data_file)
        data_file.close()
    except IOError:
        phonebook = {}


    while True:
        choice = my_funcs.show_menu(MENU)

        if choice == "0":
            save_data(phonebook, FILE_NAME)
            print(f"\nbye, bye..\n")
            break
        elif choice == "2":
            add_mail(phonebook)
        else:
            if len(phonebook) != 0:
                if choice == "1":
                    find_mail(phonebook)
                elif choice == "3":
                    change_mail(phonebook)
                elif choice == "4":
                    del_mail(phonebook)
                elif choice == "5":
                    show_pbook(phonebook)
            else:
                print(f"\nВ телефонной книге пока нет ни одной записи!\n")


def save_data(data, file_name):
    data_file = open(file_name, "wb")
    pickle.dump(data, data_file)
    data_file.close()


def add_mail(pbook):
    print()
    name = input(f"Введите имя: ")
    if name in pbook:
        print(f"Запись для {name} уже существует. Воспользуйтесь функцией замены.")
    else:
        phone = input(f"Введите номер: ")
        pbook[name] = phone
    input("press any key..\n")


def find_mail(pbook):
    print()
    name = input(f"Введите имя: ")
    print(pbook.get(name, "Запись не найдена"))
    input("press any key..\n")


def change_mail(pbook):
    print()
    name = input(f"Введите имя: ")
    if name in pbook:
        phone = input(f"Введите номер: ")
        pbook[name] = phone
    else:
        print("Запись не найдена")
    input("press any key..\n")


def del_mail(pbook):
    print()
    name = input(f"Введите имя: ")
    if name in pbook:
        del pbook[name]
        print("Запись удалена")
    else:
        print(f"Запись не найдена")
    input("press any key..\n")


def show_pbook(pbook):
    print()
    for rec in pbook:
        print(f"{rec} : {pbook[rec]}")
    input("press any key..\n")


if __name__ == '__main__':
    main()