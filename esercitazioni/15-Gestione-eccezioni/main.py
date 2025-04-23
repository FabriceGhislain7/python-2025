# GESTIONE ECCEZIONI

# CATTURA SOLO GLI ERRORI CHE SAI GESTIRE

# Un'eccezione è un errore che si verifica durante l'esecuzione del programma. Se non viene gestita, interrompe l'esecuzione

# In Python, la gestione delle eccezioni avviene con i costrutti:  
# - try-except  
# - try-except-finally

# try:
    # codice che potrebbe generare un'eccezione
# except TipoErrore:
    # codice da eseguire in caso di eccezione

# Try except - gli errori piu comuni

# ZeroDivisionError: divisione per zero
try:
    # Simulazione di un'operazione che può generare un'eccezione
    x = 10 / 0  # Divisione per zero
except ZeroDivisionError as e:
    print(f"Errore: {e}")  # output "Errore: division by zero"
    
# ValueError: conversione di un valore non valido
try:
    numeri = int("ciao")
except ValueError as e:
    print(f"Errore: {e}")  # output "Errore: invalid literal for int() with base 10: 'ciao'"
    
# TypeError: operazione su tipi non compatibili
try:
    risultato = "10" + 5  # Somma tra stringa e numero
except TypeError as e:
    print(f"Errore: {e}")  # output "Errore: can only concatenate str (not 'int') to str"
    
# OverflowError: numero troppo grande
try:
    numero = int("100000000000000000000000000000000000000000000000000000")
except OverflowError as e:
    print(f"Errore: {e}")  # output "Errore: Python int too large to convert to C long"
    
# IndexError: indice fuori range
try:
    lista = [1, 2, 3]
    elemento = lista[3]  # Indice non valido
except IndexError as e:
    print(f"Errore: {e}")  # output "Errore: list index out of range"
    
# KeyError: chiave non trovata in un dizionario
try:
    dizionario = {"a": 1, "b": 2}
    valore = dizionario["c"]  # Chiave non esistente
except KeyError as e:
    print(f"Errore: {e}")  # output "Errore: 'c'"
    
# FileNotFoundError: file non trovato
try:
    with open("file_non_esistente.txt", "r") as file:
        contenuto = file.read()
except FileNotFoundError as e:
    print(f"Errore: {e}")  # output "Errore: [Errno 2] No such file or directory: 'file_non_esistente.txt'"
    
# Import error: modulo non trovato
try:
    import modulo_inesistente
except ImportError as e:
    print(f"Errore: {e}")  # output "Errore: No module named 'modulo_inesistente'"
    
# AttributeError: attributo non trovato
try:
    testo = None
    print(testo.length())  # None non ha un attributo 'len'
except AttributeError as e:
    print(f"Errore: {e}")
    
# Exception generico: cattura tutte le eccezioni (meglio evitare)
try:
    x = 10 / 0
except Exception as e:
    print(f"Errore: {e}")
    
# Gestire piu tipi di eccezione
try:
    numeri = int("ciao")
    # numero = 10/0
    # numeri_stringa = "10"/0
except ValueError as e:
    print(f"Errore: {e}")  # output "Errore: invalid literal for int() with base 10: 'ciao'"
except ZeroDivisionError as e:
    print(f"Errore: {e}")
except TypeError as e:
    print(f"Errore: {e}")

# Gestire eccezioni multiple in un'unica riga (alternativa al precedente)
try:
    numeri = int("ciao")
except (ValueError, TypeError) as e:
    print(f"Errore: {e}")
    
# try except finally
try:  
    number = int("abc")  
except ValueError as e:  
    print(f"Errore di formato: {e}")
finally:
    print("Esecuzione del blocco finally.")
# Il blocco finally viene sempre eseguito, anche in caso di errore

# try except else finally
# dove else viene eseguito solo se non ci sono errori nel blocco try
#  mentre il finally viene sempre eseguito (tipo in modo da chiudere un file)
try:
    f = open("dati.txt", "r")
    contenuto = f.read()
except FileNotFoundError as e:
    print(f"Errore: {e}")
else:
    print("File letto con successo.")
    print(contenuto)
    # f.close() --> senza mettere il close qui
finally:
    print("Chiusura del file.")
    try:
        f.close()
    except NameError:
        print("Il file è gia stato chiuso.")
        
# lanciare un errore volontariamente
try:
    raise ValueError("Errore forzato personalizzato")
except ValueError as e:
    print(f"Errore: {e}")