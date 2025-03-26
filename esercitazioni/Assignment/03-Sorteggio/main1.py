partecipaanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3", "Partecipante 4", "Partecipante 5",
    "Partecipante 6", "Partecipante 7", "Partecipante 8", "Partecipante 9", "Partecipante 10",
]

# Generiamo le nostre squadre di partecipanti
squadra1 = []
squadra2 = []

for i in range(len(partecipaanti)):
    if i % 2 == 0:
        squadra1.append(partecipaanti[i])
    else:
        squadra2.append(partecipaanti[i])

# stampa con il join
print(f"Squadra 1: {",".join(squadra1)}")
print(f"Squadra 1: {",".join(squadra1)}")




# Stampa con il for 
print("Squadra 1:")
for nome in squadra1:
    print(nome)
print("Squadra 2:")
for nome in squadra2:
    print(nome)

# stampa con il join
print("Squadra 1:")
print(",".join(squadra1))
print("Squadra 2:")
print(",".join(squadra2))





