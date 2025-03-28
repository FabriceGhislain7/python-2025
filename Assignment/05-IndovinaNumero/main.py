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
