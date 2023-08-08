import mysql.connector

def main():
    connection_config = {
        "host": "localhost",
        "port": 3306,
        "database": "TYSQL",
        "user": "test_user",
        "password": "12345",
        "charset": "utf8",
        "use_unicode": True,
        "get_warnings": True,
    }

    # conn = mysql.connector.connect(host="localhost", port=3306, database="TYSQL", user="test_user", password="12345")
    conn = mysql.connector.connect(**connection_config)
    cur = conn.cursor()

    par = ("%toy%",)
    req = '''SELECT * FROM Products WHERE prod_desc LIKE %s'''
    cur.execute(req, par)
    result = cur.fetchall()

    print(*result, sep='\n')

    conn.close()


if __name__ == '__main__':
    main()