import random  # Importa il modulo random

# Il computer genera un numero casuale tra 1 e 10
numero_casuale = random.randint(1, 10)

indovinato = False  # Flag per indicare se l'utente ha indovinato
tentativi = 0       # Contatore dei tentativi massimi
tentativi_massimi = 3

print("Benvenuto! Hai 3 tentativi per indovinare il numero tra 1 e 10.")

# Continua a chiedere finché l'utente non indovina o finisce i tentativi
while not indovinato and tentativi < tentativi_massimi:
    tentativo = input("Inserisci un numero: ")

    # Verifica che l'input sia un numero
    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    tentativo = int(tentativo)
    tentativi += 1  # Aumenta il contatore dei tentativi

    if tentativo > numero_casuale:
        print("Il numero è troppo alto.")
    elif tentativo < numero_casuale:
        print("Il numero è troppo basso.")
    
    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato in", tentativi, "tentativo/i!")
        indovinato = True
    elif tentativi < tentativi_massimi:
        print("Sbagliato! Tentativi rimasti:", tentativi_massimi - tentativi)
    else:
        print("Game Over! Hai esaurito i tentativi.")
        print("Il numero corretto era:", numero_casuale)