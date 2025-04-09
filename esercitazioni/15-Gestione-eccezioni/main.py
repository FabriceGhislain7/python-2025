# GESTIONE ECCEZIONE

#   try except 
# ------------------------------------------------
# ZeroDivisionError
try:
    x = 10 / 0 
except ZeroDivisionError as e:
    print(f"Errore: {e}")
# -------------------------------------------------
# ValueError. Errore sul valore dei dati.
try:
    numeri = int("Ciao")
except ValueError as e:
    print(f"Errore: {e}")

# -------------------------------------------------
# TypeError. Errore sulla tipologia dei dati.
try:
    risultato = "30" + 10
    print(risultato)
except TypeError as e:
    print(f"Errore: {e}")
    
# ------------------------------------------------
# OverflowError : Numero fuori dall scala accatabile.
import math
try:
    number = math.factorial(112312423452456356745856797809808663514524357478)
    print(number)
except OverflowError as e:
    print(f"Errore: {e}")
# ------------------------------------------------
# IndexError: indice fuori range
try:
    lista = [1, 2, 3]
    elemento = lista[3]
except IndexError as e:
    print(f"Errore: {e}")
# -------------------------------------------------
# KeyError: Chiave non trovata in un dizionario
try:
    dizionario = {"a": 1, "b": 2}
    valore = dizionario["c"]
except KeyError as e:
    print(f"Error: {e}")
# ------------------------------------------------
# FileNotFoundError : permette di verificare se un file exist.
try:
    with open("file_non_esistente.txt", "r") as file:
        contenuto = file.read()
except FileNotFoundError as e:
    print(f"Errore: {e}")
#-----------------------------------------------------
# Attribution error
try:
    testo = None
    print(testo.length())
except AttributeError as e:
    print(f"Errore: {e}")
#-----------------------------------------------------
# import Error, modulo non trovato
try:
    import modulo_inesistente
except ImportError as e:
    print(f"Errore: {e}")
# ----------------------------------------------------
# Gestione di più errori
try: 
    numeri = int("Ciao")
    risult = "7" + 10
    number = 10 / 0
except ValueError as e:
    print(f"Errore: {e}")
except ZeroDivisionError as e:
    print(f"Errore: {e}")
except TypeError as e:
    print(f"Errore: {e}")
# --------------------------------------------------.-
# try except finally
try: 
    numeri = int("abc")
    risult = "7" + 10
    number = 10 / 0
except ValueError as e:
    print(f"Errore in formato: {e}")
finally:
    print(f"Esecuzione del blocco finally.")
# Il blocco finally viene sempre eseguito anche in cso di errori
#---------------------------------------------------------
# try except finally

try:
    f = open("dati.txt", "r")
    contenuto = file.read()
except FileNotFoundError as e:
    print(f"Errore: {e}")
else:
    print("File letto con successo.")
    print(contenuto)
    # file.close() --> Senza mettere close al contenuto qui.
finally:
    print("Chiusura del file")
    try:
        file.close()
    except NameError:
        print("Il file è già stato chiuso.")
# -----------------------------------------------------------
# Lanciare un errore volontariamente
try:
    raise ValueError("Errore forzato generato.")
except ValueError as e: 
    print(f"Errore: {e}")





