import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    req = '''SELECT RowID FROM Products'''
    cur.execute(req)
    result = cur.fetchall()

    print(*result, sep='\n')

    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()