# METODI DI CONSOLE

I metodi di console sono utilizzati per interagire con l'utente attraverso la console. Questi metodi consentono di leggere input da tastiera e stampare output a video. In Python, i metodi di console principali sono input() e print().

```python  
# Questo è un commento a riga singola

"""  
Questo è un commento a riga multipla  
"""

"""  
I metodi di input e print in Python permettono di gestire l'output e l'input (il dialogo con l'utente) attraverso la console.  
print() stampa a video una stringa.  
input() legge una stringa da tastiera.  
"""

# Il metodo print() stampa a video il testo passato come argomento  
print("Hello World!")

# Il metodo input() legge una riga di testo da tastiera  
nome = input("Inserisci il tuo nome: ")  # legge una riga di testo da tastiera e la assegna alla variabile 'nome'

# Stampo il nome concatenato con una stringa  
print("Ciao " + nome + "!")  # Con il segno + posso concatenare stringhe con variabili

# Stampo il nome concatenato con una stringa utilizzando l'interpolazione (f-strings)  
print(f"Ciao {nome}!")  # Con l'interpolazione posso concatenare stringhe con variabili in modo leggibile

# Chiedo all'utente di inserire il proprio cognome  
cognome = input("Inserisci il tuo cognome: ")  # Leggo il cognome da tastiera e lo assegno alla variabile 'cognome'

# Stampo il nome completo con interpolazione  
print(f"Ciao {nome} {cognome}!")  # Con l'interpolazione posso concatenare più variabili in modo semplificato

# Dichiaro una variabile intera eta_int  
eta_int = 47  # Inizializzo la variabile eta_int con il valore 47

# Dichiaro una variabile stringa eta_str  
eta_str = str(eta_int)  # Converto l'intero in stringa

# Concateno eta_int con una stringa  
print(f"Hai {eta_int} anni")  # Uso l'interpolazione per includere la variabile nella stringa

# Leggo un input con una pausa per simulare ReadKey  
print("Premi un tasto per continuare...")  
import msvcrt  # Modulo per leggere un singolo tasto su Windows  
tasto = msvcrt.getch()  # Legge il tasto premuto

# Se il tasto premuto è Enter  
if tasto == b'\r':  # '\r' rappresenta il tasto Enter perche '\r' è il codice ASCII del tasto Enter
                    # si usano : perche '\r' è un byte cioè un carattere ASCII
                    # b indica che è un byte cioè un carattere ASCII
    print("Hai premuto il tasto Enter")

# Se il tasto premuto è 's' esco dal programma  
if tasto.lower() == b's':  # Confronto il tasto convertito in minuscolo con 's'  
                           # b indica che è un byte cioè un carattere ASCII  
    print("Hai premuto il tasto S")  
    exit()  # Esco dal programma