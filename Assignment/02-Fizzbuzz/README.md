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
# effettuo la conversione in intero del valore inserito dall'utente in modo da poter effettuare i controlli successivi
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
# FIZZBUZZ (V 3.0)
## Obiettivo
Permette al utente di inserire piu numeri

## Implementazione
L’utente può uscire scrivendo "esci" altrimenti il programma chiede di inserire un altro numero.

> OPZIONALE: usare il metodo `isdigit()` per controllare se l'input è un numero.

```python
while True:
    inserimento = input("Inserisci un numero valido oppure 'esci': ")
    
    if inserimento.lower() == "esci":
        break  # uso break in modo da uscire dal ciclo while
    
    if not inserimento.isdigit():  # uso isdigit per controllare se la stringa è un numero
        print("Per favore inserisci un numero valido oppure 'esci'.\n")
        continue  # uso continue in modo da ripartire dal ciclo while

    numero = int(inserimento) # converto la stringa inserimento in un intero

    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} -> fizzBuzz!\n")
    elif numero % 3 == 0:
        print(f"{numero} -> fizz\n")
    elif numero % 5 == 0:
        print(f"{numero} -> buzz\n")
    else:
        print("Nessuno\n")
```
# FIZZBUZZ (V 4.0)
## Obiettivo
Implementare un contatore in modo da tenere traccia di quante volte sono usciti fizz, buzz, fizzbuzz e nessuno.

## Implementazione
Nel momento in cui l utente scrive esci viene stampato il conteggio.

```python
# Inizializzazione dei contatori
count_fizz = 0
count_buzz = 0
count_fizzbuzz = 0
count_nessuno = 0

while True:
    inserimento = input("Inserisci un numero: ")
    
    # se l'utente inserisce "esci" termina il programma e mostra i risultati
    if inserimento.lower() == "esci":
        print("\n--- Risultati ---")
        print(f"Fizz: {count_fizz}")
        print(f"Buzz: {count_buzz}")
        print(f"FizzBuzz: {count_fizzbuzz}")
        print(f"Nessuno: {count_nessuno}")
        break

    if not inserimento.isdigit():
        print("Per favore inserisci un numero valido oppure 'esci'.\n")
        continue

    numero = int(inserimento)

    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz\n")
        count_fizzbuzz += 1  # incremento il contatore di FizzBuzz
    elif numero % 3 == 0:
        print("Fizz\n")
        count_fizz += 1  # incremento il contatore di Fizz
    elif numero % 5 == 0:
        print("Buzz\n")
        count_buzz += 1  # incremento il contatore di Buzz
    else:
        print("Nessuno\n")
        count_nessuno += 1
```