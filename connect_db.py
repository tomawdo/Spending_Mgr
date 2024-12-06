import pymysql

def create_db_connection():
    return pymysql.connect(
        host="localhost",
        port=8889,
        user="root",
        passwd="root",
        database="SELECTION_DB"
    )

def show_tables():
    connection = create_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print(tables)
    connection.close()


show_tables()