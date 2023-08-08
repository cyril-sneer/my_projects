import mysql.connector
import my_funcs
# import tkinter
# from tkinter.ttk import *

CONN_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "database": "test",
    "user": "test_user",
    "password": "12345",
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": False
}

MAIN_MENU = {
    "1": "Добавить",
    "2": "Найти",
    "3": "Изменить",
    "4": "Удалить",
    "5": "Показать все",
    "0": "Выход"
}

def main():
    create_table(CONN_CONFIG)

    while True:
        choice = my_funcs.show_menu(MAIN_MENU)
        if choice == "0":
            break
        else:
            match choice:
                case "1":
                    add_record()
                case "2":
                    find_record()
                case "3":
                    update_record()
                case "4":
                    delete_record()
                case "5":
                    show_all_records()

def create_table(config: dict):
    with mysql.connector.connect(**config) as cnx:
        cur = cnx.cursor()

        stmt_create = '''CREATE TABLE IF NOT EXISTS phonebook 
                        (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        Name CHAR(20), 
                        Phone CHAR(20))'''
        cur.execute(stmt_create)

def add_record():
    print("\n-ДОБАВЛЕНИЕ ЗАПИСИ-")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()
        stmt_insert = "INSERT INTO phonebook (Name, Phone) values (%s, %s)"
        cur.execute(stmt_insert, (name, phone))
        cnx.commit()
        print('Запись добавлена...\n')

def find_record():
    print("\n-ПОИСК ЗАПИСИ-")
    name = input("Введите имя: ")

    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()
        stmt_select = '''SELECT * FROM phonebook WHERE Name = %s'''
        cur.execute(stmt_select, (name, ))
        result = cur.fetchall()

        if len(result) == 0:
            print("\nЗаписи не найдены...\n")
        else:
            print(f'\nНайдено {len(result)} записей:\n')
            for rec in result:
                print_record(rec)
            print()

def update_record():
    print("\n-ИЗМЕНЕНИЕ ЗАПИСИ-")
    name = input("Введите имя: ")

    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()
        stmt_select = '''SELECT * FROM phonebook WHERE Name = %s'''
        cur.execute(stmt_select, (name, ))
        result = cur.fetchall()

        if len(result) == 0:
            print("\nЗаписи не найдены...\n")
        else:
            print(f'\nНайдено {len(result)} записей:\n')
            for rec in result:
                print_record(rec)

            id_numbers = tuple(rec[0] for rec in result)
            rec_id = -1
            while rec_id not in id_numbers:
                rec_id = int(input("Введите номер записи для изменения: "))

            name = input("Введите НОВОЕ имя: ")
            phone = input("Введите НОВЫЙ номер телефона: ")

            stmt_update = "UPDATE phonebook SET Name = %s, Phone =  %s WHERE Id = %s"
            cur.execute(stmt_update, (name, phone, rec_id))
            cnx.commit()
            print('Запись ИЗМЕНЕНА...\n')

def delete_record():
    print("\n-УДАЛЕНИЕ ЗАПИСИ-")
    name = input('Введите имя: ')

    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()
        stmt_select = '''SELECT * FROM phonebook WHERE Name = %s'''
        cur.execute(stmt_select, (name, ))
        result = cur.fetchall()

        if len(result) == 0:
            print("\nЗаписи не найдены...\n")
        else:
            print(f'\nНайдено {len(result)} записей:\n')
            for rec in result:
                print_record(rec)

            id_numbers = tuple(rec[0] for rec in result)
            rec_id = -1
            while rec_id not in id_numbers:
                rec_id = int(input("Введите номер записи для удаления: "))

            stmt_delete = '''DELETE FROM phonebook WHERE Id = %s'''
            cur.execute(stmt_delete, (rec_id, ))
            print("\nЗапись удалена...\n")
            cnx.commit()

def show_all_records():
    print("\n-ПЕЧАТЬ СПРАВОЧНИКА-")
    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()
        stmt_select = '''SELECT * FROM phonebook'''
        cur.execute(stmt_select)
        result = cur.fetchall()

        print(f'\nНайдено {len(result)} записей\n')
        for rec in result:
            print_record(rec)
        print()

def print_record(rec: tuple):
    id = rec[0]
    name = rec[1]
    phone = rec[2]
    print(f"ID: {id:<5} Name: {name:20} Phone: {phone:20}")


if __name__ == '__main__':
    main()