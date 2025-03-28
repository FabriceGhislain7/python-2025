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

