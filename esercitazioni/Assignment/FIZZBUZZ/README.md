# FIZZBUZZ(v 1.0)

## OBIETTIVO

E un classico esercizio di programmazione usato spesso nei colloqui tecnico per testare le capacità di scrivere codice semplice e logico
Per ogin numero da 1 a 100:

 - Se il numero è divisibileper 3, stampa "Fizz"
 - Se è divisibile per 5, stampa "Buzz"
 - Se è divisibile per entrambi, stampa "FizzBuzz".
 - Altrimenti, stampa il numero

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
## Implementazione
Il programma deve stampare i numeri da 1 a 100, applicando le regole sopra desscritte
