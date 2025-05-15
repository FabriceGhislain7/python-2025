# INDOVINA NUMERO (V 1.0)

## Obiettivo

Creare una applicazione che permetta di indovinare un **numero casuale** generato dal computer.
1. Il computer genera un numero casuale tra 1 e 10.
2. L'utente inserisci un numero.
3. Il computer confronta il numero inserito con quello generato.
4. Se il numero inserito è uguale aquelle generato, l'utente ha indovinato.
5. Il gioco termina quando l'utente indovina il numero.

## Implementazione
 ```python 
# Importare il modulo random
import random

# Numero casuale da indovinare generato dal computer
numero_computer = random.randint(1,10)

# faccio un cilco while finché l'utente non indovona il numero 
while True:
    while True:
        numero_utente = input("Indovina il numero generato dal computer tra 1 e 10, inserendo qui la tua risposta:  ")
        if numero_utente.isdigit():
            break
        else:
            print("Il valore inserito non è valido.")
            continue
        
    # Confronto il numero del computer con quello dell'utente.
    if numero_computer == int(numero_utente):
        print("Bravo, hai indovinato il numero.")
        break
    else:
        print("Il numero inserito non è giusto, riprova.")
        continue

 ```

# INDOVINA NUMERO (V 2.0)

## Obiettivo

Creare una applicazione che permetta di indovinare un **numero casuale** generato dal computer.
1. Il computer genera un numero casuale tra 1 e 10.
2. L'utente inserisci un numero.
3. Il computer confronta il numero inserito con quello generato.
4. Se il numero inserito è uguale a quello generato, l'utente ha indovinato.
5. Se il numero inserito è minore dal numero da indovinare (rispetivamente maggiore da indovinare) 
   stampare un messaggio dicendo che il numero da inserire è più grande.
6. Il gioco termina quando l'utente indovina il numero.


## Implementazione

```python 
# Importare il modulo random
import random

# Numero computer da indoviare
numero_computer = random.randint(1,10)

# Stampo il numero casuale da indovinare generato dal computer solo per controllo.
print(f"numero_computer: {numero_computer}")

# faccio un cilco while finché l'utente non indovona il numero 
while True:
    while True:
        numero_utente = input("Indovina il numero generato dal computer tra 1 e 10, inserendo qui la tua risposta:  ")
        if numero_utente.isdigit():
            break
        else:
            print("Il valore inserito non è valido.")
            continue
        
    # Confronto il numero del computer con quello dell'utente.
    numero_utente = int(numero_utente)
    if numero_computer == numero_utente:
        print("Bravo, hai indovinato il numero.")
        break
    else:
        print("Il numero inserito non è giusto.")
        if numero_utente > numero_computer:
            print(f"Il numero da indovinare è minore di {numero_utente}")
        else:
            print(f"Il numero da indovinare è maggiore di {numero_utente}")
        continue

```

# INDOVINA NUMERO (V 3.0)

## Obiettivo

Creare una applicazione che permetta di indovinare un **numero casuale** generato dal computer.
1. Il computer genera un numero casuale tra 1 e 10.
2. L'utente inserisci un numero.
3. Il computer confronta il numero inserito con quello generato.
4. Se il numero inserito è uguale a quello generato, l'utente ha indovinato e esce dal gioco.
5. Se il numero inserito è minore dal numero da indovinare (rispetivamente maggiore da indovinare) 
   stampare un messaggio dicendo che il numero da inserire è più grande.
6. Il gioco si termina quando l'utente esaurisce il numero massimo di tentativ (3).


## Implementazione
```python 

# Importare il modulo random
import random

# Numero computer da indoviare
numero_computer = random.randint(1,10)

# Stampo il numero casuale da indovinare generato dal computer solo per controllo.
print(f"numero_computer: {numero_computer}")

# Inizializzazione del contatore 
MASSIMO_TENTATIVI = 3 
tentativo = 0

print("Indovina il numero generato dal computer tra 1 e 10.")
print(f"Hai un massimo di {MASSIMO_TENTATIVI} tentativi.")


# faccio un cilco while finché l'utente non indovona il numero 
while True:
    print("-" * 40)
    tentativo += 1    
    if tentativo > MASSIMO_TENTATIVI:
        print(f"Numero di tentativi esaurite. Il numero era {numero_computer}")
        break
    print(f"tentativo : {tentativo}")

    while True:
        numero_utente = input("Inserisci la tua risposta:  ")
        if numero_utente.isdigit():
            break
        else:
            print("Il valore inserito non è valido.")
            continue
        
    # Confronto il numero del computer con quello dell'utente.
    numero_utente = int(numero_utente)

    if numero_computer == numero_utente:
        print("Bravo, hai indovinato il numero.")
        break
    else:
        if numero_utente > numero_computer:
            print(f"Il numero da indovinare è minore di {numero_utente}")
        else:
            print(f"Il numero da indovinare è maggiore di {numero_utente}")
        continue

```

# INDOVINA NUMERO (V 4.0)

## Obiettivo
Questa versione è un aggiornamento della versione precedente con le condizioni aggiuntive seguenti:
1. punteggio iniziale = 10
2. ogni tentativo sbagliato, sostrae 2 punti
3. Alla fine del gioco, mostra il numero di tentativi rimanenti e il punteggio

## Implementazione

```python 

# Importare il modulo random
import random

# Numero computer da indoviare
numero_computer = random.randint(1,10)

# Stampo il numero casuale da indovinare generato dal computer solo per controllo.
print(f"numero_computer: {numero_computer}")

# Inizializzazione del contatore 
MASSIMO_TENTATIVI = 3 
punteggio = 10
tentativo = 0

print("Indovina il numero generato dal computer tra 1 e 10.")
print(f"Hai un massimo di {MASSIMO_TENTATIVI} tentativi.")


# faccio un cilco while finché l'utente non indovona il numero 
while True:
    print("-" * 40)
    tentativo += 1    

    if tentativo > MASSIMO_TENTATIVI:
        print(f"Numero di tentativi esaurite. Il numero era {numero_computer}")
        break
    
    print(f"tentativo: {tentativo}")

    while True:
        numero_utente = input("Inserisci la tua risposta:  ")
        if numero_utente.isdigit():
            break
        else:
            print("Il valore inserito non è valido.")
            continue
        
    # Confronto il numero del computer con quello dell'utente.
    numero_utente = int(numero_utente)

    if numero_computer == numero_utente:
        print("\nBravo, hai indovinato il numero.")
        break
    else:
        punteggio -= 2
        if numero_utente > numero_computer:
            print(f"Il numero da indovinare è minore di {numero_utente}")
        else:
            print(f"Il numero da indovinare è maggiore di {numero_utente}")
        continue

# Stampo il punteggio finale con il numero di tentativi rimanenti.
print(f"\nPunteggio finale: {punteggio}")
print(f"\nNumero di tentativi rimanenti: {MASSIMO_TENTATIVI - tentativo + (1 if tentativo > MASSIMO_TENTATIVI else 0)}")

```
# INVENTARIO MAZZINO (V 5.0)
## Obiettivo


Implemetazione del livello di dificoltà: Permette all'utente di scegliere tra livelli di difficoltà. che modifica il numero di punti sostratti o l'intervallo dei numeri o il numero dei tentativi disponibili.

i livelli di difficoltà potrebberro essere.
 - facile: 1-10, 3 tentativi, 2 punti di penalità.
 - Medio: 1-20, 5 tentativi, 3 punti di penalità
 - Dificile: 1-50, 7 tentativi, 4 punti di penalità.

## Implementazione.

1. Aggiungere un menu per scegliere il livello di difficoltà
2. Modificare il punteggio e i tentativi in base al livello scelta.
2. Modificare l'intervallo dei nuneri in base al livello scelto.
4. Modificare la penalità in base al livello scelto.
5. mostrare il punteggio finale e il numero di tentativi effettuati.

## Codice 
```python 
import random

# Generazione del MENU
menu = {"1":["Facile", (1,10), 3, 2],
        "2":["Medio", (1,20), 5, 3],
        "3":["Difficile",(1,50), 7, 4],
        "4":["Esci", 0, 0, 0]}

# Stampa del MENU
print("MENU:")
print("=" * 40)
for livello, contenuto in menu.items():
    print(f"{livello}: {contenuto[0]}")
    if livello == "4": 
        break
    print(f"Intervallo del numero da indovinare: {contenuto[1]}")
    print(f"Numero di tentativi: {contenuto[2]}")
    print(f"penalità per tentativo errato: {contenuto[3]}")
    print("-" * 10)

# Geszione del valore inserito dall'utente
punteggio = 10
while True:
    scelta = input("Inserisci il nemuro corrispondente al livello desiderato: ").lower()
    if scelta in menu.keys():
        break
    else:
        print("Il valore inserito non è valido.")
        continue

# Gestione della scelta dell'utente
if scelta == "1":
    intervallo = menu["1"][1]
    MASSIMO_TENTATIVI = menu["1"][2]
    penalita = menu["1"][3]
elif scelta == "2":
    intervallo = menu["2"][1]
    MASSIMO_TENTATIVI = menu["2"][2]
    penalita = menu["2"][3]
elif scelta == "3":
    intervallo = menu["3"][1]
    MASSIMO_TENTATIVI = menu["3"][2]
    penalita = menu["3"][3]
else:
    print("Uscita dal programma. Ciao!")
    exit()


numero_computer = random.randint(intervallo[0], intervallo[1]) 
print(f"numero_computer: {numero_computer}")
tentativo = 0 

# faccio un cilco while finché l'utente non indovona il numero 
while True:
    print("-" * 40)
    tentativo += 1    
    if tentativo > MASSIMO_TENTATIVI:
        print(f"Numero di tentativi esaurite. Il numero era {numero_computer}")
        break
    
    print(f"tentativo: {tentativo}")
    while True:
        numero_utente = input("Inserisci la tua risposta:  ")
        if numero_utente.isdigit():
            break
        else:
            print("Il valore inserito non è valido.")
            continue
        
    # Confronto il numero del computer con quello dell'utente.
    numero_utente = int(numero_utente)
    if numero_computer == numero_utente:
        print("\nBravo, hai indovinato il numero.")
        break
    else:
        punteggio -= 2
        if numero_utente > numero_computer:
            print(f"Il numero da indovinare è minore di {numero_utente}")
        else:
            print(f"Il numero da indovinare è maggiore di {numero_utente}")
        continue

# Stampo il punteggio finale con il numero di tentativi rimanenti.
print(f"\nPunteggio finale: {punteggio}")
print(f"\nNumero di tentativi rimanenti: {MASSIMO_TENTATIVI - tentativo + (1 if tentativo > MASSIMO_TENTATIVI else 0)}")

```
# INDOVINA NUMERO (V 6.0)

## Implementazione
- Utilizza una lista per memorizzare le tentativi dell'utente.
- I tentativi sono memorizzati fino a quando l'utente indovina il numero oppure esaurisci le tentativi ma vengono persi quando viene incominciata la partita successiva.

```python
import random

# Generazione del MENU
menu = {"1":["Facile", (1,10), 3, 2],
        "2":["Medio", (1,20), 5, 3],
        "3":["Difficile",(1,50), 7, 4],
        "4":["Esci", 0, 0, 0]}

# Stampa del MENU
print("MENU:")
print("=" * 40)
for livello, contenuto in menu.items():
    print(f"{livello}: {contenuto[0]}")
    if livello == "4": 
        break
    print(f"Intervallo del numero da indovinare: {contenuto[1]}")
    print(f"Numero di tentativi: {contenuto[2]}")
    print(f"penalità per tentativo errato: {contenuto[3]}")
    print("-" * 10)

# Geszione del valore inserito dall'utente
punteggio = 10
while True:
    scelta = input("Inserisci il nemuro corrispondente al livello desiderato: ").strip()
    if scelta in menu.keys():
        break
    else:
        print("Il valore inserito non è valido.")
        continue

# Gestione della scelta dell'utente
if scelta == "1":
    intervallo = menu["1"][1]
    MASSIMO_TENTATIVI = menu["1"][2]
    penalita = menu["1"][3]
elif scelta == "2":
    intervallo = menu["2"][1]
    MASSIMO_TENTATIVI = menu["2"][2]
    penalita = menu["2"][3]
elif scelta == "3":
    intervallo = menu["3"][1]
    MASSIMO_TENTATIVI = menu["3"][2]
    penalita = menu["3"][3]
else:
    print("Uscita dal programma. Ciao!")
    exit()

lista_tentativi = []
numero_computer = random.randint(intervallo[0], intervallo[1]) 
print(f"numero_computer: {numero_computer}")
tentativo = 0 


print("*" * 40)
print(f"{'INIZIO DELLA PARTITA':^40}")
print("*" * 40)



# faccio un cilco while finché l'utente non indovona il numero 
while True:
    tentativo += 1    
    if tentativo > MASSIMO_TENTATIVI:
        print(f"Numero di tentativi esaurite. Il numero era {numero_computer}")
        break
    
    print(f"tentativo: {tentativo}")
    while True:
        numero_utente = input("Inserisci la tua risposta:  ").strip()
        if numero_utente.isdigit():
            break
        else:
            print("Il valore inserito non è valido.")     
            continue
    
    numero_utente = int(numero_utente)    
    
    # Confronto il numero del computer con quello dell'utente.
    if numero_computer == numero_utente:
        print("\nBravo, hai indovinato il numero.")
        break
    else:
        punteggio -= 2
        if numero_utente > numero_computer:
            print(f"Il numero da indovinare è minore di {numero_utente}")
        else:
            print(f"Il numero da indovinare è maggiore di {numero_utente}")
        
        print("-" * 40)

        # Stampare la lista dei tentativi.
        if numero_utente not in lista_tentativi:
            lista_tentativi.append(numero_utente) 
        print(f"Lista dei tentativi sbagliati già effettuati: {lista_tentativi}")    
        continue

# Stampo il punteggio finale con il numero di tentativi rimanenti.
print(f"Punteggio finale: {punteggio}")
print(f"Numero di tentativi rimanenti: {MASSIMO_TENTATIVI - tentativo + (1 if tentativo > MASSIMO_TENTATIVI else 0)}")

```
