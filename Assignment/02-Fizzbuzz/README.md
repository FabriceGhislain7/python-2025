# FIZZBUZZ (V 1.0)
## Obiettivo
È un classico esercizio di programmazione usato spesso nei colloqui tecnici per testare la capacità di scrivere codice semplice e logico.

Per ogni numero da 1 a 100:
- Se il numero è divisibile per 3, stampa "Fizz".
- Se è divisibile per 5, stampa "Buzz".
- Se è divisibile per entrambi, stampa "FizzBuzz".
- Altrimenti, stampa il numero

## Implementazione
- Il programma deve stampare i numeri da 1 a 100, applicando le regole sopra descritte.

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        # faccio prima il fizzbuzz perche' se metto prima il fizz o il buzz non entra mai nella condizione dove i e' multiplo di 3 e 5
        print(f"{i} -> FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} -> Fizz")
    elif i % 5 == 0:
        print(f"{i} -> Buzz")
    else:
        print(i)
```
# FIZZBUZZ (V 2.0)
## Obiettivo
In questa versione l'utente inserisce un numero qualsiasi ed il programma stampa se il numero è fizz buzz o fizzbuzz.

## Implementazione
- Il programma deve chiedere all'utente di inserire un numero e stampare se il numero è fizz, buzz o fizzbuzz.

```python
numero = int(input("Inserisci un numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print(numero)
```