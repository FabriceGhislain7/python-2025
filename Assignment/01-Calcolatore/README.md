# SEMPLICE CALCOLATORE (V 1.0)
## Obiettivo
Realizzare un semplice calcolatore che permetta di eseguire le seguenti operazioni:
- Addizione
- Sottrazione
- Moltiplicazione
- Divisione

## Implementazione
- Il programma deve chiedere all'utente di inserire due numeri e l'operazione da eseguire.
- Successivamente, deve stampare il risultato dell'operazione.
 
```python 

numero1 = float(input("inserisci il primo numero: "))
numero2 = float(input("inserisci il secondo numero: "))

scelta_operazione = input("Inserisci il segno per l'operazione desiderata: +, -, *, / : ")
operazioni = ["+", "-", "/", "*"]
while not scelta_operazione in operazioni:
    scelta_operazione = input("Inserisci di nuovo il segno per l'operazione desiderata: +, -, *, / : ")

while numero2 == 0 and scelta_operazione == "/":
    numero2 = float(input("il secondo valore deve essere diverso da zero. inserisci di nuovo il secondo numero: "))
    

if scelta_operazione == "+":
    print(numero1 + numero2)
elif scelta_operazione == "-":
    print(numero1 - numero2)
elif scelta_operazione ==  "*":
    print(numero1 * numero2)
else:
    print(numero1/numero2)

```

# SEMPLICE CALCOLATORE (V 2.0)
Continuare nella stessa logica chiedendo all'utente di inserire nuovi numeri finché decida di uscire. 
Implemetare il codice.

```python 

while True:
    numero1 = float(input("inserisci il primo numero: "))
    numero2 = float(input("inserisci il secondo numero: "))

    scelta_operazione = input("Inserisci il segno per l'operazione desiderata: +, -, *, / : ")
    operazioni = ["+", "-", "/", "*"]
    while not scelta_operazione in operazioni:
        scelta_operazione = input("Inserisci di nuovo il segno per l'operazione desiderata: +, -, *, / : ")

    while numero2 == 0 and scelta_operazione == "/":
        numero2 = float(input("il secondo valore deve essere diverso da zero. inserisci di nuovo il secondo numero: "))

    if scelta_operazione == "+":
        print(numero1 + numero2)
    elif scelta_operazione == "-":
        print(numero1 - numero2)
    elif scelta_operazione ==  "*":
        print(numero1 * numero2)
    else:
        print(numero1/numero2)

    continua = input("Vuoi continuare? (si/no): ")
    if continua != "si":
        break
```

# SEMPLICE CALCOLATORE (V 3.0)
Aggiungere in questo codice l'utilizzo delle funzioni per gestire le operazioni e genera la funzione calcolatrice che implementa tutto il codice.
```python 
# Definizione delle funzioni per gestire le operazioni
def somma(a, b):
    return a + b
def sottrazione(a, b):
    return a - b
def moltiplicazione(a, b):
    return a * b
def divisione(a, b):
    return a/b

while True:
    numero1 = float(input("inserisci il primo numero: "))
    numero2 = float(input("inserisci il secondo numero: "))
    scelta_operazione = input("Inserisci il segno per l'operazione desiderata: +, -, *, / : ")
    operazioni = ["+", "-", "/", "*"]

    while not scelta_operazione in operazioni:
        scelta_operazione = input("Inserisci di nuovo il segno per l'operazione desiderata: +, -, *, / : ")
    while numero2 == 0 and scelta_operazione == "/":
        numero2 = float(input("il secondo valore deve essere diverso da zero. inserisci di nuovo il secondo numero: "))

    if scelta_operazione == "+":
        print(somma(numero1, numero2))
    elif scelta_operazione == "-":
        print(sottrazione(numero1, numero2))
    elif scelta_operazione ==  "*":
        print(moltiplicazione(numero1, numero2))
    else:
        print(divisione(numero1, numero2))

    continua = input("Vuoi continuare? (si/no): ")
    if continua != "si":
        break

```

# SEMPLICE CALCOLATRICE (V 4.0)
Aggiungere alla calcolatrice le geszione degli errori.
```python
# Definizione delle funzioni per gestire le operazioni
def somma(a, b):
    return a + b
def sottrazione(a, b):
    return a - b
def moltiplicazione(a, b):
    return a * b
def divisione(a, b):
    try:
        resultato = a/b
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Error: {e}")
    return resultato

def calcolatrice():

    while True:
        numero1 = float(input("inserisci il primo numero: "))
        numero2 = float(input("inserisci il secondo numero: "))
        scelta_operazione = input("Inserisci il segno per l'operazione desiderata: +, -, *, / : ")
        operazioni = ["+", "-", "/", "*"]

        while not scelta_operazione in operazioni:
            scelta_operazione = input("Inserisci di nuovo il segno per l'operazione desiderata: +, -, *, / : ")
        while numero2 == 0 and scelta_operazione == "/":
            numero2 = float(input("il secondo valore deve essere diverso da zero. inserisci di nuovo il secondo numero: "))

        if scelta_operazione == "+":
            print(somma(numero1, numero2))
        elif scelta_operazione == "-":
            print(sottrazione(numero1, numero2))
        elif scelta_operazione ==  "*":
            print(moltiplicazione(numero1, numero2))
        else:
            print(divisione(numero1, numero2))

        continua = input("Vuoi continuare? (si/no): ")
        if continua != "si":
            break

print(calcolatrice())

```
# SEMPLICE CALCOLATRICE (V 5.0)
Facciamo una versione più strimizzata, usando sempre le funzioni e aggiundendo il parametro operazione alla calcolatrice.
 ```python
# Definizione delle funzioni per gestire le operazioni
def somma(a, b):
    try: 
        return a + b
    except ValueError as e:
        print(f"Errore: {e}")

def sottrazione(a, b):
    try: 
        return a - b
    except ValueError as e:
        print(f"Errore: {e}")

def moltiplicazione(a, b):
    try:
        return a * b
    except ValueError as e:
        print(f"Errore: {e}")

def divisione(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Il secondo valore non può essere 0 per l'operazione divisione")
        else:
            return a/b
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Error: {e}")

def calcolatrice(a, b, operazione):
    if operazione == somma:
        return somma(a, b)
    elif operazione == sottrazione:
        return sottrazione(a, b)
    elif operazione ==  moltiplicazione:
        return moltiplicazione(a, b)
    elif operazione == divisione:
        return divisione(a, b)
    else:
        print("Operazione non valida")

print(calcolatrice(4, 0, divisione))

 ```