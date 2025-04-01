# Importare il modulo random
import random

# Numero computer da indoviare
numero_computer = random.randint(1,10)

# Stampo il numero casuale da indovinare generato dal computer solo per controllo.
print(f"numero_computer: {numero_computer}")

# Inizializzazione del contatore 
MASSIMO_TENTATIVI = 3 
punteggio = 10
tentativo = 0 # contatore tentativi inizializzato a 0

print("-" * 40)
print(f"Indovina il numero generato dal computer tra 1 e 10.")
print("Inizi con un punteggio di 10.Ogni tentativo errato comporta una perdita di 2 punti.")
print(f"Hai a disposizione {MASSIMO_TENTATIVI} tentativi.") 


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
