# RANDOM

import random  # Importo la libreria random

# i metodi di random

val_int = random.randint(1,100)  # restiuisce un numero casuale tra 1 e 100 
print(val_int)
# oppure scriverlo in una riga
print(random.randint(1, 100))

# Assegno ad una variabile un numero casuale compreso tra 1 e 100
numero_casuale = random.randint(1, 100)
print(numero_casuale)

# scegliere uma striga casuale tra quelle fornite si può usare il metodo choice
print(random.choice(["Ciao", "Hello", "hola"])) # Questo metodo può includere duplicate
# oppure 
elemento_casuale = random.choice(["Ciao", "Hello", "hola"])

# per mescolare una lista si può utilizzare il metodo shuffle
print(random.shuffle([1, 2, 3, 4, 5]))
# oppure 
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)

# Per estrare un numero casuale da una lista si può usare il metodo sample
# Il numero 1 li fuori rappresenta il numero 
# Questo metodo include elementi unici
print(random.sample([1, 2, 3, 4, 5], 1)) 
# oppure 
elemento = random.sample([1, 2, 3, 4, 5], 1)
print(elemento)

# Per estrare n numero casuale da una lista si può usare il metodo sample
# Il numero n li fuori rappresenta il numero 
# Questo metodo include elementi unici
print(random.sample([1, 2, 3, 4, 5], 3)) 
# oppure 
elementi = random.sample([1, 2, 3, 4, 5], 3)
print(elementi)

# è possibile inizializzare il generatore di numeri casuali con un 'seed'
# Ad un esempio, se si fissa a 42, le sequenza casuali generata sarà sempre la stessa.
random.seed(1)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
random.seed(None)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

import time # importo il modulo time

# Fisso il numero random tra 3 e 8 
time.sleep(random.randint(3, 8))
print("Ciao")

print(random.random()) # restituisce un numero casuale tra 0 e 1
print(random.uniform(1, 10)) # restituisce un numero casuale tra 1 e 10