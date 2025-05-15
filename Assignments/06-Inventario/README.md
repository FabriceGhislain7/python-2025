# INVENTARIO MAZZINO (V 1.0)
## Obiettivo

Gestione di un piccolo inventario per quantità per ogni prodotto.

## Implementazione.

Crea un dizionario con articoli e quantità.
> Il programma deve:
1. Visualizzare l'inventario
2. Aggiungere un nuovo articolo.
3. Aggiungere la quantità.

## Codice 
```python 

# Inizializzare il mio dizionario 
prodotti = {
    "mele": 10,
    "banane": 5,
    "arance": 8,
    "pere": 12,
    "fragole": 15
}

print("\nInventario del magazzino")
for articolo, quantita in prodotti.items():
    print(f"{articolo}: {quantita}")

# Inserisco un nuovo prodotto
nuovo_articolo = input("Inserisci il nome del nuovo articolo: ")

# Inserisco la quantita.
if nuovo_articolo != "":
    quantita_nuovo_articolo = int(input("Inserisci la quantità del nuovo articolo: "))
    
    if nuovo_articolo in prodotti.keys():
        quantita_nuovo_articolo = prodotti[nuovo_articolo] + quantita_nuovo_articolo

    # Inserisco il nuovo prodotto nella lista dei prodotti.
    prodotti[nuovo_articolo] = quantita_nuovo_articolo

print("\nInventario magazzino aggiornato:")
for articolo, quantita in prodotti.items():
    print(f"{articolo}: {quantita}")

```
# INVENTARIO MAZZINO (V 2.0)
## Obiettivo

Aggiungere il campo prezzo unitario.

## Implementazione.
Creare un dizionario con articoli e quantità e prezzo unitario.
```python 

# Inizializzare il mio dizionario 
prodotti = {
    "mele": [10, 2],
    "banane": [5, 0.2],
    "arance": [8, 0.9],
    "pere": [12, 4],
    "fragole": [15, 0.5]
}

print("\nInventario del magazzino stampato secondo il modello:")
print("articolo: quantità, prezzo unitario in euro")
print("-" * 50)
for articolo, caratteristiche in prodotti.items():
    print(f"{articolo}: {caratteristiche[0]}, {caratteristiche[1]}")

# Inserisco un nuovo prodotto
print("=" * 50)
nuovo_articolo = input("Inserisci il nome del nuovo articolo: ").lower()

# Inserisco la quantita.
if nuovo_articolo != "":
    print("=" * 50)
    quantita_nuovo_articolo = int(input(f"Inserisci la quantità dell'articolo  '{nuovo_articolo}' inseriro: "))
    
    print("=" * 50)
    prezzo_nuovo_articolo = float(input(f"Inserisci il prezzo unitario dell'articolo '{nuovo_articolo}' inserito: "))
    
    if nuovo_articolo in prodotti.keys():
        quantita_nuovo_articolo += prodotti[nuovo_articolo][0]  
        prezzo_nuovo_articolo = prodotti[nuovo_articolo][1]

    # Inserisco il nuovo prodotto nella lista dei prodotti.
    prodotti[nuovo_articolo] = [quantita_nuovo_articolo, prezzo_nuovo_articolo]

print("\nInventario del magazzino aggiornato:")
print("articolo: quantità, prezzo unitario in euro")
print("-" * 50)  
for articolo, caratteristiche in prodotti.items():
    print(f"{articolo}: {caratteristiche[0]}, {caratteristiche[1]}")

```
# INVENTARIO (V 3.0)
## Obiettivo 
Implementare una struttura a funzioni

## Implementazione 
Creare un dizionario con articoli e quantità e prezzo untario dove i valori sono raggruppati in una lista o un dizionario. 
```python
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

```
