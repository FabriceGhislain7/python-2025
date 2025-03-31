import random

# Il computer genera un numero casuale tra 1 e 10
numero_casuale = random.randint(1, 10)

indovinato = False      # Flag per indicare se l'utente ha indovinato
tentativi = 0           # Contatore dei tentativi effettuati
tentativi_massimi = 3   # 
punteggio = 10          # Punteggio iniziale
penalità = 2            # Punti persi ad ogni errore

print("Benvenuto! Hai 3 tentativi per indovinare il numero tra 1 e 10.")
print("Inizi con 10 punti. Ogni errore ti costa 2 punti.")

while not indovinato and tentativi < tentativi_massimi:
    tentativo = input("Inserisci un numero: ")

    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    tentativo = int(tentativo)
    tentativi += 1

    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        punteggio -= penalità
        if tentativo > numero_casuale:
            print("Il numero è troppo alto.")
        else:
            print("Il numero è troppo basso.")

        if tentativi < tentativi_massimi:
            print("Sbagliato! Tentativi rimasti:", tentativi_massimi - tentativi)

if indovinato:
    print(f"Hai impiegato {tentativi} tentativo/i.")
    print(f"Il tuo punteggio finale è: {punteggio} punti.")
else:
    print("Game Over! Hai esaurito i tentativi.")
    print(f"Il numero corretto era: {numero_casuale}")
    print(f"Il tuo punteggio finale è: {punteggio} punti.")