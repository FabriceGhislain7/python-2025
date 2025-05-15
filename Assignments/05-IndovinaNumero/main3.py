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

    
    
