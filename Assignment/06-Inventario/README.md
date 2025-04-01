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