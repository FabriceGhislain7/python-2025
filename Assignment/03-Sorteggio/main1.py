import random

partecipanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3", "Partecipante 4", "Partecipante 5",
    "Partecipante 6", "Partecipante 7", "Partecipante 8", "Partecipante 9", "Partecipante 10",
]

# Mischiare la lista dei partecipanti per poter fare un sorteggio casuale.
random.shuffle(partecipanti)

# Generiamo le nostre squadre di partecipanti
squadra1 = []
squadra2 = []

j = 0
while len(partecipanti)!= 0:
    print(len(partecipanti))
    # print(f"numero dei partecipanti restanti -> {len(partecipanti)}")
    partecipante_random = random.choice(partecipanti)

    if j % 2 == 0:
        squadra1.append(partecipante_random)
    else: 
        squadra2.append(partecipante_random)

    partecipanti.remove(partecipante_random)
    print(len(partecipanti))


    start = ""
    while True:
        nuovo_partecipante = input("Se c'è un nuovo partecipante, inserisci il suo nome. Altrimenti inserire 'no': ")

       
        if nuovo_partecipante.lower == 'no' or nuovo_partecipante == '':
            print('Nessuno, nuovo partecipante. Premi "INVIO" per procedere al prossimo soreggio: ') 
        else: 
            partecipanti.append(nuovo_partecipante)
        
        start = input("Premi 'INVIO' per procedere al prossimo soreggio: ")

        if start.upper() == 'INVIO':
            break
       
    j += 1

# Fine del sorteggio
print("Fine del sorteggio.")

# Stampa con il for 
print("Squadra 1:")
for nome in squadra1:
    if nome == squadra1[0]:
        print(f"Capitano della Squadra 1: {nome}")
    else:
        print(nome)
print("Squadra 2:")
for nome in squadra2:
    if nome == squadra2[0]:
        print(f"Capitano della Squadra 2: {nome}")
    else:
        print(nome)



# APPROCCIO DELL'INSEGNANTE
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

    # Assegnamo casualmente il partecipante a una delle squadre. 
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




