import datetime
def aggiungi_spesa(spese):
    """
    Aggiunge una nuova spesa alla lista delle spese.

    Args:
        spese (list): La lista che contiene tutte le spese.
    """
    # Step 1: Richiedi la data e valida il formato
    while True:
        data = input("Inserisci la data della spesa (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(data, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato data non valido. Riprova.")

    # Step 2: Richiedi la categoria
    categorie = ["Cibo", "Trasporti", "Intrattenimento", "Altro"]
    print("Categorie disponibili: ", ", ".join(categorie))
    while True:
        categoria = input("Inserisci la categoria: ")
        if categoria in categorie:
            break
        print("Categoria non valida. Scegli tra: ", ", ".join(categorie))

    # Step 3: Richiedi l'importo
    while True:
        try:
            importo = float(input("Inserisci l'importo della spesa: "))
            if importo > 0:
                break
            print("L'importo deve essere maggiore di zero.")
        except ValueError:
            print("Importo non valido. Inserisci un numero.")

    # Step 4: Crea il dizionario e aggiungilo alla lista
    spesa = {"data": data, "categoria": categoria, "importo": importo}
    spese.append(spesa)
    print("Spesa aggiunta con successo!")