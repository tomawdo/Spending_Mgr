from connect_db import connessione_db # richiamo la connessione al db

# Chiamata alla funzione per ottenere la connessione
connessione = connessione_db()

# Usa la connessione per creare un cursore ed eseguire query
cursor = connessione.cursor() # essenziale la funzione cursor
'''
sql = "INSERT INTO categorie (nome, flusso) VALUES (%s, %s)"
values = [
    ("Tasse", "Uscita"),
    ("Svago", "Uscita"),
    ("Regali", "Uscita"),
    ("Alimentare", "Uscita")
    ]
'''
sql = "INSERT INTO categorie (nome, flusso) VALUES (%s, %s)"
values = ("Subscription", "Uscita")
cursor.execute(sql, values) # execute esegue inserimento singolo
# cursor.executemany(sql, values) # executemany esegue inserimento multiplo (tuple)

connessione.commit()

print(f"ultimo id inserito: {cursor.lastrowid}") # cursor last row id accede all'ultimo id