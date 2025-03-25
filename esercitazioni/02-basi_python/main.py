# Questo è un commento.

"""
I metodi di input e print in Python permettono di gestire l'output e l'input (il dialogo con l'utente) attraverso la console
"""
# il metodo print() stampa a video il testo passato come argomento.
# Stampa a video ka striga "Hello World"
print("Hello World!")

# Il metodo input() legge una riga di testo  da tastiera e la restituisce come striga
nome = input("Inserisci il tuo nome: ")
# Stampo ll nome inserito
print ("Ciao", nome)

# Stampo il nome concatenato con una striga 
print("Ciao " + nome + "!") # Con il segno + posso concatenare strighe e variabili.

# Stampo il nome concatenato con una striga utilizzando l'interpolazione (f-strings)
print(f"Caio {nome}") # Con l'interpolazione riesco a concatenare strighe e variabili in modo leggibile.  

# Chiedo all'utente di inserire il proprio cognome
cognome = input ("Inserisce il tuo cognome: ") # leggo il nome da tastiera e lo assegno alla variabile "cognome"

# Stampo il nome completo con l'interpolazione 
print (f"Ciao {nome} {cognome}!") # Con l'interpolazione, riesco a concatenare piu 

# Dichiaro una variabile intera eta_int
eta_int = 47 # Inizializzo la viariabile eta_int con il valore 47

# Stampo eta_int anche provando se la variabile è u intero.
print(eta_int) # Stampo la variabile eta_int

# Dichiarazione di una variabile striga eta_str
eta_str = str(eta_int) # Converto l'intero in striga.

print("Premi un tasto per continuare...")
# metto import a questa riga per prova ma si dovrebbe mettere a
import msvcrt # modulo per leggere un singolo tasto su windows
tasto = msvcrt.getch()  # legge il tasto premuto

# Se il tasto premuto è Enter 
if tasto == b'\r': # Confronto il tasto inserito con il tasto "Enter"
    print("Hai premuto il tasto Enter") # Stampo un messaggio

# Se il tasto premuto è "s"
if tasto.lower() == b's': # Confronto il tasto convertito in minoscolo con 's'
    print("Hai premuto il tasto 's' ") # Stampo un messaggio
    exit() # Esco dal programma