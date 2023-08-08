import mysql.connector
from my_funcs import TextMenu

CONN_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "database": "student_info",
    "user": "test_user",
    "password": "12345",
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": True
}

MAIN_MENU = {
    "-": "Создание и наполнение базы",
    "1": "Факультеты",
    "2": "Специальности",
    "3": "Студенты",
    "0": "Выход"
}

CREATE_DB_MENU = {
    "1": "Создать БД",
    "2": "Наполнить БД тестовыми значениями",
    "0": "Вернуться назад"
}

ACTIONS_MENU = {
    "1": "Добавить",
    "2": "Найти",
    "3": "Изменить",
    "4": "Удалить",
    "5": "Показать все",
    "0": "Вернуться назад"
}

def main():
    while True:
        match TextMenu(MAIN_MENU, '\n--ГЛАВНОЕ МЕНЮ--').get_choice():
            case "0":  # QUIT
                break
            case "-":  # CREATE DB & INSERT VALUES
                db_menu()
            case "1":  # DEPARTMENTS
                pass
            case "2":  # MAJORS
                pass
            case "3":  # STUDENTS
                students_menu()

def db_menu():
    while True:
        match TextMenu(CREATE_DB_MENU, '\n--МЕНЮ БАЗЫ ДАННЫХ--').get_choice():
            case "0":  # RETURN
                break
            case "1":  # CREATE DB
                create_db()
            case "2":  # INSERT VALUES
                insert_values()

def students_menu():
    while True:
        match TextMenu(ACTIONS_MENU, '\n--МЕНЮ СТУДЕНТОВ--').get_choice():
            case "0":  # RETURN
                break
            case "1":  # ADD
                add_student()
            case "2":  # FIND
                pass
            case "3":  # CHANGE
                pass
            case "4":  # DELETE
                pass
            case "5":  # SHOW ALL
                show_all_students()

def create_db():
    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()

        # CREATE DATABASE
        cur.execute('CREATE DATABASE IF NOT EXISTS student_info')
        cur.execute('USE student_info')

        # CREATE TABLES
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS Departments
                    (DeptID VARCHAR(3) NOT NULL PRIMARY KEY,
                    Name VARCHAR(30) NOT NULL)
        ''')
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS Majors
                    (MajorID VARCHAR(6) NOT NULL PRIMARY KEY,
                    Name VARCHAR(30) NOT NULL)
        ''')
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS Students
                    (StudentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(30) NOT NULL,
                    MajorID VARCHAR(6) NOT NULL,
                    DeptID VARCHAR(3) NOT NULL,
                    FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID))
        ''')

    CONN_CONFIG['database'] = 'student_info'

def insert_values():
    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()

        # INSERT VALUES
        cur.execute('''
                    INSERT INTO Departments (DeptID, Name)
                    VALUES
                    ("TEC", "Technical"),
                    ("HUM", "Humanitarian"),
                    ("MED", "Medical"),
                    ("LAW", "Juridical")
        ''')
        cur.execute('''
                    INSERT INTO Majors (MajorID, Name)
                    VALUES
                    ("ECO001", "Economist"),
                    ("LAW001", "Lawyer"),
                    ("LAW002", "Judge"),
                    ("ENG001", "Engineer"),
                    ("ENG002", "IT specialist"),
                    ("HUM001", "Teacher"),
                    ("MED001", "Doctor"),
                    ("MED002", "Nurse")
        ''')
        cur.execute('''
                    INSERT INTO Students (Name, MajorID, DeptID)
                    VALUES
                    ("Serge", "LAW001", "LAW"),
                    ("Alex", "HUM001", "HUM"),
                    ("Katty", "MED002", "MED")
        ''')

        cnx.commit()

def show_all_students():
    print('\n-Список студентов-')
    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()

        stmt_select = '''
        select Students.Name, Majors.Name, Departments.Name
        FROM students, majors, departments
        WHERE students.majorid = majors.majorid
        AND students.deptID = departments.deptID
        '''
        cur.execute(stmt_select)

        result = cur.fetchall()
        print_request_result(result)

def print_request_result(request_result: list):
    for rec in request_result:
        print(' - '.join(rec))

def get_valid_options(col_name, table_name):
    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()
        cur.execute(f"select {col_name} from {table_name}")
        options = [value[0] for value in cur.fetchall()]
    return options

def add_student():
    print('\n-Добавление студента-')
    name = input('Введите имя: ')

    while True:
        major_id = input("Введите код специальности: ")
        valid_options = get_valid_options("MajorID", "majors")
        if major_id.upper() in valid_options:
            break
        else:
            print('Некорректный ввод, повторите...')
            answer = input('Вам нужна подсказка? [y/n]: ').upper()
            if answer == 'Y':
                print(*get_valid_options("MajorID", "majors"), sep=", ")

    while True:
        department_id = input("Введите код факультета: ")
        valid_options = get_valid_options('DeptID', 'departments')
        if department_id.upper() in valid_options:
            break
        else:
            print('Некорректный ввод, повторите...')
            answer = input('Вам нужна подсказка? [y/n]: ').upper()
            if answer == 'Y':
                print(*get_valid_options('DeptID', 'departments'), sep=", ")

    with mysql.connector.connect(**CONN_CONFIG) as cnx:
        cur = cnx.cursor()
        cur.execute('''
                    INSERT INTO Students (Name, MajorID, DeptID)
                    VALUES
                    (%s, %s, %s)
                    ''', (name, major_id, department_id))
        cnx.commit()

if __name__ == '__main__':
    main()