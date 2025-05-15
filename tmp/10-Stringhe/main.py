# STRINGHE

# metodi che permettono di eseguire operazioni o ottenere informazioni
# Length
nome = "Nome1"
print(len(nome))  # Output: 5

# isspace
nome2 = " "
print(nome2.isspace())  # Output: True

# lower
nome3 = "Nome2"
print(nome3.lower())  # Output: nome2

# upper
nome4 = "Nome3"
print(nome4.upper())  # Output: NOME3

# strip
nome5 = " Nome4 "
print(nome5.strip())  # Output: Nome4

# split
nomi2 = "Nome1,Nome2,Nome3"
nomi3 = nomi2.split(",")  # Ritorna una lista
for nome in nomi3:  
    print(nome)  
# Output:  
# Nome1  
# Nome2  
# Nome3

# replace
nome7 = "Nome1"  
print(nome7.replace("Nome1", "Nome2"))  # Output: Nome2

# slicing
nome8 = "Nome1"
print(nome8[0:3])  # Output: Nom

# contains
nome9 = "Nome1"
print("Nome" in nome9)  # Output: True

# find restituisce -1 se non trova nessuna occorrenza
nome10 = "Nome1"
print(nome10.find("Nome1"))  # Output: 0 restituisce la posizione della prima occorrenza

# rfind
nome11 = "Nome1"
print(nome11.rfind("o"))  # Output: 0 restituisce la posizione dell'ultima occorrenza

# startswith
nome12 = "Nome1"
print(nome12.startswith("N"))  # Output: True

# endswith
nome13 = "Nome1"
print(nome13.endswith("1"))  # Output: True

# Concatenazione con format
nomme = "Nome1"
cognome = "Cognome1"
print("{} {}".format(nome, cognome))

# metodi per convertire tipi di dati

# Conversione implicita cioe che non richiede l'uso di metodi
eta = 21
eta_aggiornata = eta + 1.5
print(eta_aggiornata)  # Output: 22.5 (conversione da int a float)
# verificare che tipo di dato e una variabile
print(type(eta))  # Output: <class 'int'>
print(type(eta_aggiornata))  # Output: <class 'float'>

# Conversione esplicita (cast) cioe che richiede l'uso di metodi
altezza = 1.75
altezza_aggiornata = int(altezza)  # Conversione da float a int
print(altezza_aggiornata)  # Output: 1
print(f"Il tipo di variabile altezza è {type(altezza)}")
print(f"Il tipo di variabile altezza_aggiornata è {type(altezza_aggiornata)}")

# Parsing di stringhe
# Conversione da stringa a int
eta_stringa = "21.15"
try:
    eta_int = int(eta_stringa)
    print(f"Conversione riuscita: {eta_int}")
except ValueError:
    print("Conversione fallita: la stringa non è un numero valido.")
    # stampa il tipo di errore
    import sys
    print(f"Tipo di errore: {sys.exc_info()[0]}")

# Conversione da stringa a float
# eta_stringa_sbagliata = "fdgdd"
# eta_stringa_sbagliata = int(eta_stringa_sbagliata)  # Questo genererà un errore ValueError: invalid literal for int()