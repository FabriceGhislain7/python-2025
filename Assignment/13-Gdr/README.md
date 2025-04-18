# GDR (V 1.0)

## Obiettivi del programma
- Creare un giocco a turni dove due personaggii si scontrano
- Usare funzione in modo da gestire:
- attacco
- turni 
- salute

## Obiettivi didattici 
- Usare funzioni e parametri
```python
import random
def mostra_benvenuto():
    print("Benvenuto ne gioco di combattimento!") 

def crea_personaggio(nome):
    personaggio = {
        "nome": nome,
        "salute": 100, 
        "attacco_min": 10,
        "attacco_max": 20
    }
    return personaggio

# Stamapa il messaggio di benvenuto
nome = input  
```