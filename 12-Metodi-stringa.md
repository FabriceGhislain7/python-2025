# METODI STRINGA

```python  
# METODI DI STRINGA  
"""  
In Python, le stringhe hanno metodi integrati che permettono di eseguire operazioni o ottenere informazioni.  
"""

# Length  
# Restituisce la lunghezza di una stringa  
nome2 = "Nome1"  
print(len(nome2))  # Output: 5

# isspace (equivalente di IsNullOrWhiteSpace)  
# Verifica se una stringa è vuota o contiene solo spazi bianchi  
nome3 = " "  
print(nome3.isspace())  # Output: True

# lower  
# Converte una stringa in minuscolo  
nome4 = "Nome1"  
print(nome4.lower())  # Output: nome1

# upper  
# Converte una stringa in maiuscolo  
nome5 = "Nome1"  
print(nome5.upper())  # Output: NOME1

# strip  
# Rimuove gli spazi bianchi all'inizio e alla fine di una stringa  
nome6 = " Nome1 "  
print(nome6.strip())  # Output: Nome1

# split  
# Divide una stringa in base a un separatore  
nomi2 = "Nome1,Nome2,Nome3"  
nomi3 = nomi2.split(",")  # Ritorna una lista  
for nome in nomi3:  
    print(nome)  
# Output:  
# Nome1  
# Nome2  
# Nome3

# replace  
# Sostituisce una sottostringa con un'altra  
nome7 = "Nome1"  
print(nome7.replace("Nome1", "Nome2"))  # Output: Nome2

# substring (equivalente di Substring in C#)  
# In Python, si usa il slicing  
nome8 = "Nome1"  
print(nome8[0:3])  # Output: Nom

# contains  
# Verifica se una stringa contiene una sottostringa  
nome9 = "Nome1"  
print("Nom" in nome9)  # Output: True

# find (equivalente di IndexOf)  
# Restituisce l'indice della prima occorrenza di una sottostringa  
nome10 = "Nome1"  
print(nome10.find("Nome1"))  # Output: 0

# rfind (equivalente di LastIndexOf)  
# Restituisce l'indice dell'ultima occorrenza di una sottostringa  
nome11 = "Nome1"  
print(nome11.rfind("o"))  # Output: 3

# startswith  
# Verifica se una stringa inizia con una sottostringa  
nome12 = "Nome1"  
print(nome12.startswith("N"))  # Output: True

# endswith  
# Verifica se una stringa finisce con una sottostringa  
nome13 = "Nome1"  
print(nome13.endswith("1"))  # Output: True

# Concatenazione di stringhe  
nome14 = "Nome1"  
cognome2 = "Rossi"  
print(nome14 + " " + cognome2)  # Output: Nome1 Rossi

# Concatenazione con interpolazione  
nome15 = "Nome1"  
cognome3 = "Rossi"  
print(f"{nome15} {cognome3}")  # Output: Nome1 Rossi

# Concatenazione con format  
nome16 = "Nome1"  
cognome4 = "Rossi"  
print("{} {}".format(nome16, cognome4))  # Output: Nome1 Rossi

# METODI DI CONVERSIONE  
"""  
Python fornisce funzioni integrate per convertire tipi di dati.  
"""

# Conversione implicita  
eta8 = 10  
altezza3 = eta8 + 1.5  # Da int a float  
print(altezza3)  # Output: 11.5

# Conversione esplicita (cast)  
altezza4 = 1.70  
eta9 = int(altezza4)  # Da float a int  
print(eta9)  # Output: 1

# Conversione con metodi  
eta10 = 10  
eta11 = str(eta10)  # Da int a stringa  
print(f"Il tipo della variabile eta10 è {type(eta10)}")  # Output: <class 'int'>  
print(f"Il tipo della variabile eta11 è {type(eta11)}")  # Output: <class 'str'>

# Parsing di stringhe  
eta4 = "10"  
try:  
    eta4_int = int(eta4)  # Parsing da stringa a int  
    print(eta4_int)  # Output: 10  
except ValueError:  
    print("Conversione non riuscita")

# TryParse simulato  
eta5 = "10"  
try:  
    eta6 = int(eta5)  
    print(eta6)  # Output: 10  
except ValueError:  
    print("Conversione non riuscita")

# Convert (simulazione con metodi di Python)  
eta7 = "10"  
try:  
    eta7_int = int(eta7)  # Parsing da stringa a int  
    print(eta7_int)  # Output: 10  
except ValueError:  
    print("Conversione non riuscita")  
```