# RANDOM

import random  # importo la libreria random

# i metodi di random

print(random.randint(1, 100))

# assegno ad una variabile un numero casuale tra 1 e 100
numero_casuale = random.randint(1, 100)
print(numero_casuale)

# scegliere una stringa casuale tra quelle fornite si può usare il metodo choice
# questo metodo puo includere duplicati
print(random.choice(["ciao", "hello", "hola"]))
# oppure
elemento_casuale = random.choice(["ciao", "hello", "hola"])
print(elemento_casuale)

# mescolare una lista si può usare il metodo shuffle
print(random.shuffle([1, 2, 3, 4, 5]))
# oppure
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)

# estrarre un elemento casuale da una lista si può usare il metodo sample
# il numero 1 fuori dalla lista indica il numero di elementi che voglio estrarre
# questo metodo include elementi random unici
print(random.sample([1, 2, 3, 4, 5], 1))
# oppure
elemento = random.sample([1, 2, 3, 4, 5], 1)
print(elemento)

# scegliere n elementi casuali da una lista si può usare il metodo sample
print(random.sample([1, 2, 3, 4, 5], 3))
# oppure
elementi = random.sample([1, 2, 3, 4, 5], 3)
print(elementi)

# e possibile inizializzare il generatore di numeri casuali con un seed
# Ad esempio, se si fissa il seed a 42, la sequenza di numeri casuali generata sarà sempre la stessa
random.seed(1)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
random.seed(None)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

import time  # importa il modulo time
# fisso il numero random tra 3 ed 8
# time.sleep(random.randint(3, 8))
print("Ciao")

print(random.random())  # restituisce un numero float casuale tra 0 e 1

print(random.uniform(1, 10))  # restituisce un numero float casuale tra 1 e 10