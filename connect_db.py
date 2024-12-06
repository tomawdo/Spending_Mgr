import pymysql

def connessione_db():
    return pymysql.connect(
        host="localhost",
        port=8889,
        user="root",
        passwd="root",
        database="PySQL"
    )