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
