import sqlite3

def main():
    conn = sqlite3.connect('tysql.sqlite')
    cur = conn.cursor()

    par = ("%toy%",)
    req = '''SELECT * FROM Products WHERE prod_desc LIKE ? '''
    cur.execute(req, par)
    result = cur.fetchall()

    print(*result, sep='\n')

    conn.close()


if __name__ == '__main__':
    main()
