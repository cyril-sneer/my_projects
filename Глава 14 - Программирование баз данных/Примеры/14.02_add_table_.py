import sqlite3

def main():
    # Подсоединиться к базе данных.
    with sqlite3.connect('inventory.db') as conn:

        # Получить курсор.
        cur = conn.cursor()

        # Добавить таблицу Inventory.
        cur.execute('''CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL,
                                               ItemName TEXT,
                                               Price REAL)''')

        # Зафиксировать изменения.
        conn.commit()

    # # Закрыть соединение.
    # conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()