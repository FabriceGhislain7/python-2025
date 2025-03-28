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

