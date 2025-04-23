import random

partecipanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3",
    "Partecipante 4", "Partecipante 5", "Partecipante 6",
    "Partecipante 7", "Partecipante 8", "Partecipante 9",
    "Partecipante 10", "Partecipante 11"
]

# Aggiunta partecipanti extra
while True:
    nuovo = input("Aggiungi un partecipante (o premi INVIO per terminare): ")
    if nuovo == "":
        break
    partecipanti.append(nuovo)

# Ciclo per sorteggi multipli
while True:
    random.shuffle(partecipanti)

    squadra1 = [] # lista vuota per la squadra 1
    squadra2 = [] # lista vuota per la squadra 2

    for i in range(len(partecipanti)):
        if i % 2 == 0:
            squadra1.append(partecipanti[i])
        else:
            squadra2.append(partecipanti[i])

    print(f"\nSquadra 1 ({len(squadra1)}): {', '.join(squadra1)}")
    print(f"Capitano Squadra 1: {squadra1[0]}") # stampo il capitano della squadra 1
    
    print(f"\nSquadra 2 ({len(squadra2)}): {', '.join(squadra2)}")
    print(f"Capitano Squadra 2: {squadra2[0]}") # stampo il capitano della squadra 2
    
    # salva le squadre in due files di testo
    with open("squadra1.txt", "w") as file1:
        file1.write(f"Squadra 1 ({len(squadra1)}): {', '.join(squadra1)}\n")
        file1.write(f"Capitano Squadra 1: {squadra1[0]}\n")
    with open("squadra2.txt", "w") as file2:
        file2.write(f"Squadra 2 ({len(squadra2)}): {', '.join(squadra2)}\n")
        file2.write(f"Capitano Squadra 2: {squadra2[0]}\n")
    # Stampa il risultato
    print("\nSquadre salvate nei file 'squadra1.txt' e 'squadra2.txt'.")

    # Chiedi se si vuole sorteggiare di nuovo
    risposta = input("\nVuoi sorteggiare di nuovo? (s/n): ").lower()
    if risposta != "s":
        break
