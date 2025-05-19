# CICLI

"""
I principali tipi di cicli in Python sono:
- for
- while
- Non esiste do-while, ma può essere simulato con while
- foreach è incluso nel for
"""

# for - segue un blocco di codice un numero definito di volte (ciclo con contatore)
# for <variabile> in <sequenza>:
for i in range(11): # range(11) genera i numeri da 0 a 10
    print(i) # Stampa il valore corrente di i
    
# while - Esegue un blocco di codice finché una condizione è
# il ciclo while ha una variabile di controllo
j = 0  # j è una variabile di controllo
while j <= 10:  # Finché j è minore o uguale a 10
    print(j)
    j += 1  # Incrementa j di 1 unita

# while con condizione true
k = 0  # k è una variabile di controllo
while True:  # Ciclo infinito
    print(k)  # Stampa k
    k += 1  # Incrementa k di 1 unita
    if k > 10: # Se k è maggiore di 10
        break # Esce dal ciclo
    
# do while (simulato)
l = 0  # l è una variabile di controllo  
while True:  # Inizia con un ciclo infinito
    print(l) # Stampa l
    l += 1 # Incrementa l di 1 unita
    if not (l > 10): # Se la xcondizione non e soddisfatta, esce dal ciclo
        break
    
# for each (simulato) - Esegue un blocco di codice per ogni elemento di una sequenza o di una colezione
nomi = ["nome1", "nome2", "nome3"]  # Array (o lista) di stringhe
for nome in nomi: # Itera su ogni elemento della lista
    print(nome)  # Stampa il nome