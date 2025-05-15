# Comprehensions
# Si usano quando vuoi trasformare o filtrare elementi in un ciclo
# Sintassi
# [espressione for elemento in collezione if condizione]
# in un unico passaggio:
# creare la variabile con la quale iterare
# effettuare l'operazione
# ciclare su ogni elemento della collezione
# aggiunta dell elemento alla collezione appena creata
# e filtrare gli elementi che non ci interessano

# List Comprehensions

# Esempio 1: Creare una lista di quadrati con comprehensions
quadrati = [q**2 for q in range(5)]
print(quadrati)  # Output: [0, 1, 4, 9, 16]
# senza comprehensions
numeri = [1, 2, 3, 4, 5]
quadrati = []
for numero in numeri:
    quadrati.append(numero ** 2)
print(quadrati)  # Output: [1, 4, 9, 16, 25]

# Esempio 2: Creare una lista di numeri pari con comprehensions
pari = [p for p in range(10) if p % 2 == 0]
print(pari)  # Output: [0, 2, 4, 6, 8]
# senza comprehensions
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = []
for numero in numeri:
    if numero % 2 == 0:
        pari.append(numero)
print(pari)  # Output: [2, 4, 6, 8]

# Esempio 3: trasformare stringhe
nomi = ["Nome1", "nome2", "Nome3"]
puliti = [n.lower() for n in nomi]
print(puliti)  # Output: ['nome1', 'nome2', 'nome3']
# senza comprehensions
nomi = ["Nome1", "nome2", "Nome3"]
puliti = []
for nome in nomi:
    puliti.append(nome.lower())
print(puliti)  # Output: ['nome1', 'nome2', 'nome3']

# Esempio 4: Creare o trasformare dizionari in una sola riga
nomi = ["nome1", "nome2", "nome3"]
lunghezze = {n: len(n) for n in nomi}
print(lunghezze)  # Output: {'nome1': 5, 'nome2': 5, 'nome3': 5}
# senza comprehensions
nomi = ["nome1", "nome2", "nome3"]
lunghezze = {}
for nome in nomi:
    lunghezze[nome] = len(nome)
print(lunghezze)  # Output: {'nome1': 5, 'nome2': 5, 'nome3': 5}

# Esempio 5: Creare un set personalizzato
caratteri = {c for c in "frutta"}
print(caratteri)  # Output: {'a', 'f', 't', 'r', 'u'}
# senza comprehensions
caratteri = set()
for c in "frutta":
    caratteri.add(c)
print(caratteri)  # Output: {'a', 'f', 't', 'r', 'u'}

# Esempio 6: Inserire condizioni
numeri = [1, 2, 3, 4, 5]
parita = ["pari" if n % 2 == 0 else "dispari" for n in numeri]
print(parita)  # Output: ['dispari', 'pari', 'dispari', 'pari', 'dispari']
# senza comprehensions
numeri = [1, 2, 3, 4, 5]
parita = []
for numero in numeri:
    if numero % 2 == 0:
        parita.append("pari")
    else:
        parita.append("dispari")
print(parita)  # Output: ['dispari', 'pari', 'dispari', 'pari', 'dispari']