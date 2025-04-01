# STRIGHE

# length
nome = "Nome1"
print(len(nome))  # output: 5

# isspace              # Controlla se la stringa è composta solo da spazi bianchi
punctuatione = " la virgola "
nome = "   "
print(punctuatione.isspace())  # output: False
print(nome.isspace())  # output: True

# lower
nome3 = "Nome2"
print(nome3.lower())  # output: nome2

# upper
nome4 = "Nome3" 
print(nome4.upper())  # output: NOME3

# strip
nomi2 = ",,Nomi1,Nomi2,Nomi3,,"
nomi3 = nomi2.strip(",") # Rimuove le virgole all'inizio e alla fine della stringa
print(nomi3)  # output: Nomi1,Nomi2,Nomi3

# split
nomi2 = "Nomi1,Nomi2,Nomi3"
nomi3 = nomi2.split(",") # Divide la stringa in una lista di stringhe
for nome in nomi3:
    print(nome)  # output: Nomi1 Nomi2 Nomi3    
# Output:
# Nomi1         
# Nomi2
# Nomi3

# replace
nome7 = "Nome1"
print(nome7.replace("Nome1", "Nome2"))  # output: Nome2

# slicing
nome8 = "Nome1"
print(nome8[0:3])  # output: Nom

# contains
nome9 = "Nome1"
print("Nome1" in nome9)  # output: True

# find
nome10 = "Nome1"
print(nome10.find("Nome1"))  # Restituisce la posizione della prima occorrenza della sottostringa, 
# oppure -1 se non trovata
# output: 0
print(nome10.find("2Nome2"))  # output: -1
print(nome10.find("1"))  # output: 4

# rfind
nome11 = "Nome1"
print(nome11.rfind("o"))  # Restituisce la posizione dell'ultima occorrenza della sottostringa, 
# oppure -1 se non trovata
# output: 2

# startswith     # Controlla se la stringa inizia con una sottostringa specificata
nome12 = "Nome1"  
print(nome12.startswith("Nome"))  # output: True
print(nome12.startswith("Nome2"))  # output: False
print(nome12.startswith("o"))  # output: False
print(nome12.startswith("N"))  # output: True   

# endswith       # Controlla se la stringa termina con una sottostringa specificata
nome13 = "Nome1"        
print(nome13.endswith("1"))  # output: True
print(nome13.endswith("Nome"))  # output: False

# concatenazione con format
nomme = "Nome1"
cognome = "Cognome1"
print("Nome: {},\nCognome: {}".format(nomme, cognome))  # output: Nome: Nome1, Cognome: Cognome1
# si puo usare una \n per portare a capo il testo
print("Nome: {},\nCognome: {}".format(nomme, cognome))  # output: Nome: Nome1, Cognome: Cognome1

# metodo per convertire i tipi di dati
# Conversione implicita che non richiede l'uso di un metodo

eta = 21
eta_aggiornata = eta + 1  # Conversione implicita da int a str
print(eta_aggiornata)  # output: 22
# verifica che tipo di dato è una varibile
print(type(eta))  # output: <class 'int'>
print(type(eta_aggiornata))  # output: <class 'int'>    

# Conversione esplicita che richiede l'uso di un metodo
altezza = 1.75
altezza_aggiornata = int(altezza)  # Conversione esplicita da float a str
print(altezza_aggiornata)  # output: 1

print(f"Il tipo di variabile altezza è: {type(altezza)}")  # output: Il tipo di variabile altezza è: <class 'float'>
print(f"Il tipo di variabile altezza_aggiornata è: {type(altezza_aggiornata)}")  # output: Il tipo di variabile altezza_aggiornata è: <class 'int'>

# Parsing di stringhe 
# Conversione da stigha a int
eta_stringa = "21"

try:
    eta_int = int(eta_stringa)  # Conversione da stringa a int
    print(f"Conversione riuscita: {eta_int}")  # output: Conversione riuscita: 21
except ValueError:
    print("Conversione fallita: la stringa non è un numero intero valido.")
    # Stampa i tipo di errore
    import sys  # Importa il modulo sys per gestire gli errori
    print(f"Errore: {sys.exc_info()[0]}")

# Conversione da stringa a float
eta_stringa_sbagliata = "hgktrva"  # stringa non valida per la conversione in int
eta_stringa_sbagliata = float(eta_stringa_sbagliata)  # Conversione da stringa a float
# Stampa i tipo di errore
print(f"Errore: {sys.exc_info()[0]}")  # output: Errore: <class 'ValueError'>
