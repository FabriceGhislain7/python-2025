import random

# Il computer genera un numero casuale tra 1 e 10
numero_casuale = random.randint(1, 10)

indovinato = False  # Flag per indicare se l'utente ha indovinato

# Continua a chiedere finché l'utente non indovina
while not indovinato:
    # Input utente
    tentativo = input("Inserisci un numero: ")
    
    # Verifica che l'input sia un numero
    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue # Salta il resto del ciclo e ricomincia

    tentativo = int(tentativo)

    # Confronto
    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        print("Sbagliato! Riprova.")