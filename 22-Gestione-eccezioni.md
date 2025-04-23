# GESTIONE ECCEZIONI

Il sistema di gestione delle eccezioni di Python:

```python  
# GESTIONE DELLE ECCEZIONI  
# In Python, la gestione delle eccezioni avviene con i costrutti:  
# - try-except  
# - try-except-finally

# TRY-EXCEPT  
try:  
    number = int("abc")  # Questo solleverà un ValueError  
except ValueError as e:  
    print(f"Errore: {e}")

# GESTIRE PIÙ TIPI DI ECCEZIONI  
try:  
    number = int("abc")  
except ValueError as e:  
    print(f"Errore di formato: {e}")  
except Exception as e:  
    print(f"Errore generico: {e}")

# TRY-EXCEPT-FINALLY  
try:  
    number = int("abc")  
except ValueError as e:  
    print(f"Errore di formato: {e}")  
finally:  
    print("Il blocco finally viene sempre eseguito")

# LANCIARE ECCEZIONI PERSONALIZZATE  
try:  
    raise Exception("Errore generico personalizzato")  
except Exception as e:  
    print(f"Errore: {e}")

# USO COMPLETO DI TRY-EXCEPT-FINALLY CON RAISE  
try:  
    number = int("abc")  
    raise Exception("Errore generico")  # Eccezione personalizzata  
except ValueError as e:  
    print(f"Errore di formato: {e}")  
except Exception as e:  
    print(f"Errore generico: {e}")  
finally:  
    print("Il blocco finally viene sempre eseguito")

# ESEMPIO: GESTIRE FILE MANCANTI O ERRORI DI FORMATO  
try:  
    with open("file.txt", "r") as file:  
        text = file.read()  
        number = int(text)  # Potrebbe sollevare ValueError  
except FileNotFoundError as e:  
    print(f"File non trovato: {e}")  
except ValueError as e:  
    print(f"Errore di formato: {e}")  
except Exception as e:  
    print(f"Errore generico: {e}")  
finally:  
    print("Il blocco finally viene sempre eseguito")

# GESTIRE INDEXERROR  
try:  
    numbers = [1, 2, 3]  
    print(numbers[3])  # IndexError: accesso fuori dall'intervallo  
except IndexError as e:  
    print(f"Indice non valido: {e}")

# GESTIRE ATTRIBUTERROR PER OGGETTI NULL  
try:
    testo = None
    print(testo.length())  # None non ha un attributo 'len'
except AttributeError as e:
    print(f"Errore: {e}")


# GESTIRE ZERODIVISIONERROR  
try:  
    result = 10 / 0  
except ZeroDivisionError as e:  
    print(f"Divisione per zero: {e}")

# GESTIRE OVERFLOWERROR  
try:  
    number = int("100000000000000000000000")  # Solleva ValueError in Python  
except OverflowError as e:  
    print(f"Overflow: {e}")  
except ValueError as e:  
    print(f"Errore di conversione: {e}")

# GESTIRE ECCEZIONI CON THROW E RAISE  
try:  
    raise OverflowError("Errore di overflow personalizzato")  
except OverflowError as e:  
    print(f"Errore personalizzato: {e}")  

```
Eccezione | Cosa significa
--- | ---
ValueError | Conversione non valida (es. int("abc"))
TypeError | Operazione su tipi incompatibili
ZeroDivisionError | Divisione per zero
IndexError | Indice fuori range su liste
KeyError | Chiave non esistente in un dizionario
FileNotFoundError | File inesistente
ImportError | Problemi nell'import di moduli