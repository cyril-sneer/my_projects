import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Отправить инструкцию SELECT в СУБД.
    cur.execute('''INSERT INTO Products (Description) VALUES("Coffee")''')
    cur.execute('''SELECT * FROM Products WHERE lower(Description) == "coffee"''')

    # Извлечь результаты инструкции SELECT.
    results = cur.fetchall()

    print(results)

    # Закрыть соединение с базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()