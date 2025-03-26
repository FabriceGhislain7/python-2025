import random

partecipanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3", "Partecipante 4", "Partecipante 5",
    "Partecipante 6", "Partecipante 7", "Partecipante 8", "Partecipante 9", "Partecipante 10", "Partecipante 11"
]

# Mischio i partecipanti per rendere il sorteggio casuale
random.shuffle(partecipanti)

# Creo le liste vuote per le squadre
squadra1 = [] # Creo una lista vuota per la squadra 1
squadra2 = [] # Creo una lista vuota per la squadra 2

# ciclo in modo da assegnare i partecipanti alle squadre in modo alternato
for i in range(len(partecipanti)):
    if i % 2 == 0:  # se il resto della divisione tra i e 2 è 0
        squadra1.append(partecipanti[i]) # aggiungo il partecipante alla squadra 1
    else:
        squadra2.append(partecipanti[i]) # altrimenti aggiugo il partecipante alla squadra 2
        
# stampa con il join (più elegante)
print(f"\nSquadra 1: {', '.join(squadra1)}")
print(f"Squadra 2: {', '.join(squadra2)}")