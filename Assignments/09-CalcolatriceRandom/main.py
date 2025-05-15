import random
import os

path_registro_punteggio = "registro_punteggio.txt"
if not os.path.exists(path_registro_punteggio):
    with open(path_registro_punteggio, "w") as file:
        file.write("NUMERO OPERAZIONI: 10\n")
        file.write("tentativo: 0\n")
        file.write("punteggio: 0\n")

j = 0
with open(path_registro_punteggio, "r") as file:
    for line in file:
        j += 1
        if j == 1:
            NUMERO_OPERAZIONI = line.strip()
        if j == 2:
            tentativo = line.strip()
        if j == 3:
            punteggio = line.strip()

NUMERO_OPERAZIONI = int(NUMERO_OPERAZIONI[-2:].strip())
tentativo = int(tentativo[-2:].strip())
print(punteggio)
punteggio = int(punteggio[-2:].strip())

if tentativo == 0:
    print("Inizio della partita.")

while NUMERO_OPERAZIONI != 0:
    tentativo += 1
    numero1 = random.randint(1, 20)
    numero2 = random.randint(1, 20)
    operatori = ["+", "-", "*", "/"]
    random.shuffle(operatori)

    operatore_casuale = operatori[0]

    if operatore_casuale == "+":
        operazione = numero1 + numero2
    elif operatore_casuale == "-":
        operazione = numero1 - numero2
    elif operatore_casuale == "*":
        operazione = numero1 * numero2
    else:
        operazione = numero1/numero2


    print("Trova il risultato dell'operazione")
    print(f"Risposta giusta: {operazione}")
    print(f"operazione n° {tentativo}")
    risultato_utente = input(f"{numero1} {operatore_casuale} {numero2} = ")

    if operatore_casuale == "/" and numero2 == 0:
        continue

    if float(risultato_utente) == float(operazione):
        print("Risposta corretta.\n")
        punteggio += 1

    elif not risultato_utente.isdigit() :
        punteggio -= 1
        print("Risposta errata.\n")
    else:
        print("Risposta errata.\n")
        punteggio -= 1

    with open(path_registro_punteggio, "w") as file:
        file.write(f"NUMERO OPERAZIONI: {NUMERO_OPERAZIONI}\n")
        file.write(f"tentativo: {tentativo}\n")
        file.write(f"punteggio: {punteggio}\n")

    print("Desideri continuare la partita?")
    scelta_utente = input("Premi 's' per continuare o un'altro tasto per uscire: ")

    if scelta_utente == "s":
        continue
    else:
        break

if tentativo < NUMERO_OPERAZIONI:
    print("La partita non è finita.")
    print(f"Punteggio attuale: {punteggio}")
else: 
    print(f"Fine della partita.")
    print(f"Punteggio finale: {punteggio}")



