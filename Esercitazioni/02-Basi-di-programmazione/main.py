# METODI DI INPUT E PRINT
# eseguo lo sript con python main.py

"""
I metodi di input e print in Python permettono di gestire l'output e l'input
(il dialogo con l'utente) attraverso la console.
"""

# Il metodo print() stampa a video il testo passato come argomento
# Stampa a video la stringa "Hello World!"
print("Hello World!")

# Il metodo input() legge un testo da tastiera
# e la restituisce come stringa
nome = input("Inserisci il tuo nome: ")
# stampo il nome inserito
print("Ciao", nome)

# Stampo il nome concatenato con una stringa
print("Ciao " + nome + "!")  # Con il segno + posso concatenare stringhe con variabili

# Stampo il nome concatenato con una stringa utilizzando l'interpolazione (f-strings)
print(f"Ciao {nome}!")  # Con l'interpolazione posso concatenare stringhe con variabili in modo leggibile

# Chiedo all'utente di inserire il proprio cognome
cognome = input("Inserisci il tuo cognome: ")  # Leggo il cognome da tastiera e lo assegno alla variabile 'cognome'

# Stampo il nome completo con interpolazione
print(f"Ciao {nome} {cognome}!")  # Con l'interpolazione posso concatenare più variabili in modo semplificato

# Dichiaro una variabile intera eta_int
eta_int = 47 # Inizializzo la variabile eta_int con il valore 47

# stampo eta provando anche se è un intero
print(eta_int) # Stampo la variabile eta_int

# Dichiaro una variabile stringa eta_str
eta_str = str(eta_int)  # Converto l'intero in stringa

# Leggo un input con una pausa per simulare ReadKey
print("Premi un tasto per continuare...")
# metto limport in questa riga per prova ma dovrebbe essere messo all'inizio del file
import msvcrt  # Modulo per leggere un singolo tasto su Windows
tasto = msvcrt.getch()  # Legge il tasto premuto

# Se il tasto premuto è Enter
if tasto == b'\r': # '\r' rappresenta il tasto Enter perche '\r' è il codice ASCII del tasto Enter
    # b indica che è un byte cioè un carattere ASCII
    print("Hai premuto il tasto Enter")  # Stampo un messaggio
    
# Se il tasto premuto è 's' esco dal programma
if tasto.lower() == b's': # Confronto il tasto convertito in minuscolo con 's'
    print("Hai premuto il tasto 's'")  # Stampo un messaggio
    exit()  # Esco dal programma