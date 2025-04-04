# OPERATORI DI SPACCHETTAMENTO
# '*' e '**' sono operatori di spacchettamento in Python.

# Con una lista
numeri = [1, 2, 3, 4, 5]
print(*numeri)  # Stampa: 1 2 3 4 5

# con un Tupla 
numeri = (1, 2, 3, 4, 5)
print(*numeri)  # Stampa: 1 2 3 4 5

# con un dizionario
dati = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
print(*dati)  # Stampa: nome cognome eta
print(*dati.values())  # Stampa: Mario Rossi 30


# con un dizionario con funziione 
dati = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
def saluta(nome, cognome, eta):
    print(f"Ciao {nome} {cognome}, hai {eta} anni.")

saluta(**dati)  # Stampa: Ciao Mario Rossi, hai 30 anni.

# In assegnezione 
a, *b, c = 1, 2, 3, 4, 5
print(a) # Stampa: 1
print(b) # Stampa: [2, 3, 4]    
print(c) # Stampa: 5

# Nel caso in cui non ci si metesse il * si otterrebbe un errore
# a, b, c = 1, 2, 3, 4, 5 # ValueError: too many values to unpack (expected 3)
# print(a)    
# print(b)
# print(c)  

# unire le liste 
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]  
unita = [*lista1, *lista2]  # Unisce le due liste
print(unita)  # Stampa: [1, 2, 3, 4, 5, 6]

# unire i dizionari
d1 = {"a": 1, "b": 2}   
d2 = {"c": 3, "d": 4}
d3 = {**d1, **d2}  # Unisce i due dizionari
print(d3)  # Stampa: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Mischiare valori normali e spacchettati
valori = [1, 2, 3, 4]
nuova = [0, *valori, 5]  # Aggiunge i valori spacchettati alla lista
print(nuova)  # Stampa: [1, 1, 2, 3, 4, 5]

# Convertire le strighe in lista 
print([*'ciao'])  # Stampa: ['c', 'i', 'a', 'o']
print((*'ciao',))  # Stampa: ('c', 'i', 'a', 'o')

# Convertire le strighe in tupla

# Convertire range in lista
print([*range(3,6)])  # Stampa: [0, 1, 2, 3, 4]