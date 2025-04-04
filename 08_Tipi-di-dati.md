# TIPI DI DATI

In python i tipi di dati sono suddivisi in due categorie principali:

1. **Tipi di dati semplici**: includono interi, float, stringhe, booleani e NoneType.
2. **Tipi di dati complessi**: includono array, liste, tuple, dizionari e insiemi.

A differenza di csharp o Java, Python non richiede dichiarazioni esplicite del tipo. Il tipo è dedotto automaticamente dall'assegnazione.

```python
# I TIPI DI DATI SEMPLICI

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
from datetime import datetime
data_nascita = datetime(2000, 1, 1)  # Dichiarazione e inizializzazione di una variabile datetime (anno, mese, giorno)

# Utilizzo delle variabili con interpolazione di stringhe (f-strings)  
print(f"La variabile eta contiene il valore {eta}")  # Output: La variabile eta contiene il valore 10  
print(f"La variabile altezza contiene il valore {altezza}")  # Output: La variabile altezza contiene il valore 1.7

# Ricezione di input dall'utente  
nome_utente = input("Inserisci il tuo nome: ")  # Legge una stringa da tastiera  
print(f"Ciao {nome_utente}!")  # Output: Ciao Nome1!
```

```python
# I TIPI DI DATI COMPLESSI (o strutture di dati)

# ARRAY (con la libreria array)
import array  
numeri = array.array('i', [10, 20, 30, 40, 50])  # Dichiarazione e inizializzazione di un array di interi uso array.array perchè è una libreria
# Aggiunta di un elemento all'array
numeri.append(60)  # Aggiunta di un elemento alla fine dell'array
# 'i' indica che gli elementi dell'array sono numeri interi
# stampo l'array
print(numeri)  # Output: array('i', [10, 20, 30, 40, 50, 60])
# stampo attraverso un ciclo for
for numero in numeri:  
    print(numero)  # Output: 10 20 30 40 50 60

# LISTA  
numeri_lista = [10, 20, 30, 40, 50]  # Dichiarazione e inizializzazione di una lista di interi  
numeri_lista.append(60)  # Aggiunta di un elemento alla lista
# stampo la lista
print(numeri_lista)  # Output: [10, 20, 30, 40, 50, 60]
# stampo attraverso un ciclo for
for numero in numeri_lista:  
    print(numero)  # Output: 10 20 30 40 50 60
# Lista di stringhe  
nomi_lista = ["Nome1", "Nome2", "Nome3"]  # Dichiarazione e inizializzazione di una lista di stringhe
# una lista può contenere elementi di diversi tipi
lista_mista = [10, "Nome1", 20.5, True]  # Dichiarazione e inizializzazione di una lista con elementi di diversi tipi
# stampo la lista
print(lista_mista)  # Output: [10, 'Nome1', 20.5, True]
# stampo attraverso un ciclo for
for elemento in lista_mista:  
    print(elemento)  # Output: 10 Nome1 20.5 True

# DIZIONARIO  
voti = {"Matematica": 28, "Informatica": 30}  # Dichiarazione e inizializzazione di un dizionario  
voti["Fisica"] = 26  # Aggiunta di una nuova coppia chiave-valore al dizionario
# stampo il dizionario
print(voti)  # Output: {'Matematica': 28, 'Informatica': 30, 'Fisica': 26}

# Esempi di utilizzo delle strutture dati  
print(f"Il primo elemento della lista è: {numeri_lista[0]}")  # Output: Il primo elemento della lista è: 10  
print(f"Il voto in Matematica è: {voti['Matematica']}")  # Output: Il voto in Matematica è: 28

# BEST PRACTICES PER LA DICHIARAZIONE DI VARIABILI
# - Usa nomi significativi  
# - Segui la convenzione snake_case per i nomi delle variabili

# Esempio di variabili dichiarate con nomi significativi
eta_studente = 20
altezza_media_studenti = 1.75
is_maggiorenne = True
```