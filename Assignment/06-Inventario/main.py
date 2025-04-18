# Funzione che aggiunge.
def vedi_inventario(input_inventario):
    """_summary_
    Questa funzione ha per scopo di prendere in ingresso un l'inventario sotto forma di dizionario e lo stampa in chiavi valori

    Args:
        input_inventario (_type_): dizionario
    """
    print("\nInventario del magazzino aggiornato:")
    print("articolo: quantità, prezzo unitario in euro")
    print("-" * 50)
    for articolo, caratteristiche in input_inventario.items():
        print(f"{articolo}: {caratteristiche[0]}, {caratteristiche[1]}")

def modifica_articolo(input_dizionario):
    """_summary_ la funzione prende come argomento un dizionario(inventario da aggiornare), 
    e di seguito chiede all'utente d'inserire l'articolo da aggiornare (nome, quantità, prezzo).
    e infine aggiorna il dizionario inserito come argomento.

    Args:
        input_dizionario (_dict_): dizionario(inventario) da aggiornare.
    """
    articolo_modificato = input("Inserisci il nome del nuovo articolo: ").lower()
    if articolo_modificato != "":
        quantita_nuovo_articolo = int(input(f"Inserisci la quantità dell'articolo  '{articolo_modificato}' inseriro: "))
        prezzo_nuovo_articolo = float(input(f"Inserisci il prezzo unitario dell'articolo '{articolo_modificato}' inserito: "))

        if articolo_modificato in input_dizionario.keys():
            quantita_nuovo_articolo += input_dizionario[articolo_modificato][0]
            prezzo_nuovo_articolo = input_dizionario[articolo_modificato][1]
            magazino[articolo_modificato] = [quantita_nuovo_articolo, prezzo_nuovo_articolo]
            print(f"Articolo {articolo_modificato} aggiunto e aggiornato con successo. Quantità: {quantita_nuovo_articolo}, prezzo {prezzo_nuovo_articolo}")
        else:
            print("Articolo non presente nell'inventario")

def aggiungi_articolo(input_dizionario):
    """_summary_La funzione prende come argomento un dizionario all'interno del quale viene inserito un nuovo articolo.

    Args:
        input_dizionario (_dict_): Dizionario mel quale viene inserito un nuovo articolo.
    """
    nuovo_articolo = input("Inserisci il nome del nuovo articolo: ").lower()
    if nuovo_articolo in input_dizionario:
        print("Articolo già presente nel magazino.")
    elif nuovo_articolo == "":
        print("Non si può inserire un articolo senza nomi")
    elif not nuovo_articolo in input_dizionario.keys():
        quantita_nuovo_articolo = int(input(f"Inserisci la quantità dell'articolo '{nuovo_articolo}' inseriro: "))
        prezzo_nuovo_articolo = float(input(f"Inserisci il prezzo unitario dell'articolo '{nuovo_articolo}' inserito: "))
        input_dizionario[nuovo_articolo] = [quantita_nuovo_articolo, prezzo_nuovo_articolo]
        print(f"Articolo aggiornato con successo")
        print(f"Articolo: {nuovo_articolo}: Quantità: {quantita_nuovo_articolo}, Prezzo: {prezzo_nuovo_articolo}")
    else:
        print("Inserimento invalido.")

def aggiorna_inventario(input_dizionario, input_articolo, input_quantita, input_prezzo):
    if input_articolo != "":
        if input_quantita.isdigit() and input_prezzo.isdigit():
            if input_articolo in input_dizionario.keys():
                input_quantita += input_dizionario[input_articolo][0]
                input_dizionario[input_articolo] = [input_quantita, input_prezzo]
                print("Dizionario aggiornato con successo.")
                return input_dizionario
            else:
                print("Aggiornamento non valido")
        else:
            print("La quantità inserita deve essere un numero")
    else:
        print("L'articolo deve avere un nome.")


# Use case
magazino = {
    "mele": [10, 2],
    "banane": [5, 0.2],
    "arance": [8, 0.9],
    "pere": [12, 4],
    "fragole": [15, 0.5]
}

# vedi_inventario(magazino)
aggiungi_articolo(magazino)