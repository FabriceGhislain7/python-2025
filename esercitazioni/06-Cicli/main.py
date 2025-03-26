# CICLI
"""
I principali tipi di cicli in Python sono:
- for 
- while
- Non esiste do-while, ma può essere simulato con while
- foreach è incluso nel for
"""

# for - Esegue un blocco di codice un numero defito di volte (ciclo con cntattore)1
# for <variabile> in <sequenza>:
for i in range(11): # Questo commando genera i numeri da 0 a 10
    print(i) # stampa i valori corenti di i
print()

# while - Esegue un blocco di codice finché uma condizione è 
# Il ciclo while ha una variabile di controllo
j = 0  # j è una variabile di controllo
while j <= 10: # Finché j è minore oppure uguale a 10
    print(j)
    j += 1  # incrementa j di 1 unità. 
print()

# while con la condizione "True"
k = 0 # k è una variabile di controllo
while True:
    print(k)  # stampa k
    k += 1    # incrementa k di 1 unità
    if k > 10: # se k è ,aggiore di 10
        break  # Esce dal ciclo
print() 

# do whlie (simulato)
l = 0 # Variabile i controllo 
while True: # while con un ciclo infinito
    print(l) # Stampa l
    if not (l > 10): # Se la condizione non è soddisfata, esce dal ciclo
        break
print()

# for each (simulato) - Esegue un blocco di codice per ogni elementi di una sequenza o una collezione
nomi = ["nome1", "nome2", "nome3"] # Array(o lista di strighe)
for nome in nomi: # itera su ogni elementi della lista 
    print(nome)  # Stampa il nome  


