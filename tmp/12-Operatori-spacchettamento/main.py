# OPERATORI DI SPACCHETTAMENTO

# `*` ed `**`
# servono per "spacchettare" o "espandere" contenitori come liste, tuple e dizionari.

# `*` spacchetta una lista o una tupla in argomenti posizionali
# con lista
numeri = [1, 2, 3]
print(*numeri)  # Stampa 1 2 3

# con tupla
numeri = (1, 2, 3)
print(*numeri)  # Stampa 1 2 3

# con dizionario
dati = {"nome": "Nome", "eta": 30}
print(*dati)  # Stampa la chiave
print(*dati.values())  # Stampa i valori

# con dizionario con funzione
dati = {"nome": "Nome", "eta": 30}
def saluta(nome, eta):
    print(f"Ciao {nome}, hai {eta} anni!")

saluta(**dati)

# in assegnazione
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # prende il primo valore
print(b)  # prende in valori in mezzo
print(c)  # prende l ultimo valore

# unire liste
lista1 = [1, 2]
lista2 = [3, 4]
unita = [*lista1, *lista2]
print(unita)  # Stampa [1, 2, 3, 4]

# unire dizionari
# Se ci sono chiavi duplicate, vince l’ultima
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {**d1, **d2}
print(d3)

# mischiare valori normali e spacchettati
valori = [2, 3, 4]
nuova = [1, *valori, 5]
print(nuova)

# convertire stringhe in lista
print([*'ciao'])

# convertire stringhe in tupla
print((*'ciao',))

# convertire range in lista
print([*range(3, 6)])