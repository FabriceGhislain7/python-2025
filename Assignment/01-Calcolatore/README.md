# SEMPLICE CALCOLATORE (V 1.0)
## Realizzare un semplice calcolatore che permettere di eseguire le seguente operazioni:
 - Addizione
 - Sottrazione
 - Moltiplicazione
 . Divisione 

## Implementazione 
 - il programma deve chiedere all'utente di inserire due numeri poi cgiedere l'operazione
 - Successivamente deve stampare il risultato ottenuto
 
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