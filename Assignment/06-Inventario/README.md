# INVENTARIO MAGAZZINO (V 1.0)
## Obiettivo
Gestione di un piccolo inventario con quantità per ogni prodotto

## Implementazione
Crea un dizionario con articoli e quantità.

> Il programma deve permettere di:

1. Visualizzare l'inventario
2. Aggiungere un nuovo articolo
3. Aggiornare la quantita'

```python
inventario = {
    "mele": 10,
    "banane": 5,
    "pere": 8,
    "ciliegie": 15,
    "fragole": 20
}
azione = input("Vuoi [V]edere o [A]ggiornare l'inventario? ")

if azione == "V":
    for prodotto, quantita in inventario.items():
        print(f"{prodotto}: {quantita}")
elif azione == "A":
    prodotto = input("Nome prodotto: ")
    quantita = int(input("Quantità da aggiungere: "))
    if prodotto in inventario:
        inventario[prodotto] += quantita
    else:
        inventario[prodotto] = quantita  # oppure posso fare # inventario.setdefault(prodotto, 0) # inventario[prodotto] += quantita
    # stampa l inventario aggiornato
    print("Inventario aggiornato")
    for prodotto, quantita in inventario.items():
        print(f"{prodotto}: {quantita}")
else:
    print("Azione non valida.")
```
# INVENTARIO MAGAZZINO (V 2.0)
## Obiettivo
Aggiungere il campo prezzo unitario
## Implementazione
Creare un dizionario con articoli e quantità e prezzo unitario dove i valori sono raggruppati in una lista o un dizionario

```python
inventario = {
    "mele": [10, 0.20],
    "banane": [5, 0.15],
    "pere": [8, 0.18],
    "ciliegie": [15, 0.25],
    "fragole": [20, 0.22]
}

azione = input("Vuoi [V]edere o [A]ggiornare l'inventario? ").upper()

if azione == "V":
    for prodotto, dati in inventario.items():
        quantita, prezzo = dati  # dati è una lista con [quantità, prezzo]
        print(f"{prodotto}: {quantita} pezzi - €{prezzo:.2f} ciascuno")  # con .2f stampo il prezzo con 2 decimali

elif azione == "A":
    prodotto = input("Nome prodotto: ").lower()
    quantita = int(input("Quantità da aggiungere: "))
    prezzo_unitario = float(input("Prezzo unitario (€): "))

    if prodotto in inventario:
        inventario[prodotto][0] += quantita  # aggiorna la quantità con [prodotto][0] dove 0 è la quantità
        inventario[prodotto][1] = prezzo_unitario  # sovrascrive il prezzo
    else:
        inventario[prodotto] = [quantita, prezzo_unitario]

    print("Inventario aggiornato:")
    for prodotto, dati in inventario.items():
        quantita, prezzo = dati
        print(f"{prodotto}: {quantita} pezzi - €{prezzo:.2f} ciascuno")

else:
    print("Azione non valida.")
```
# INVENTARIO MAGAZZINO (V 3.0)
## Obiettivo
Implementare una struttura a funzioni
## Implementazione
Creare un dizionario con articoli e quantità e prezzo unitario dove i valori sono raggruppati in una lista o un dizionario

Usare il dizionario come variabile globale

```python
inventario = {
    "mele": [10, 0.20],
    "banane": [5, 0.15],
    "pere": [8, 0.18],
    "ciliegie": [15, 0.25],
    "fragole": [20, 0.22]
}

def vedi_inventario():
    print("\n--- Inventario Attuale ---")
    for prodotto, dati in inventario.items():
        quantita, prezzo = dati
        print(f"{prodotto}: {quantita} pezzi - €{prezzo:.2f} ciascuno")

def aggiorna_inventario():
    prodotto = input("Nome prodotto: ").lower()
    quantita = int(input("Quantità da aggiungere: "))
    prezzo_unitario = float(input("Prezzo unitario (€): "))

    if prodotto in inventario:
        inventario[prodotto][0] += quantita
        inventario[prodotto][1] = prezzo_unitario
    else:
        inventario[prodotto] = [quantita, prezzo_unitario]

    print("\nInventario aggiornato:")
    vedi_inventario()

# Menù principale
azione = input("Vuoi [V]edere o [A]ggiornare l'inventario? ").upper()

if azione == "V":
    vedi_inventario()
elif azione == "A":
    aggiorna_inventario()
else:
    print("Azione non valida.")
```
# INVENTARIO MAGAZZINO (V 4.0)

## Obiettivo
versione con funzioni che ricevono l’inventario come argomento, in modo da evitare variabili globali e rendere il codice più ordinato e riutilizzabile

## Implementazione
- Creare un dizionario con articoli e quantità e prezzo unitario dove i valori sono raggruppati in un dizionario
- Passare l'inventario come argomento alle funzioni
- Se possibile usare il print fuori dalle funzioni

```python
def vedi_inventario(inventario):
    for prodotto, dati in inventario.items():
        quantita, prezzo = dati
        print(f"{prodotto}: {quantita} pezzi - €{prezzo:.2f} ciascuno")

def aggiorna_inventario(inventario):
    prodotto = input("Nome prodotto: ").lower()
    quantita = int(input("Quantità da aggiungere: "))
    prezzo_unitario = float(input("Prezzo unitario (€): "))

    if prodotto in inventario:
        inventario[prodotto][0] += quantita
        inventario[prodotto][1] = prezzo_unitario
    else:
        inventario[prodotto] = [quantita, prezzo_unitario]

# Inventario iniziale
inventario = {
    "mele": [10, 0.20],
    "banane": [5, 0.15],
    "pere": [8, 0.18],
    "ciliegie": [15, 0.25],
    "fragole": [20, 0.22]
}

# Menù principale
azione = input("Vuoi [V]edere o [A]ggiornare l'inventario? ").upper()

if azione == "V":
    print("\n--- Inventario Attuale ---")
    vedi_inventario(inventario)

elif azione == "A":
    aggiorna_inventario(inventario)
    print("\nInventario aggiornato:")
    vedi_inventario(inventario)

else:
    print("Azione non valida.")
```
# INVENTARIO MAGAZZINO (V 5.0)
## Obiettivo
la funzione aggiorna_inventario() riceve tutti i dati come argomenti: prodotto, quantita, prezzo_unitario — invece di chiederli con input() al suo interno

## Implementazione
- Creare un dizionario con articoli e quantità e prezzo unitario dove i valori sono raggruppati in un dizionario
- Passare l'inventario come argomento alle funzioni
- Passare i dati come argomenti alla funzione aggiorna_inventario()
- Se possibile usare il print fuori dalle funzioni

```python

```