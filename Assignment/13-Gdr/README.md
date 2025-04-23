# GDR Obiettivi didattici
- Usare funzioni con parametri e valori di ritorno
- Simulare cicli di gioco
- Gestire l'input dell'utente
- Gestire errori
- Gestire la letture e scrittura su file json

FASE | Argomento Python | Implementazione nel gioco
---|---|---
1 | Funzioni | Struttura modulare con def
2 | Parametri e ritorni (return) | crea_personaggio(nome) restituisce un dizionario
3 | Dizionari | Gestione di salute, attacco, nome
4 | Condizioni (if, else) | Controllo della salute per capire se qualcuno ha perso
5 | Cicli (while) | Turni di combattimento
6 | Import di librerie (import random) | Generare danni casuali
7 | List comprehension | Inventario o log dei danni subiti
8 | Classi e oggetti (class) | Trasformare personaggio da dict a oggetto
9 | File (open, read, write) | Salvare e caricare le partite attraverso una classe 
10 | Gestione errori (try, except) | Input dell'utente attraverso una classe

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
# V 2.0
## Obiettivi del programma
- Inserire la logica di gioco proncipale (il loop nel quale avviene il duello) all interno di una funzione specifica
- Creare il blocco main() per eseguire la logica di gioco principale

## Descrizione della logica di gioco
- Il giocatore attacca (incomincia il turno)
- Si controlla se il nemico è sconfitto
- Il secondo personaggio attacca
- Si controlla se il giocatore è sconfitto
- Si ripete finché uno dei due ha salute = 0
```python
def gioca_duello():
    # stampo il messaggio di benvenuto
    mostra_benvenuto()

    # Creiamo i personaggi
    giocatore = crea_personaggio("Personaggio Principale")
    nemico = crea_personaggio("Nemico")

    # definiamo un contatore per i turni
    turno = 1

     # Ciclo finché qualcuno perde (quando la salute è zero)
    while True:
        print(f"Turno {turno}:")

        # Attacco del giocatore
        esegui_attacco(giocatore, nemico)

        # controlla se il nemico è sconfitto
        if personaggio_sconfitto(nemico):
            print("Hai vinto il duello!")
            break  # esci dal ciclo nel caso di vittoria

        # Attacco del nemico
        esegui_attacco(nemico, giocatore)

        # controlla se il giocatore è sconfitto
        if personaggio_sconfitto(giocatore):
            print("Sei stato sconfitto!") 
            break # esci dal ciclo nel caso di sconfitta

        # incremento il contatore dei turni
        turno += 1

# punto di ingresso
def main():
    gioca_duello()

# Esegui il gioco
if __name__ == "__main__":
    main()
```
# V 3.0
## Obiettivi del programma
- Implementare una lista che memorizza quanti danni ogni personaggio subisce turno dopo turno

Modifica la funzione crea_personaggio così:

```python
def crea_personaggio(nome):
    return {
        "nome": nome,
        "salute": 100,
        "attacco_min": 10,
        "attacco_max": 20,
        "storico_danni_subiti": []  # <--- nuova lista
         }
```
- Aggiorna la funzione esegui_attacco da così:
```python
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
```
A così:
```python
def esegui_attacco(attaccante, difensore):  # prende due personaggi
    danno = random.randint(attaccante["attacco_min"],attaccante["attacco_max"])
    difensore["salute"] -= danno
    difensore["storico_danni_subiti"].append(danno)  # <--- salviamo il danno
    print(f"{attaccante['nome']} attacca {difensore['nome']} e infligge {danno} danni!")
    if difensore["salute"] < 0:
        difensore["salute"] = 0
    print(f"{difensore['nome']} ha {difensore['salute']} punti salute rimasti.")
```
- stampare lo storico dei danni subiti da ogni personaggio:
```python
print("Storico danni subiti dal nemico:", nemico["storico_danni_subiti"])
print("Storico danni subiti dal giocatore:", giocatore["storico_danni_subiti"])
```
# V 4.0
## Obiettivi del programma
- usare le comprehensions (list comprehensions) in modo da creare più personaggi in un modo compatto

Senza list comprehension:
```python
nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
nemici = []
for nome in nomi_nemici:
    nemici.append(crea_personaggio(nome))
print(nemici)
```
Con list comprehension:
```python
nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
nemici = [crea_personaggio(nome) for nome in nomi_nemici]
print(nemici)
```
Aggiorna la funzione gioca_duello da così:
```python
# Creiamo i personaggi
giocatore = crea_personaggio("Personaggio Principale")
nemico = crea_personaggio("Nemico")
```
A così:
```python
# Creazione del giocatore
giocatore = crea_personaggio("Personaggio Principale")

# Creazione di più nemici
nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
nemici = [crea_personaggio(nome) for nome in nomi_nemici]

# Scegliamo il primo nemico per iniziare il duello
nemico = nemici[0]

# Oppure scelgo casualmente un nemico
nemico = random.choice(nemici)
```
# V 4.0
## Obiettivi del programma
- Modificare il valore di attacco tra 5 e 35
- Implementare il passaggio al prossimo nemico se il primo viene sconfitto
- Se perde, il gioco finisce

## Funzionalita del torneo
- Il giocatore inizia con 100 di salute come il nemico
- Se il giocatore vince, affronta il prossimo nemico
- Se perde, finisce il gioco
- Alla fine viene mostrato un riepilogo del torneo con l elenco dei nemici sconfitti dal giocatore (sia il numero che i nomi)
```python
def gioca_duello():
    # stampo il messaggio di benvenuto
    mostra_benvenuto()

    # Creazione del giocatore
    giocatore = crea_personaggio("Personaggio Principale")

    # Creazione di più nemici
    nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
    nemici = [crea_personaggio(nome) for nome in nomi_nemici]

    # Faccio lo shuffle dei nemici
    random.shuffle(nemici)
    
    # Statistiche torneo
    nemici_sconfitti = 0
    
    # Loop sul torneo: un nemico alla volta
    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico['nome']}")
        
        # definiamo un contatore per i turni
        turno = 1

        # Ciclo finché qualcuno perde (quando la salute è zero)
        while True:
            print(f"Turno {turno}:")

            # Attacco del giocatore
            esegui_attacco(giocatore, nemico)
            
            # stampo lo storico dei danni subiti dal nemico
            print("Storico danni subiti dal nemico:", nemico["storico_danni_subiti"])

            # controlla se il nemico è sconfitto
            if personaggio_sconfitto(nemico):
                print(f"Hai vinto il duello contro {nemico['nome']}!")
                
                # incrementa il contatore dei nemici sconfitti
                nemici_sconfitti += 1
                
                break  # Passa al prossimo nemico

            # Attacco del nemico
            esegui_attacco(nemico, giocatore)
            
            # stampo lo storico dei danni subiti dal giocatore
            print("Storico danni subiti dal giocatore:", giocatore["storico_danni_subiti"])

            # controlla se il giocatore è sconfitto
            if personaggio_sconfitto(giocatore):
                print("Sei stato sconfitto!") 
                
                # stampa quanti nemici hai sconfitto
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")
                
                # break → il ciclo continua dopo la sconfitta
                return # esci dalla funzione nel caso di sconfitta

            # incremento il contatore dei turni
            turno += 1
            
    # Se il giocatore ha sconfitto tutti
    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")
```
# V 5.0
## Obiettivi del programma
- Implementare funzionalità di recupero salute tra un nemico e l'altro
- Dopo ogni vittoria il giocatore recupera una percentuale fissa di salute che gli è rimasta (30%)
- Se la salute è maggiore di 100, la riporto a 100
- Dopo ogni nemico sconfitto, il giocatore recupera salute e stampiamo un riepilogo della salute attuale
```python
if personaggio_sconfitto(nemico):
    print(f"Hai vinto il duello contro {nemico['nome']}!")
    
    # Recupero salute tra scontri (30)
    percentuale_recupero = 0.3
    salute_recuperata = int(giocatore["salute"] * percentuale_recupero)
    
    # Limitiamo il recupero della salute a 100
    if giocatore["salute"] + salute_recuperata > 100:
        salute_recuperata = 100
        
    # recupero salute
    giocatore["salute"] += salute_recuperata

    # stampo la salute del giocatore
    print(f"\nHai recuperato {salute_recuperata} punti salute! Salute attuale: {giocatore['salute']}")
    
    # incrementa il contatore dei nemici sconfitti
    nemici_sconfitti += 1
    
    break  # Passa al prossimo nemico
```
# V 7.0 
Trasformare il personaggio in una classe (traformare il dizionario in una classe).
Implementare le basi della programmazione orientata agli oggetti(OOP) in modo da:
Creare una classe Personnaggio che rapresenta un personaggio del gioco

## Obiettivi didattici
Capire cosa sono:
- Le classi
- I metodi
- Il costruttore `__init__()`
- L'uso di self
- `__init__()` è il costruttore della classe. Viene eseguito automaticamente quando un oggetto da una classe
- `self`è il riferimento all'istanza attuale dell'oggetto. Ogni volta che chiami un metodo su un oggetto, self rapresenta quel oggetto.

Creazione della classe Personaggio
```python 
class Personaggio:
```
- [x]
- [ ]
- [x]

# V 8.0
Utilizzate i metodi delle classi per gestire un torneo in questo progetto.
 