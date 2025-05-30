import random
import os

FILE_SALVATAGGIO = "punteggio_calcolatrice.txt"
MAX_OPERAZIONI = 10

# Menu iniziale
print("1. Nuova partita")
print("2. Continua partita")
print("3. Visualizza punteggio salvato")
scelta = input("Seleziona un'opzione (1/2/3): ").strip()

# Inizializza variabili
punteggio = 0  # punteggio iniziale
progressi = 0  # operazioni fatte

# Se l'utente vuole vedere il punteggio salvato
if scelta == "3":
    if os.path.exists(FILE_SALVATAGGIO):
        with open(FILE_SALVATAGGIO, "r", encoding="utf-8") as file:
            contenuto = file.read()
            print("\nStato partita salvato:")
            print(contenuto)
    else:
        print("Nessuna partita salvata trovata.")
    exit()

# Se vuole continuare
if scelta == "2":
    if os.path.exists(FILE_SALVATAGGIO):
        with open(FILE_SALVATAGGIO, "r", encoding="utf-8") as file:
            righe = file.readlines()
            for riga in righe:
                if "progressi" in riga:
                    progressi = int(riga.strip().split(":")[1])
                elif "punteggio" in riga:
                    punteggio = int(riga.strip().split(":")[1])
        print(f"\nRiprendiamo da dove eravamo: {progressi}/10 operazioni fatte, punteggio attuale: {punteggio}\n")
    else:
        print("Nessuna partita salvata trovata, si parte da zero.\n")

# Altrimenti nuova partita (scelta == "1" o default)
if scelta == "1":
    punteggio = 0
    progressi = 0
    # Sovrascrivi file
    with open(FILE_SALVATAGGIO, "w", encoding="utf-8") as file:
        file.write("progressi: 0\npunteggio: 0\n")

# Operazioni disponibili
operazioni = ["+", "-", "*", "/"]

# Gioco principale
while progressi < MAX_OPERAZIONI:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operazione = random.choice(operazioni)

    # Assicura che la divisione sia valida
    if operazione == "/":
        b = random.randint(1, 10)
        a = a * b  # per avere un risultato intero cioe se esce 3/2 il risultato non è intero quindi moltiplico il 3 per 2 in modo che il risultato sia intero

    print(f"Quanto fa: {a} {operazione} {b}?")


    if operazione == "+":
        risultato_corretto = a + b
    elif operazione == "-":
        risultato_corretto = a - b
    elif operazione == "*":
        risultato_corretto = a * b
    elif operazione == "/":
        risultato_corretto = a // b
    else:
        raise ValueError("Operazione non valida.")

    risposta = input("Risposta: ").strip()
    if risposta.lstrip('-').isdigit():  # Controlla se è un numero intero positivo o negativo lstrip('-') serve a rimuovere il segno meno se presente
        risposta_num = int(risposta)  # Converte la risposta in un numero intero
        if risposta_num == risultato_corretto:
            print("Corretto! +1 punto.\n")
            punteggio += 1
        else:
            print(f"Sbagliato! La risposta era {risultato_corretto}. -1 punto.\n")
            punteggio -= 1
    else:
        print(f"Risposta non valida. Era richiesto un numero intero. -1 punto.\n")
        punteggio -= 1

    # Incrementa progressi e salva su file
    progressi += 1
    with open(FILE_SALVATAGGIO, "w", encoding="utf-8") as file:
        file.write(f"progressi: {progressi}\n")
        file.write(f"punteggio: {punteggio}\n")

# Fine partita
print("Hai completato tutte le 10 operazioni!")
print(f"Punteggio finale: {punteggio}/10")

# Reset file
os.remove(FILE_SALVATAGGIO)
print("Partita terminata. Salvataggio eliminato.")