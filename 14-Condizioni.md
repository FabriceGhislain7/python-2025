# CONDIZIONI

Le condizioni sono istruzioni che permettono di eseguire un blocco di codice solo se una determinata condizione è vera. In Python, le principali istruzioni di controllo sono:

```python  
# CONDIZIONI  
"""  
Le principali istruzioni di controllo in Python sono:  
- if  
- else  
- elif (equivalente di else if in C#)  
- Non esiste uno switch nativo, ma si può simulare con dizionari o blocchi if-elif-else  
"""

# Pulire la console (simulazione per Python)  
import os  
os.system('cls' if os.name == 'nt' else 'clear')  # Pulisce la console

# ESEMPIO DI IF  
# Se una condizione viene soddisfatta, esegue un blocco di codice  
v = 10  
if v > 5:  
    print("v è maggiore di 5")

# ESEMPIO DI IF ELSE  
# Se una condizione viene soddisfatta, esegue un blocco di codice, altrimenti un altro  
w = 10  
if w > 5:  
    print("w è maggiore di 5")  
else:  
    print("w è minore o uguale a 5")

# ESEMPIO DI IF ELIF ELSE  
# Controlla più condizioni  
x = 10  
if x > 5:  
    print("x è maggiore di 5")  
elif x == 5:  
    print("x è uguale a 5")  
else:  
    print("x è minore di 5")  
# Nota: elif va messo tra if ed else, poiché non verrebbe mai eseguito dopo un else.

# ESEMPIO DI SWITCH (simulazione con un dizionario)  
# Python non ha un'istruzione switch nativa, ma si può simulare con un dizionario  

# **Match-case** (da Python 3.10) che offre funzionalità simili a switch.
# **Default**: Nel caso di match-case, _ viene usato come caso "predefinito" per gestire valori non corrispondenti.
y = 10  
match y:  
    case 5:  
        print("y è uguale a 5")  
    case 10:  
        print("y è uguale a 10")  
    case _:  
        print("y non è né 5 né 10")
# match-case con stringhe
z = "ciao"
match z:
    case "ciao":
        print("z è uguale a ciao")
    case "mondo":
        print("z è uguale a mondo")
    case _:
        print("z non è né ciao né mondo")

# ESEMPIO DI SWITCH CON STRINGHE  
z = "ciao"  
if z == "ciao":  
    print("z è uguale a ciao")  
elif z == "mondo":  
    print("z è uguale a mondo")  
else:  
    print("z non è né ciao né mondo")

# ESEMPIO DI SWITCH CON BOOLEANI  
a = True  
if a is True:  
    print("a è True")  
elif a is False:  
    print("a è False")  
else:  
    print("a non è né True né False")  
```