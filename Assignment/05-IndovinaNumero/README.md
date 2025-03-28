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