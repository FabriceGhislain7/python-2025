# CONDIZIONI 

# Le condizioni sono istruzioni che permettono di eseguire un blocco di codice solo se una determinata condizione è vera.
"""
Le principali istruzioni di controllo in python sono:
- if 
- else 
- elif (equivalente di else if in c#)
- Non esite uno switch nativo, ma si può simulare con dizionari if-elif-else
"""
# if 
numero_r = 10
if numero_r > 5:
    print("Il numero è maggire di 5")

# if else 
numero_s = 10
if numero_s > 5:
    print("Il numero è maggiorne di 5.")
else:
    print("Il numero è minore o uguale a 5.")

# if elif else
if numero_s > 5:
    print("Il numero è maggiorne di 5.")
elif numero_s == 5:
    print("Il numero è uguale a 5.")
else:
    print("Il numero è minore o uguale a 5.")

# match-case 
# match-case è stato introdotto in python 3.10
# è simile allo swicth-case in altri lingguagi

y = 10 
match y :
    case 5:
        print("y è uguale a 5")
    case 10:
        print("y è uguale a 19")
    case _:
        print("y non è ne 5 ne 10")

# match-case con le strighe 
match z:
    case "ciao":
        print("z è uguale a ciao")
    case "mondo":
        print("z è uguale a mondo")
    case _:
        print("z non è ne ciao ne mondo")





