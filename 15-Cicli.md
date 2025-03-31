# CICLI

I cicli sono strutture di controllo che permettono di eseguire un blocco di codice più volte. In Python, i principali tipi di cicli sono:

```python  
# CICLI  
"""  
I principali tipi di cicli in Python sono:
- for  
- while  
- Non esiste do-while, ma può essere simulato con while
- foreach è incluso nel for
"""

# Pulire la console (simulazione per Python)
import os
os.system('cls' if os.name == 'nt' else 'clear')  # Pulisce la console

# ESEMPIO DI FOR
# Esegue un blocco di codice un numero definito di volte
for i in range(11):  # range(11) genera i numeri da 0 a 10
    print(i)  # Stampa il valore corrente di i

# ESEMPIO DI WHILE  
# Esegue un blocco di codice finché una condizione è vera
j = 0  # j è una variabile di controllo
while j <= 10:  # Finché j è minore o uguale a 10
    print(j)  # Stampa j  
    j += 1  # Incrementa j

# ESEMPIO DI WHILE CON CONDIZIONE TRUE
# Esegue un blocco di codice finché una condizione è vera
k = 0  # k è una variabile di controllo
while True:  # Ciclo infinito  
    print(k)  # Stampa k  
    k += 1  # Incrementa k  
    if k > 10:  # Se k è maggiore di 10  
        break  # Esce dal ciclo

# ESEMPIO DI DO-WHILE SIMULATO  
# Python non ha un costrutto do-while, ma possiamo simularlo con un while  
l = 0  # l è una variabile di controllo  
while True:  # Inizia con un ciclo infinito  
    print(l)  # Stampa l  
    l += 1  # Incrementa l  
    if not (l > 10):  # Condizione per continuare  
        break  # Esce dal ciclo

# ALTRO ESEMPIO DI DO-WHILE SIMULATO  
numero = 10  # numero è una variabile di controllo  
while True:  # Ciclo infinito  
    print(numero)  # Stampa numero  
    numero -= 1  # Decrementa numero  
    if not (numero > 0):  # Se la condizione non è soddisfatta, esce dal ciclo  
        break

# ESEMPIO DI FOREACH  
# Python utilizza il costrutto for per iterare su collezioni  
nomi = ["nome1", "nome2", "nome3"]  # Array (o lista) di stringhe  
for nome in nomi:  # Itera su ogni elemento della lista  
    print(nome)  # Stampa il nome corrente  
```