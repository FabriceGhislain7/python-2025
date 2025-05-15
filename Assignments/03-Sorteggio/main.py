import random

# Lista dei partecipanti
partecipanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3", "Partecipante 4", "Partecipante 5",
    "Partecipante 6", "Partecipante 7", "Partecipante 8", "Partecipante 9", "Partecipante 10",
]

# Aggiungi i partecipanti 
while True: 
    nuovo = input ("Aggiungi un altro parecipante oppure preni 'INVIO' per termibare ")
    if nuovo == "":
        break
    partecipanti.append(nuovo)

while True:
    random.shuffle(partecipanti)

    # Generiamo le nostre squadre di partecipanti
    squadra1 = []
    squadra2 = []

    # 
    for i in range(len(partecipanti)):
        if i % 2 == 0:
            squadra1.append(partecipanti[i])
        else:
            squadra2.append(partecipanti[i])
    
    
    # stampa con il join
    print(f"\nSquadra 1: {len(squadra1)}: {",".join(squadra1)}")
    print(f"Capitano della Squadra 1: {squadra1[0]}") # Stampa il capitano della squadra 1

    print(f"\nSquadra 2: {len(squadra2)}: {",".join(squadra2)}")
    print(f"Capitano della Squadra 1: {squadra2[0]}") # Stampa il capitano della squadra 2

    risposta = input(f"\nVuoi sorteggiare di nuovo? (si/no): ").lower()
    if risposta != "s":
        break

path_squadra1 = "03-Sorteggio/squadra1.txt" # Percorso del file creato
path_squadra2 = "03-Sorteggio/squadra2.txt" # Percorso del file creato

# Scrivere le squadre in un file di testo
with open(path_squadra1, "w") as file: # w per scrivere (write)
    for partecipante in squadra1:
        file.write(partecipante + "\n") # Aggiunge una nuova riga al file
    
with open(path_squadra2, "w") as file: # w per scrivere (write)
    for partecipante in squadra2:
        file.write(partecipante + "\n") # Aggiunge una nuova riga al file