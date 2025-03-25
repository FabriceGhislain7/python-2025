# CONDIZIONI
# Le condizioni sono istruzioni che permettono di eseguire un blocco di codice solo se una determinata condizione è vera.

"""  
Le principali istruzioni di controllo in Python sono:  
- if  
- else  
- elif (equivalente di else if in C#)  
- Non esiste uno switch nativo, ma si può simulare con dizionari o blocchi if-elif-else  
- pero c'è il match-case a partire da Python 3.10 che è simile pero lo usano in pochi
"""

# if - Se una condizione viene soddisfatta, esegue un blocco di codice
numero_r = 10 # assegno il valore 10 alla variabile numero_r
if numero_r > 5: # confronto se il numero_r è maggiore di 5
    print("Il numero è maggiore di 5")  # Il numero è maggiore di 5
    
# if else - Se una condizione viene soddisfatta, esegue un blocco di codice, altrimenti un altro blocco
numero_s = 10 # assegno il valore 10 alla variabile numero_s
if numero_s > 5: # confronto se il numero_s è maggiore di 5
    print("Il numero è maggiore di 5")  # Il numero è maggiore di 5
else:
    print("Il numero è minore o uguale a 5")  # Il numero è min
    
# if elif else - Se una condizione viene soddisfatta, esegue un blocco di codice, altrimenti un altro blocco, altrimenti un altro blocco
numero_t = 10 # assegno il valore 10 alla variabile numero_t
if numero_t > 5: # confronto se il numero_t è maggiore di 5
    print("Il numero è maggiore di 5")  # Il numero è maggiore di 5
elif numero_t == 5: # confronto se il numero_t è uguale a 5
    print("Il numero è uguale a 5")  # Il numero è uguale a 5
else:
    print("Il numero è minore di 5")
    
# match-case
# match-case è stato introdotto in Python 3.10
# è simile allo switch-case di altri linguaggi
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