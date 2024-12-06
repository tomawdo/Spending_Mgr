import pymysql
from connect_db import connessione_db # richiamo la connessione al db

connessione = connessione_db() # Chiamata alla funzione per ottenere la connessione
cursor = connessione.cursor() # Creazione del cursore dalla connessione

# cursor.execute("CREATE DATABASE PySQL") # Esecuzione della query

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Chiusura della connessione
cursor.close()
connessione.close()
