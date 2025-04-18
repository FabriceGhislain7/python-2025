# GDR Obiettivi didattici
- Usare funzioni con parametri e valori di ritorno
- Simulare cicli di gioco
- Gestire l'input dell'utente
- Gestire errori
- Gestire la letture e scrittura su file json

# V 1.0
## Obiettivi del programma
- Creare un gioco a turni dove due personaggi si scontrano
- Usare funzioni in modo da gestire:
- attacco
- turni
- salute

## Funzioni principali
- Funzione: stampa un messaggio di benvenuto
- Funzione: crea un personaggio con le seguenti caratteristiche:
```json
{
    "nome": "Nome del personaggio",
    "salute": 100,
    "attacco_min": 10,
    "attacco_max": 20
}
```
- Funzione: esegue un attacco
- Funzione: controlla se qualcuno è sconfitto
- Funziome principale: gestisce il ciclo di gioco

```python
import random

# Funzione senza parametri: stampa un messaggio di benvenuto
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")  # Non prende input, non restituisce nulla. Serve solo a stampare testo

# Funzione con parametri: crea un personaggio
def crea_personaggio(nome):  # restituisce un dizionario
    personaggio = {
        "nome": nome,
        "salute": 100,
        "attacco_min": 10,
        "attacco_max": 20
    }
    return personaggio

# Funzione con parametri: esegue un attacco
def esegui_attacco(attaccante, difensore):  # prende due personaggi
    danno = random.randint(attaccante["attacco_min"],attaccante["attacco_max"])  # sceglie un numero casuale tra attacco_min ed attacco_max
    difensore["salute"] -= danno  # sottrae il danno alla salute dell altro personaggio
    # stampo il messaggio di attacco
    print(f"{attaccante['nome']} attacca {difensore['nome']} e infligge {danno} danni!")  # stampa il messaggio di attacco
    # Se la salute scende sotto 0, la riportiamo a zero
    if difensore["salute"] < 0:
        difensore["salute"] = 0
    # stampo la salute del difensore
    print(f"{difensore['nome']} ha {difensore['salute']} punti salute rimasti.")  # stampa la salute del difensore

# Funzione con parametri: controlla se qualcuno è sconfitto
def personaggio_sconfitto(personaggio):  # prende il personaggio
    # ritorna un valore booleano
    return personaggio["salute"] <= 0  # controlla se la salute è zero

# stampo il messaggio di benvenuto
mostra_benvenuto()

# provo la funzione di creazione del personaggio
nome = input("Inserisci il nome del tuo personaggio: ")
personaggio = crea_personaggio(nome)
# stampo il personaggio
print(f"Personaggio creato: {personaggio['nome']}, Salute: {personaggio['salute']}, Attacco min: {personaggio['attacco_min']}, Attacco max: {personaggio['attacco_max']}")

# creo due personaggi dummy
giocatore = crea_personaggio("Personaggio amico")
nemico = crea_personaggio("Nemico")

#stampo i personaggi
print(giocatore)
print(nemico)
# oppure lo stampo formattato
print(f"Personaggio amico: {giocatore['nome']}, Salute: {giocatore['salute']}, Attacco min: {giocatore['attacco_min']}, Attacco max: {giocatore['attacco_max']}")
print(f"Nemico: {nemico['nome']}, Salute: {nemico['salute']}, Attacco min: {nemico['attacco_min']}, Attacco max: {nemico['attacco_max']}")

# stampo il messaggio di inizio combattimento
print("Inizia il combattimento!")

# provo la funzione attacco
esegui_attacco(giocatore, nemico)
esegui_attacco(nemico, giocatore)

# provo personaggio sconfitto
if personaggio_sconfitto(nemico):
    print(f"{nemico['nome']} è sconfitto!")
else:
    print(f"{nemico['nome']} è ancora in piedi!")

if personaggio_sconfitto(giocatore):
    print(f"{giocatore['nome']} è sconfitto!")
else:
    print(f"{giocatore['nome']} è ancora in piedi!")
```