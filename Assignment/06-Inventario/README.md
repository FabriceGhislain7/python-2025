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