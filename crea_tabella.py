from connect_db import connessione_db # richiamo la connessione al db

# Chiamata alla funzione per ottenere la connessione
connessione = connessione_db()

# Usa la connessione per creare un cursore ed eseguire query
cursor = connessione.cursor() # essenziale la funzione cursor

#cursor.execute("CREATE TABLE categorie (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))") # Esecuzione della query
cursor.execute("SHOW TABLES") # eseguo la query

for t in cursor:
    print(t)

# Chiusura della connessione
cursor.close()
connessione.close()
