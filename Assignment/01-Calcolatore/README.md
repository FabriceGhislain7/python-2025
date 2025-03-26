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