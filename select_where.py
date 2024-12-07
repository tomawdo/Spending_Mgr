from connect_db import connessione_db # richiamo la connessione al db

# Chiamata alla funzione per ottenere la connessione
connessione = connessione_db()

# Usa la connessione per creare un cursore ed eseguire query
cursor = connessione.cursor() # essenziale la funzione cursor

sql = "SELECT * FROM categorie WHERE flusso = 'uscita'"
cursor.execute(sql)
result = cursor.fetchall() #selezion tutti i record
#result = cursor.fetchone() # seleziona ultimo record

for riga in result:
    print(riga)