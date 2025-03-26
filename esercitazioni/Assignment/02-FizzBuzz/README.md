# FIZZBUZZ(v 1.0)

## OBIETTIVO

E un classico esercizio di programmazione usato spesso nei colloqui tecnico per testare le capacità di scrivere codice semplice e logico
Per ogin numero da 1 a 100:

 - Se il numero è divisibileper 3, stampa "Fizz"
 - Se è divisibile per 5, stampa "Buzz"
 - Se è divisibile per entrambi, stampa "FizzBuzz".
 - Altrimenti, stampa il numero

## Implementazione
Il programma deve stampare i numeri da 1 a 100, applicando le regole sopra desscritte

```python 
for numero in range(1, 101): 
    if numero % 3 == 0 and numero % 5 == 0: # Se è divisibile per entrambi, stampa "FizzBuzz".
        print("FizzBuzz")
    elif numero % 3 == 0: 
        print("Fizz")
    elif numero % 5 == 0: 
        print("Buzz")
    else: 
        print(numero)
```
# FIZZBUZZ(v 2.0)

## OBIETTIVO

In questo esercizio l'utente deve inserire un valore intero e comparira una delle condizioni elencate sopra.

## implementazione
l'utente deve inserire un valore intero e comparira una delle condizioni elencate sopra.

```python
numero = int(input("Inserisci un numero intero: "))

if numero % 3 == 0 and numero % 5 == 0: # Se è divisibile per entrambi, stampa "FizzBuzz".
    print(f"{numero} -> FizzBuzz")
elif numero % 3 == 0: 
    print(f"{numero} -> Fizz")
elif numero % 5 == 0: 
    print(f"{numero} -> Buzz")
else: 
    print(numero)

```

# FIZZBUZZ(v 3.0)

## OBIETTIVO

In questo esercizio permettiamo all'utente di inserire più numeri.

## Implementazione
L'utente può uscire dal programma scrivendo "esci" altrimenti il programma chiede di inserire un altro numero
OPZIONALE: usare il metodo `isdigit` per controllare se l'input è un numero.
```python
while True:
    inserimento = input("Inserisci un numero intero valido oppure inserici 'esci' per uscire dal programma: ")
    
    if inserimento.lower() == "esci":
        print("Ciao, alla prossima.")
        break
    
    if not inserimento.isdigit:
        print("Per favore inserire un numero intero valido oppure 'esci' per uscire dal programma: " )
        continue # Ricomincia il ciclo for while dall'inizio 
    
    numero = int(inserimento)    # Convertiamo la striga in numer intero.

    if numero % 3 == 0 and numero % 5 == 0: 
        print(f"{numero} -> FizzBuzz")
    elif numero % 3 == 0: 
        print(f"{numero} -> Fizz")
    elif numero % 5 == 0: 
        print(f"{numero} -> Buzz")
    else: 
        print(numero)
```

# FIZZBUZZ(v 4.0)

## OBIETTIVO

Implementare un contatore in modo a tenere traccia di quante volte sono usciti fizz, buzz, fizzbuzz, nessuno viene stampato il conteggio del contatore.

## Implementazione
Nel momento in cui l'utente inserisci 'esci', viene stampato il contatore
```python 

contatore_Fizz = 0
contatore_Buzz = 0
contatore_FizzBuzz = 0
contatore_nessuno = 0

while True:
    
    inserimento = input("Inserisci un numero intero valido oppure inserici 'esci' per uscire dal programma: ")
    
    if inserimento.lower() == "esci":
        print("Ciao, alla prossima.")
        break
    
    if not inserimento.isdigit():
        print("Per favore inserire un numero intero valido oppure 'esci' per uscire dal programma: " )
        continue # Ricomincia il ciclo for while dall'inizio 
    
    numero = int(inserimento)    # Convertiamo la striga in numer intero.

    if numero % 3 == 0 and numero % 5 == 0: 
        print(f"{numero} -> FizzBuzz")
        contatore_FizzBuzz += 1

    elif numero % 3 == 0: 
        print(f"{numero} -> Fizz")
        contatore_Fizz += 1

    elif numero % 5 == 0: 
        print(f"{numero} -> Buzz")
        contatore_Buzz += 1
    else: 
        print(numero)
        contatore_nessuno += 1

print(f"contatore Fizz -> {contatore_Fizz}")
print(f"contatore Buzz -> {contatore_Buzz}")
print(f"contatore FizzBuzz -> {contatore_FizzBuzz}")
print(f"contatore nessuno -> {contatore_nessuno}")

```

