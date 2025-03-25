# TIPI DI DATI SEMPLICI 

# Variabili di tipo intero
eta = 19 # Dichiarazione e inizializzazione di una variabile intera

# Vairiabiòe di tipo decimale 
altezza = 1.70  # Dichirazione e inizializzazione di una variabile decimale

# Variabile di tipo carattere
initiale = 'M'  # Dichiarazione e inizializzazione di una variabile carattere

# Variabile di tipo striga
nome = "Nome1"  # Dichiarazione e inizializzazione di una variabile striga.

# Variabili di tipo booleano 
maggiorenne = True # Dichiarazione e inizializzazione di una variabile booleanno

# Variabile di tipo data
from datetime import datetime  # import il modulo datetime
data_nascita = datetime(2000, 1, 1) # Dichiarazione e inizializzazione di una variabile datetime (anno, mese, giorno)

# Utillizzo delle variabili con interpollazione di stringhe (f-strings)
print(f"La variabile eta contiene contiene il valore {eta}") # Output: La variabile eta contiene contiene il valore 10
print(f"La variabile altezza contiene contiene il valore {altezza}") # Output: La variabile altezza contiene contiene il valore 1.70

# TIPI DI DATI COMPLESSI

# ARRAY (con la libraia array)
import array # import del modulo array
numeri = array.array('i', [10, 20, 30, 40, 50]) # Dichiarazione e inizializzazione di un array di interi
# uso array.array perché una libreria che ha già un motodo che si chiamaallo stesso momento
# 'i' indica che tutti gli elementi dell'array sono degli interi. 
# Stampo l'array
print(numeri) # Output: array('i', [10, 20, 30, 40, 50])
# stampo attraverso un cilco 'for' 
for numero in numeri:
    print(numero) # Stampa ogni elemento
print() # Lasciamo una riga vuota

# LISTA
# Lista degli interi
numeri_lista = [10, 20, 30, 40, 50] # Dichiarazione e inizializzazione di una lista di interi
numeri_lista.append(60) # Aggiunto di un elemento alla lista
# Stampo la lista 
for numero in numeri_lista:
    print(numero)  # Output : 10 20 30 40 50   (in colonna verrà fuori)
print()

# Lista delle strighe
nomi_lista = ["nome1", "nome2", "nome3"] # lista delle varabili solo di tipo strigne

# Lista mista
lista_mista = [10, "Nome1", 20, 5, True] # lista mista contenendo variabili di tipo interi, striga, boleanno 
print(lista_mista)

# DIZIONARI
voti = {"Matematica": 28, "Informatica": 30} # Dichiarazione e inizializzazione di un dizionario
print(voti) # Output: {"Matematica": 28, "Informatica": 30}
voti["Fisica"] = 26  # Aggiuto di una nuova coppia di chiave-valore al dizionario
# Stampo  il dizionario
print(voti)  # Output: {'Matematica': 28, 'Informatica': 30, 'Fisica': 26}

# Esempi dell'utilizzo delle struttue dati
print(f"Il mio primo elemento della lista è {numeri_lista[0]}") # Output: Il primo elemnto dlla lista è 10
print(f"Il mio primo elemento del dizionaro è {voti["Matematica"]}") # Output: Voto di Matematica

# BEST PRACTICES PER LA DICHIARAIONE DELLE VARIABILI 
# - Uso dei nomi significativi 
# - Uso della convenzione snake_name per il nome delle varabili
