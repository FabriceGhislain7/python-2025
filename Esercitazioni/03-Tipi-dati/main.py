# I TIPI DI DATI COMPLESSI (o strutture di dati)

# Liste =           [] Ordinate e modificabili, ammettono duplicati, possono contenere dati di tipi diversi
# Set (insiemi) =   {} Non ordinati e non modificabili, si possono aggiungere o rimuovere elementi non ammettono duplicati
# Tuple =           () Ordinate e non modificabili, ammettono duplicati, veloci
# Dizionari =       {} Non ordinati e modificabili, non ammettono chiavi duplicate, possono contenere dati di tipi diversi

# stampa scritta LISTA al centro
print(f"{'LISTA':^40}")
print("-" * 40)

# LISTA

frutta = ["Mela", "Banana", "Ciliegia", "Banana"]  # Dichiarazione e inizializzazione di una lista
print(frutta)  # Output: ['Mela', 'Banana', 'Ciliegia']
print (frutta[0]) # Output: Mela
print (frutta[-1])  # Output: Ciliegia (ultimo elemento)
print (frutta[-2])  # Output: Banana (penultimo elemento)
# print (frutta[3])  # Output: list index out of range
print (frutta[::])  # Output: ['Mela', 'Banana', 'Ciliegia'] (tutti gli elementi)
print (frutta[::2]) # Output: ['Mela', 'Ciliegia'] (elementi con indice pari)
print (frutta[1:3])  # Output: ['Banana', 'Ciliegia'] (dal secondo al terzo elemento)

# stampa con for
for frutto in frutta:
    print(frutto)  # Stampo ogni elemento della lista
# stampa con join
print(", ".join(frutta))  # Output: Mela, Banana, Ciliegia

# print(dir(frutta))  # accedo ai metodi disponibili per la lista
# print(help(frutta))  # accedo alla documentazione della lista
# print(help(frutta.append))  # accedo alla documentazione del metodo append

print(len(frutta)) # Output: 4 (numero di elementi nella lista)
print("mela" in frutta) # Output: False (verifica se l'elemento è presente nella lista)
print("Mela" in frutta) # Output: True (verifica se l'elemento è presente nella lista)
print(frutta.count("Banana"))  # Output: 3 (numero di occorrenze dell'elemento nella lista)
print(frutta.count("Melone"))  # Output: 0 (numero di occorrenze dell'elemento nella lista)

frutta.append("Fragola")  # Aggiunta di un elemento alla lista in modo che sia l ultimo elemento
print(frutta)
frutta.extend(["Kiwi", "Ananas"])  # Estensione della lista con un'altra lista
print(frutta)

frutta.remove("Banana")  # Rimozione di un elemento dalla lista se c'è piu di un occorrenza rimuove la prima occorrenza
print(frutta)
frutta.pop()  # Rimozione dell'ultimo elemento della lista
print(frutta)
if "Banana" in frutta:
    frutta.remove("Banana") # Rimozione di un elemento specifico
print(frutta)
frutta.append("Banana")
frutta.append("Banana")
frutta.append("Banana")
# frutta=list(set(frutta)) # Rimozione duplicati che genera un set non ordinato
print(frutta)

frutta.insert(0, "Pera")  # Inserimento di un elemento in una posizione specifica (sostuisce l'elemento in quella posizione)
print(frutta)

frutta.sort()  # Ordinamento della lista
print(frutta)
frutta.reverse()  # Inversione dell'ordine degli elementi
print(frutta)
frutta.sort(reverse=True)  # Ordinamento inverso della lista
print(frutta)
# stampare ed ordinare la lista contemporaneamente
print(sorted(frutta))  # Output: ['Ciliegia', 'Mela', 'Pera']
# stampare ed ordinare ed invertire la lista contemporaneamente
print(sorted(frutta, reverse=True))  # Output: ['Pera', 'Mela', 'Ciliegia']

print(frutta.index("Pera"))  # Output: 0 (indice dell'elemento nella lista)
# print(frutta.index("Melone"))  # Output: ValueError: 'Melone' is not in list

frutta.copy()  # Copia della lista (in questo caso le modifiche non vengono applicate alla lista originale ma alla copia)
print(frutta)
# copiare la lista su una lista con un nome diverso
frutta2 = frutta.copy() # Copia della lista in modo da avere due liste indipendenti
print(frutta2)

frutta.clear()  # Rimozione di tutti gli elementi della lista
print(frutta)  # Output: []

# stampa scritta SET al centro
print(f"{'SET':^40}")
# stampa linea divisoria
print("-" * 40)

# SET

# I set sono usati principalmente per eliminare duplicati da una lista o per eseguire operazioni di insieme come unione, intersezione, differenza e differenza simmetrica.
# Il vantaggio di un set, rispetto ad una lista, è che è più veloce per verificare se un elemento è presente in un set rispetto ad una lista.

frutta_set = {"Mela", "Banana", "Ciliegia", "Banana"}  # Dichiarazione e inizializzazione di un set
print(frutta_set)  # Output: {'Mela', 'Banana', 'Ciliegia'} l'ordine degli elementi può variare

# frutta_set.insert(0, "Pera")
# frutta_set.sort()
# frutta_set.reverse()

print(dir(frutta_set)) # accedo ai metodi disponibili per il set

print("Mela" in frutta_set)  # Output: True (verifica se l'elemento è presente nel set)

frutta_set.remove("Banana")  # Rimozione di un elemento dal set
frutta_set.discard("Banana")  # Rimozione di un elemento dal set
# la differenza tra discard e remove è che remove genera un errore se l'elemento non è presente nel set

frutta_set.add("Fragola")  # Aggiunta di un elemento al set
print(frutta_set)  # Output: {'Mela', 'Ciliegia', 'Fragola'}

frutta_set.update(["Kiwi", "Ananas"])  # Estensione del set con un'altra lista
print(frutta_set)  # Output: {'Mela', 'Ciliegia', 'Fragola', 'Ananas', 'Kiwi'}

frutta_set.pop()  # Rimozione di un elemento casuale dal set
print(frutta_set)

frutta_set.clear()  # Rimozione di tutti gli elementi del set
print(frutta_set)  # Output: set()

# stampa linea divisoria
print("-" * 40)
# stampa scritta TUPLE al centro
print(f"{'TUPLE':^40}")
# stampa linea divisoria
print("-" * 40)

# TUPLE 

# Le tuple sono simili alle liste, ma sono immutabili, cioè non possono essere modificate dopo la creazione.
# Le tuple si usano principalmente per proteggere i dati che non devono essere modificati.
# Le tuple sono più veloci delle liste e delle tuple e occupano meno spazio in memoria.

frutta_tupla = ("Mela", "Banana", "Ciliegia", "Banana")  # Dichiarazione e inizializzazione di una tupla
print(frutta_tupla)  # Output: ('Mela', 'Banana', 'Ciliegia', 'Banana')

print(frutta_tupla[0])  # Output: Mela
print(frutta_tupla[1])  # Output: Banana

# frutta_tupla.insert(0, "Pera") # AttributeError: 'tuple' object has no attribute 'insert'
# frutta_tupla[0] = "Pera" # TypeError: 'tuple' object does not support item assignment

print("Mela" in frutta_tupla)  # Output: True (verifica se l'elemento è presente nella tupla)
print(frutta_tupla.count("Mela"))  # Output: 1 (numero di occorrenze dell'elemento nella tupla)
print(frutta_tupla.count("Banana"))  # Output: 2 (numero di occorrenze dell'elemento nella tupla)
print(frutta_tupla.index("Banana"))  # Output: 1 (indice della prima occorrenza dell'elemento nella tupla)
print(len(frutta_tupla))  # Output: 4 (numero di elementi nella tupla)

# stampa linea divisoria
print("-" * 40)
# stampa scritta DIZIONARIO al centro
print(f"{'DIZIONARIO':^40}")
# stampa linea divisoria
print("-" * 40)

# DIZIONARIO

# I dizionari sono usati per memorizzare dati in coppie chiave-valore.
# Un dizionario è una raccolta non ordinata, modificabile e indicizzata.
# I dizionari non possono avere due chiavi uguali e sono veloci nel trovare un valore tramite la chiave.

frutta_dizionario = {"mela": 2, "banana": 3, "ciliegia": 5}  # Dichiarazione e inizializzazione di un dizionario
print(frutta_dizionario)  # Output: {'mela': 2, 'banana': 3, 'ciliegia': 5}

print(frutta_dizionario["mela"])  # Output: 2 (accedo al valore assegnato alla chiave)

frutta_dizionario["mela"] = 4  # Modifica del valore associato alla chiave
print(frutta_dizionario)
frutta_dizionario.pop("banana")  # Rimozione di una coppia chiave-valore
print(frutta_dizionario)  # Output: {'mela': 4, 'ciliegia': 5, 'fragola': 6}
frutta_dizionario["fragola"] = frutta_dizionario.pop("mela")  # in questo caso la chiave mela viene sostituita con fragola
print(frutta_dizionario)  # Output: {'ciliegia': 5, 'fragola': 4}

frutta_dizionario["fragola"] = 6  # Aggiunta di una nuova coppia chiave-valore
print(frutta_dizionario) # Output: {'mela': 4, 'banana': 3, 'ciliegia': 5, 'fragola': 6}

print(frutta_dizionario.keys())  # Output: dict_keys(['mela', 'banana', 'ciliegia'])
print(frutta_dizionario.values())  # Output: dict_values([2, 3, 5])
# posso generare una lista di tuple ocsi
print(frutta_dizionario.items())  # Output: dict_items([('mela', 2), ('banana', 3), ('ciliegia', 5)])

print(len(frutta_dizionario))  # Output: 3 (numero di coppie chiave-valore nel dizionario)

print("mela" in frutta_dizionario)  # Output: False (verifica se la chiave è presente nel dizionario)

frutta_dizionario.clear()  # Rimozione di tutte le coppie chiave-valore dal dizionario
print(frutta_dizionario)  # Output: {}

# BEST PRACTICES PER LA DICHIARAZIONE DI VARIABILI  
# - Usa nomi significativi  
# - Segui la convenzione snake_case per i nomi delle variabili

# Esempio di variabili dichiarate con nomi significativi
frutta_tipo = "Mela"  # Dichiarazione e inizializzazione di una variabile stringa
frutta_quantita = 2  # Dichiarazione e inizializzazione di una variabile intera
frutta_prezzo = 1.50  # Dichiarazione e inizializzazione di una variabile float
is_delivered = True  # Dichiarazione e inizializzazione di una variabile booleana