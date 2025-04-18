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
# calcolatore basico
# definisco quali sono gli input che l'utente deve inserire
primo_numero = float(input("Inserisci il primo numero: "))
secondo_numero = float(input("Inserisci il secondo numero: "))
operazione = input("Inserisci l'operazione da eseguire (+, -, *, /): ")

# definisco le operazioni che il calcolatore deve eseguire
if operazione == "+":
    print(primo_numero + secondo_numero)
elif operazione == "-":
    print(primo_numero - secondo_numero)
elif operazione == "*":
    print(primo_numero * secondo_numero)
elif operazione == "/":
    print(primo_numero / secondo_numero)
    if secondo_numero == 0:
        print("Non puoi dividere per 0")
else:
    print("Operazione non valida")
```

# SEMPLICE CALCOLATORE (V 2.0)
## Obiettivo
Implementare la logica affinche il programma chieda all utente di inserire nuovi numeri da calcolare fino a quando l'utente non decide di uscire.

## Implementazione
- Il programma deve chiedere all'utente di inserire due numeri e l'operazione da eseguire fino a quando l'utente decide di uscire.

```python
# calcolatore basico
while True:
    # definisco quali sono gli input che l'utente deve inserire
    primo_numero = float(input("Inserisci il primo numero: "))
    secondo_numero = float(input("Inserisci il secondo numero: "))
    operazione = input("Inserisci l'operazione da eseguire (+, -, *, /): ")

    # definisco le operazioni che il calcolatore deve eseguire
    if operazione == "+":
        print(primo_numero + secondo_numero)
    elif operazione == "-":
        print(primo_numero - secondo_numero)
    elif operazione == "*":
        print(primo_numero * secondo_numero)
    elif operazione == "/":
        if secondo_numero == 0:
            print("Non puoi dividere per 0")
        else:
            print(primo_numero / secondo_numero)
    else:
        print("Operazione non valida")

    # chiedo all'utente se vuole continuare
    continua = input("Vuoi continuare? (s/n): ")
    if continua.lower() != "s":
        break
```
# SEMPLICE CALCOLATORE (V 3.0)
## Obiettivo
Implementare le funzioni con valori di ritorno per ogni operazione.

## Implementazione
- Il programma deve chiedere all'utente di inserire due numeri e l'operazione da eseguire fino a quando l'utente decide di uscire.
- Ogni operazione deve essere implementata in una funzione con valori di ritorno.

```python
# calcolatore con funzioni
def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Non puoi dividere per 0"
else:
    return a / b

def calcolatore():
    while True:
        primo_numero = float(input("Inserisci il primo numero: "))
        secondo_numero = float(input("Inserisci il secondo numero: "))
        operazione = input("Inserisci l'operazione da eseguire (+, -, *, /): ")

        if operazione == "+":
            print(somma(primo_numero, secondo_numero))
        elif operazione == "-":
            print(sottrazione(primo_numero, secondo_numero))
        elif operazione == "*":
            print(moltiplicazione(primo_numero, secondo_numero))
        elif operazione == "/":
            print(divisione(primo_numero, secondo_numero))
        else:
            print("Operazione non valida")

        continua = input("Vuoi continuare? (s/n): ")
        if continua.lower() != "s":
            break

# chiamo la funzione calcolatore
calcolatore()
```
# SEMPLICE CALCOLATORE (V 4.0)
## Obiettivo
Implementare la gestione delle eccezioni per ogni operazione con try except.

## Implementazione
- Il programma deve chiedere all'utente di inserire due numeri e l'operazione da eseguire fino a quando l'utente decide di uscire.
- Ogni operazione deve essere implementata in una funzione con valori di ritorno.
- Ogni operazione deve essere gestita con try except.

```python
def somma(a, b):
    try:
        return a + b
    except TypeError:
        return "Errore: i valori devono essere numeri"
    
def sottrazione(a, b):
    try:
        return a - b
    except TypeError:
        return "Errore: i valori devono essere numeri"
    
def moltiplicazione(a, b):
    try:
        return a * b
    except TypeError:
        return "Errore: i valori devono essere numeri"
    
def divisione(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return (f"Errore: divisione per zero: {e}")

def calcolatore():
    while True:
        try:
            primo_numero = float(input("Inserisci il primo numero: "))
            secondo_numero = float(input("Inserisci il secondo numero: "))
            operazione = input("Inserisci l'operazione da eseguire (+, -, *, /): ")

            if operazione == "+":
                print(somma(primo_numero, secondo_numero))
            elif operazione == "-":
                print(sottrazione(primo_numero, secondo_numero))
            elif operazione == "*":
                print(moltiplicazione(primo_numero, secondo_numero))
            elif operazione == "/":
                print(divisione(primo_numero, secondo_numero))
            else:
                print("Operazione non valida")
        except ValueError:
            print("Errore: inserisci un numero valido")

        continua = input("Vuoi continuare? (s/n): ")
        if continua.lower() != "s":
            break
# Chiamo la funzione calcolatore
calcolatore()
```