# GENERATORE DI PASSWORD

# Importo il modulo random
import random

# Dichiarazione e inizializzazione di una variabile che contiene una stringa con tutti i caratteri maiuscoli
alfabeto_maiuscolo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Dichiarazione e inizializzazione di una variabile che contiene una stringa con tutti i caratteri minuscoli
alfabeto_minuscolo = alfabeto_maiuscolo.lower()
# Dichiarazione e inizializzazione di una variabile che contiene una stringa con tutti i numeri
numeri = "0123456789"
# Dichiarazione e inizializzazione di una variabile che contiene una stringa con tutti i caratteri speciali
speciali = "!@#$%&*"

# definisco la lunghezza della password
lunghezza = random.randint(4, 8)

# creo una lista di caratteri in modo da memorizzare i caratteri della password
password = []

# seleziono un carattere a caso tra i caratteri maiuscoli
carattere_maiuscolo = random.choice(alfabeto_maiuscolo)

# seleziono un carattere a caso tra i caratteri minuscoli
carattere_minuscolo = random.choice(alfabeto_minuscolo)

# seleziono un carattere a caso tra i numeri
carattere_numero = random.choice(numeri)

# seleziono un carattere a caso tra i caratteri speciali
carattere_speciale = random.choice(speciali)

# aggiungo i caratteri alla password
password.append(carattere_maiuscolo)
password.append(carattere_minuscolo)
password.append(carattere_numero)
password.append(carattere_speciale)

# ciclo for che si ripete per la lunghezza della password
for i in range(lunghezza - 4): # -4 perchè ho già aggiunto 4 caratteri quindi devo aggiungere lunghezza - 4
    # scelgo un carattere a caso tra le liste di caratteri
    lista = random.choice([alfabeto_maiuscolo, alfabeto_minuscolo, numeri, speciali])
    # scelgo un carattere a caso tra i caratteri della lista
    carattere = random.choice(lista)
    # aggiungo il carattere alla password
    password.append(carattere)
    
# faccio uno shuffle dei caratteri della password in modo da farla diventare piu casuale
random.shuffle(password)

# unisco i caratteri della password in una stringa
password = "".join(password)

# stampo la password
print(password)

"""
import random

caratteri = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*"
password = [
    random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    random.choice("abcdefghijklmnopqrstuvwxyz"),
    random.choice("0123456789"),
    random.choice("!@#$%&*")
] + [random.choice(caratteri) for _ in range(random.randint(0, 4))]

random.shuffle(password)
print("".join(password))
"""