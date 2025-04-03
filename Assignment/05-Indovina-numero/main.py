import random

print("Scegli il livello di difficoltà:")
print("1 - Facile   (1-10, 3 tentativi, -2 punti per errore)")
print("2 - Medio    (1-20, 5 tentativi, -3 punti per errore)")
print("3 - Difficile(1-50, 7 tentativi, -4 punti per errore)")

# Selezione livello
scelta = input("Inserisci il numero del livello (1/2/3): ")

if scelta == "1":
    livello = "Facile"
    limite_superiore = 10
    tentativi_massimi = 3
    penalità = 2
elif scelta == "2":
    livello = "Medio"
    limite_superiore = 20
    tentativi_massimi = 5
    penalità = 3
elif scelta == "3":
    livello = "Difficile"
    limite_superiore = 50
    tentativi_massimi = 7
    penalità = 4
else:
    print("Scelta non valida. Verrà impostato il livello Facile.")
    livello = "Facile"
    limite_superiore = 10
    tentativi_massimi = 3
    penalità = 2

# Imposta il numero da indovinare e punteggio iniziale
numero_casuale = random.randint(1, limite_superiore)
punteggio = 10
tentativi = 0
indovinato = False
storico_tentativi = []

print(f"\nHai scelto il livello: {livello}")
print(f"Indovina un numero tra 1 e {limite_superiore}")
print(f"Hai a disposizione {tentativi_massimi} tentativi.")
print(f"Ogni errore costa {penalità} punti. Parti da 10 punti!")

# Inizio del gioco
while not indovinato and tentativi < tentativi_massimi:
    tentativo = input("\nInserisci un numero: ")

    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    tentativo = int(tentativo)
    storico_tentativi.append(tentativo)
    tentativi += 1

    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        punteggio -= penalità
        if tentativo > numero_casuale:
            print("Troppo alto.")
        else:
            print("Troppo basso.")

        if tentativi < tentativi_massimi:
            print(f"Tentativi rimasti: {tentativi_massimi - tentativi}")
            print("Tentativi precedenti:", storico_tentativi)

# Risultato finale
print("\n=== RISULTATO ===")
if indovinato:
    print(f"Hai indovinato in {tentativi} tentativo/i.")
else:
    print("Game Over! Hai esaurito i tentativi.")
    print(f"Il numero corretto era: {numero_casuale}")

# Evita punteggio negativo
if punteggio < 0:
    punteggio = 0

print(f"Punteggio finale: {punteggio} punti.")
print("Storico dei tuoi tentativi:", storico_tentativi)

# stampare una lista di numeri casuali con join
lista_numeri = [str(num) for num in storico_tentativi]
print("I tuoi tentativi sono:", ", ".join(lista_numeri))