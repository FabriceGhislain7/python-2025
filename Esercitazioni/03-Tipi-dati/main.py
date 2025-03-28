# TIPI DI DATI

# I TIPI DI DATI SEMPLICI

# Variabili di tipo intero =       int
# Variabili di tipo decimale =     float
# Variabili di tipo stringa =      str
# Variabili di tipo booleano =     bool
# Variabili di tipo data =         datetime

# Variabili di tipo intero
eta = 10  # Dichiarazione e inizializzazione di una variabile intera
# Variabili di tipo decimale
altezza = 1.70  # Dichiarazione e inizializzazione di una variabile float
# Variabili di tipo carattere
iniziale = 'M'  # Dichiarazione e inizializzazione di una variabile carattere
# Variabili di tipo stringa
nome = "Nome1"  # Dichiarazione e inizializzazione di una variabile stringa
# Variabili di tipo booleano
maggiorenne = True  # Dichiarazione e inizializzazione di una variabile booleana
# Variabili di tipo data
from datetime import datetime  # Importo il modulo datetime
data_nascita = datetime(2000, 1, 1)  # Dichiarazione e inizializzazione di una variabile datetime (anno, mese, giorno)
# Utilizzo delle variabili con interpolazione di stringhe (f-strings)  
print(f"La variabile eta contiene il valore {eta}")  # Output: La variabile eta contiene il valore 10  
print(f"La variabile altezza contiene il valore {altezza}")  # Output: La variabile altezza contiene il valore 1.7

# stampo una linea divisoria
print("-" * 40)
# stampa la scritta TIPI DI DATI al centro
print(f"{'TIPI DI DATI':^40}") # ^ allinea al centro 40 è la lunghezza della stringa
print("-" * 40)

# I TIPI DI DATI COMPLESSI (o strutture di dati)

# Liste =           [] Ordinate e modificabili, ammettono duplicati, possono contenere dati di tipi diversi
# Set (insiemi) =   {} Non ordinati e non modificabili, si possono aggiungere o rimuovere elementi non ammettono duplicati (con non modificabili si intende che non si possono modificare gli elementi, ma si possono aggiungere o rimuovere elementi)
# Tuple =           () Ordinate e non modificabili, ammettono duplicati, veloci
# Dizionari =       {} Non ordinati e modificabili, non ammettono chiavi duplicate, possono contenere dati di tipi diversi

# stampa scritta LISTA al centro
print(f"{'LISTA':^40}")
print("-" * 40)

# LISTA

frutta = ["Mela", "Banana", "Ciliegia"]  # Dichiarazione e inizializzazione di una lista
print(frutta)  # Output: ['Mela', 'Banana', 'Ciliegia']

# Accesso agli elementi di una lista
print (frutta[0])  # Output: Mela
print (frutta[-1])  # Output: Ciliegia (ultimo elemento)
print (frutta[-2])  # Output: Banana (penultimo elemento)
# print (frutta[4])  # Output: list index out of range

# Accesso a una porzione di una lista
print (frutta[::])  # Output: ['Mela', 'Banana', 'Ciliegia'] (tutti gli elementi)
print (frutta[::2]) # Output: ['Mela', 'Ciliegia'] (elementi con indice pari)
print (frutta[1:3])  # Output: ['Banana', 'Ciliegia'] (dal secondo al terzo elemento)

# print(dir(frutta))  # accedo ai metodi disponibili per la lista
# print(help(frutta))  # accedo alla documentazione della lista
# print(help(frutta.append))  # accedo alla documentazione del metodo append

len(frutta)  # Output: 3 (numero di elementi nella lista)
print("mela" in frutta) # Output: False (verifica se l'elemento è presente nella lista)
print("Mela" in frutta)  # Output: True (verifica se l'elemento è presente nella lista)

for frutto in frutta:
    print(frutto)  # Stampo ogni elemento della lista
    
frutta.append("Fragola")  # Aggiunta di un elemento alla lista
frutta.remove("Banana")  # Rimozione di un elemento dalla lista
print(frutta)  # Output: ['Mela', 'Pera', 'Ciliegia', 'Fragola']
frutta.pop()  # Rimozione dell'ultimo elemento della lista
# rimozione di un elemento specifico
if "Banana" in frutta:
    frutta.remove("Banana")
# rimozione duplicati
frutta = list(set(frutta))
frutta.insert(0, "Pera")  # Inserimento di un elemento in una posizione specifica (sostuisce l'elemento in quella posizione)
print(frutta)  # Output: ['Mela', 'Pera', 'Ciliegia']
frutta.extend(["Kiwi", "Ananas"])  # Estensione della lista con un'altra lista
frutta.sort()  # Ordinamento della lista
frutta.sort(reverse=True)  # Ordinamento inverso della lista
print(frutta)  # Output: ['Ciliegia', 'Mela', 'Pera']
frutta.reverse()  # Inversione dell'ordine degli elementi della lista
print(frutta)  # Output: ['Pera', 'Mela', 'Ciliegia']
print(frutta.index("Mela"))  # Output: 1 (indice dell'elemento nella lista)
# print(frutta.index("Banana"))  # Output: ValueError: 'Banana' is not in list
frutta.count("Mela")  # Output: 1 (numero di occorrenze dell'elemento nella lista)
frutta.count("Banana")  # Output: 0 (numero di occorrenze dell'elemento nella lista)
frutta.copy()  # Copia della lista
print(frutta)
# copiare la lista su una lista con un nome diverso
frutta2 = frutta.copy()
print(frutta2)
# stampare ed ordinare la lista contemporaneamente
print(sorted(frutta))  # Output: ['Ciliegia', 'Mela', 'Pera']
# stampare ed ordinare ed invertire la lista contemporaneamente
print(sorted(frutta, reverse=True))  # Output: ['Pera', 'Mela', 'Ciliegia']
frutta.clear()  # Rimozione di tutti gli elementi della lista
print(frutta)  # Output: []

# stampa scritta SET al centro
print(f"{'SET':^40}")
# stampa linea divisoria
print("-" * 40)

# SET

frutta_set = {"Mela", "Banana", "Ciliegia", "Banana"}  # Dichiarazione e inizializzazione di un set
print(frutta_set)  # Output: {'Mela', 'Banana', 'Ciliegia'} l'ordine degli elementi può variare

# frutta_set.insert(0, "Pera")  # AttributeError: 'set' object has no attribute 'insert'
# ordinare un set
# frutta_set.sort()  # AttributeError: 'set' object has no attribute 'sort'
# invertire un set
# frutta_set.reverse()  # AttributeError: 'set' object has no attribute 'reverse'
print("Mela" in frutta_set)  # Output: True (verifica se l'elemento è presente nel set)
frutta_set.add("Fragola")  # Aggiunta di un elemento al set
frutta_set.remove("Banana")  # Rimozione di un elemento dal set
print(frutta_set)  # Output: {'Mela', 'Ciliegia', 'Fragola'}
frutta_set.discard("Banana")  # Rimozione di un elemento dal set
frutta_set.update(["Kiwi", "Ananas"])  # Estensione del set con un'altra lista
print(frutta_set)  # Output: {'Mela', 'Ciliegia', 'Fragola', 'Ananas', 'Kiwi'}
frutta_set.pop()  # Rimozione di un elemento casuale dal set
frutta_set.clear()  # Rimozione di tutti gli elementi del set
print(frutta_set)  # Output: set()

# stampa linea divisoria
print("-" * 40)
# stampa scritta TUPLE al centro
print(f"{'TUPLE':^40}")
# stampa linea divisoria
print("-" * 40)

# TUPLE

frutta_tupla = ("Mela", "Banana", "Ciliegia", "Banana")  # Dichiarazione e inizializzazione di una tupla
print(frutta_tupla)  # Output: ('Mela', 'Banana', 'Ciliegia')
print(frutta_tupla[0])  # Output: Mela
print(frutta_tupla[1])  # Output: Banana
# frutta_tupla[0] = "Pera"  # TypeError: 'tuple' object does not support item assignment
print("Mela" in frutta_tupla)  # Output: True (verifica se l'elemento è presente nella tupla)
print(frutta_tupla.count("Mela"))  # Output: 1 (numero di occorrenze dell'elemento nella tupla)
print(frutta_tupla.index("Banana"))  # Output: 1 (indice dell'elemento nella tupla)
print(len(frutta_tupla))  # Output: 3 (numero di elementi nella tupla)
print(frutta.count("Banana"))  # Output: 0 (numero di occorrenze dell'elemento nella tupla)

# stampa linea divisoria
print("-" * 40)
# stampa scritta DIZIONARIO al centro
print(f"{'DIZIONARIO':^40}")
# stampa linea divisoria
print("-" * 40)

# DIZIONARIO

frutta_dizionario = {
    "mela": 2,
    "banana": 3,
    "ciliegia": 5
}  # Dichiarazione e inizializzazione di un dizionario
print(frutta_dizionario)  # Output: {'mela': 2, 'banana': 3, 'ciliegia': 5}
print(frutta_dizionario["mela"])  # Output: 2
frutta_dizionario["mela"] = 4  # Modifica di un valore nel dizionario
print(frutta_dizionario)  # Output: {'mela': 4, 'banana': 3, 'ciliegia': 5}
frutta_dizionario["fragola"] = 6  # Aggiunta di una nuova coppia chiave-valore al dizionario
print(frutta_dizionario)  # Output: {'mela': 4, 'banana': 3, 'ciliegia': 5, 'fragola': 6}
frutta_dizionario.pop("banana")  # Rimozione di una coppia chiave-valore dal dizionario 
print(frutta_dizionario)  # Output: {'mela': 4, 'ciliegia': 5, 'fragola': 6}
print(frutta_dizionario.keys())  # Output: dict_keys(['mela', 'ciliegia', 'fragola'])
print(frutta_dizionario.values())  # Output: dict_values([4, 5, 6])
print(frutta_dizionario.items())  # Output: dict_items([('mela', 4), ('ciliegia', 5), ('fragola', 6)])
print(len(frutta_dizionario))  # Output: 3 (numero di coppie chiave-valore nel dizionario)
print("mela" in frutta_dizionario)  # Output: True (verifica se la chiave è presente nel dizionario)
print("banana" in frutta_dizionario)  # Output: False (verifica se la chiave è presente nel dizionario)
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