import mysql.connector
import tkinter
from tkinter.ttk import *

CONN_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "test_user",
    "password": "12345",
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": True,
}

CITIES = (
    (1, 'Токио', 38001000),
    (2, 'Дельфи', 25703168),
    (3, 'Шанхай', 23740778),
    (4, 'Сан-Паоло', 21066245),
    (5, 'Мумбай', 21042538),
    (6, 'Мехико', 20998543),
    (7, 'Пекин', 20383994),
    (8, 'Осака', 20237645),
    (9, 'Каир', 18771769),
    (10, 'Нью-Йорк', 18593220),
    (11, 'Дакка', 17598228),
    (12, 'Карачи', 16617644),
    (13, 'Буэнос-Айрес', 15180176),
    (14, 'Калькутта', 14864919),
    (15, 'Стамбул', 14163989),
    (16, 'Чунцин', 13331579),
    (17, 'Лагос', 13122829),
    (18, 'Манила', 12946263),
    (19, 'Рио-де-Жанейро', 12902306),
    (20, 'Гуанджоу', 12458130)
)

class RadioButtonMenu:
    def __init__(self, close_after_selection: bool = True):
        self.choice = 1

        self.root = tkinter.Tk()
        self.root.title('База данных населения')

        self.frame = Frame(self.root, padding=(10, 5, 10, 5), relief='groove')
        self.frame.grid(padx=5, pady=5, sticky='NSEW', row=0, column=0)
        self.text_frame = Frame(self.root, padding=(10, 5, 10, 5), relief='groove', height=10, width=300)
        self.text_frame.grid(padx=5, pady=5, sticky='NSEW', row=0, column=1)

        self.action_selected = tkinter.IntVar()
        self.action_selected.set(1)
        Radiobutton(self.frame, text='Список по возрастанию численности',
                    variable=self.action_selected, value=1).grid(column=0, row=0, columnspan=2, sticky='w')
        Radiobutton(self.frame, text='Список по убыванию численности',
                    variable=self.action_selected, value=2).grid(column=0, row=1, columnspan=2, sticky='w')
        Radiobutton(self.frame, text='Список по названию',
                    variable=self.action_selected, value=3).grid(column=0, row=2, columnspan=2, sticky='w')
        Radiobutton(self.frame, text='Общая численность',
                    variable=self.action_selected, value=4).grid(column=0, row=3, columnspan=2, sticky='w')
        Radiobutton(self.frame, text='Средняя численность',
                    variable=self.action_selected, value=5).grid(column=0, row=4, columnspan=2, sticky='w')
        Radiobutton(self.frame, text='Наибольшая численность',
                    variable=self.action_selected, value=6).grid(column=0, row=5, columnspan=2, sticky='w')
        Radiobutton(self.frame, text='Наименьшая численность',
                    variable=self.action_selected, value=7).grid(column=0, row=6, columnspan=2, sticky='w')
        Button(self.frame, text='Выбрать', command=self.set_choice).grid(column=0, row=7)
        Button(self.frame, text='Закрыть', command=self.root.destroy).grid(column=1, row=7)

        self.output_text = tkinter.StringVar()
        self.output_text.set('Здесь будет напечатан результат операции ')
        self.output_label = Label(self.text_frame, textvariable=self.output_text)
        self.output_label.grid(column=0, row=0)

        self.root.mainloop()

    def set_choice(self):
        self.choice = self.action_selected.get()

        match self.choice:
            case 1:
                self.print_list_population_asc()
            case 2:
                self.print_list_population_desc()
            case 3:
                self.print_list_names()
            case 4:
                self.print_total()
            case 5:
                self.print_aver()
            case 6:
                self.print_max()
            case 7:
                self.print_min()

    def print_list_population_asc(self):
        with mysql.connector.connect(**CONN_CONFIG) as cnx:
            cur = cnx.cursor()

            stmt_select = "SELECT CityName, Population FROM Cities ORDER BY Population"
            cur.execute(stmt_select)

            output = self.print_request_result(cur.fetchall())
            self.output_text.set(output)

    def print_list_population_desc(self):
        with mysql.connector.connect(**CONN_CONFIG) as cnx:
            cur = cnx.cursor()

            stmt_select = "SELECT CityName, Population FROM Cities ORDER BY Population DESC"
            cur.execute(stmt_select)

            output = self.print_request_result(cur.fetchall())
            self.output_text.set(output)

    def print_list_names(self):
        with mysql.connector.connect(**CONN_CONFIG) as cnx:
            cur = cnx.cursor()

            stmt_select = "SELECT CityName, Population FROM Cities ORDER BY CityName"
            cur.execute(stmt_select)

            output = self.print_request_result(cur.fetchall())
            self.output_text.set(output)

    def print_total(self):
        with mysql.connector.connect(**CONN_CONFIG) as cnx:
            cur = cnx.cursor()

            stmt_select = "SELECT SUM(Population) FROM Cities"
            cur.execute(stmt_select)

            output = f'Общая численность населения:\n'
            output += f'{cur.fetchone()[0]:,}'
            self.output_text.set(output)

    def print_aver(self):
        with mysql.connector.connect(**CONN_CONFIG) as cnx:
            cur = cnx.cursor()

            stmt_select = "SELECT AVG(Population) FROM Cities"
            cur.execute(stmt_select)

            output = f'Средняя численность населения:\n'
            output += f'{cur.fetchone()[0]:,.2f}'
            self.output_text.set(output)

    def print_max(self):
        with mysql.connector.connect(**CONN_CONFIG) as cnx:
            cur = cnx.cursor()

            stmt_select = "SELECT MAX(Population) FROM Cities"
            cur.execute(stmt_select)
            popul = cur.fetchone()
            stmt_select = "SELECT CityName, Population FROM Cities WHERE Population = %s"
            cur.execute(stmt_select, popul)

            output = f'Наибольшая численность населения:\n'
            output += self.print_request_result(cur.fetchall())
            self.output_text.set(output)

    def print_min(self):
        with mysql.connector.connect(**CONN_CONFIG) as cnx:
            cur = cnx.cursor()

            stmt_select = "SELECT MIN(Population) FROM Cities"
            cur.execute(stmt_select)
            popul = cur.fetchone()
            stmt_select = "SELECT CityName, Population FROM Cities WHERE Population = %s"
            cur.execute(stmt_select, popul)

            output = f'Наименьшая численность населения:\n'
            output += self.print_request_result(cur.fetchall())
            self.output_text.set(output)

    def print_request_result(self, request_results: list):
        output = []
        for rec in request_results:
            output.append(f'{rec[0]:<20} - {rec[1]:,}')
        return '\n'.join(output)


def main():
    create_db()
    RadioButtonMenu()

def create_db():
    cnx = None
    try:
        cnx = mysql.connector.connect(**CONN_CONFIG)
        cur = cnx.cursor()

        cur.execute("CREATE DATABASE IF NOT EXISTS Cities_DB")
        cur.execute("USE Cities_DB")

        stmt_drop = "DROP TABLE IF EXISTS cities"
        cur.execute(stmt_drop)

        stmt_create = "CREATE TABLE cities (CityID INT PRIMARY KEY NOT NULL, CityName CHAR(20), Population DECIMAL)"
        cur.execute(stmt_create)

        stmt_insert = "INSERT INTO cities (CityID, CityName, Population) VALUES (%s, %s, %s)"
        cur.executemany(stmt_insert, CITIES)
        cnx.commit()

    except mysql.connector.Error as err:
        print('Ошибка базы данных', err)

    finally:
        if cnx is not None:
            cnx.close()
            CONN_CONFIG['database'] = "Cities_DB"


if __name__ == '__main__':
    main()
