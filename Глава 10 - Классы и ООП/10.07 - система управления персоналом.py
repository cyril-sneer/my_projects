from objects import emp
import my_funcs
import pickle

FILE_NAME = r"data\employees.dat"
MENU = {"1": "Найти",
        "2": "Добавить",
        "3": "Изменить",
        "4": "Удалить",
        "5": "Показать",
        "0": "Выход"}

def main():
    employees_db = load_data(FILE_NAME)

    while True:
        choice = my_funcs.show_menu(MENU)

        if choice == "0":
            save_data(FILE_NAME, employees_db)
            print(f"\nbye, bye..\n")
            break
        elif choice == "2":
            add_record(employees_db)
        elif len(employees_db) == 0:
            print("\nВ базе данных пока нет ни одной записи...\n")
        elif choice == "1":
            find_record(employees_db)
        elif choice == "3":
            modify_record(employees_db)
        elif choice == "4":
            del_record(employees_db)
        elif choice == "5":
            print_all(employees_db)
    return

def load_data(data_file: str):
    try:
        file = open(data_file, 'rb')
        employees_db = pickle.load(file)
        file.close()
    except IOError:
        employees_db = {}
    return employees_db

def save_data(data_file: str, data_base: dict):
    file = open(data_file, 'wb')
    pickle.dump(data_base, file)
    file.close()

def add_record(data_base: dict):
    print()
    emp_id = input('Введите ID сотрудника: ')
    if emp_id in data_base:
        print("\nЗапись для сотрудника с таким ID уже существует! Воспользуйтесь функцией ИЗМЕНЕНИЯ данных\n")
    else:
        emp_name = input("Введите имя: ")
        emp_dept = input("Введите отдел: ")
        emp_pos = input("Введите должность: ")
        data_base[emp_id] = emp.Employee(emp_name, emp_id, emp_dept, emp_pos)
        print("\nЗапись успешно добавлена..\n")

def find_record(data_base: dict):
    emp_id = input('Введите ID сотрудника: ')
    print(f"\n{data_base.get(emp_id, 'Запись не найдена!')}\n")

def modify_record(data_base: dict):
    emp_id = input('Введите ID сотрудника: ')
    if emp_id in data_base:
        emp_name = input("Введите имя: ")
        emp_dept = input("Введите отдел: ")
        emp_pos = input("Введите должность: ")
        data_base[emp_id].set_name(emp_name)
        data_base[emp_id].set_dept(emp_dept)
        data_base[emp_id].set_position(emp_pos)
        print(f"\nЗапись модифицирована..\n")
    else:
        print(f"\nЗапись не найдена!\n")

def del_record(data_base: dict):
    emp_id = input('Введите ID сотрудника: ')
    if emp_id in data_base:
        del data_base[emp_id]
        print(f"\nЗапись удалена..\n")
    else:
        print(f"\nЗапись не найдена!\n")

def print_all(data_base: dict):
    print()
    for rec in data_base:
        print(data_base[rec])
    print()


if __name__ == '__main__':
    main()
