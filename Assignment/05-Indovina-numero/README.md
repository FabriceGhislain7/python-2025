# INDOVINA NUMERO (V 1.0)
## Obiettivo

Creare una applicazione che permetta di indovinare un **numero casuale** generato dal computer.

1. Il computer genera un numero casuale tra 1 e 10.
2. L'utente inserisce un numero.
3. Il computer confronta il numero inserito con quello generato.
4. Se il numero inserito è uguale a quello generato, l'utente ha indovinato.
6. Il gioco termina quando l'utente indovina il numero.

## Implementazione

1. Utilizzare la libreria `random` per generare il numero casuale.
2. Utilizzare un ciclo `while` per ripetere l'input dell'utente fino a quando non indovina il numero.
3. Utilizzare un'istruzione `if` per confrontare il numero inserito con quello generato.

```python
import random

# Il computer genera un numero casuale tra 1 e 10
numero_casuale = random.randint(1, 10)

indovinato = False  # Flag per indicare se l'utente ha indovinato

# Continua a chiedere finché l'utente non indovina
while not indovinato:
    # Input utente
    tentativo = input("Inserisci un numero: ")
    
    # Verifica che l'input sia un numero
    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue # Salta il resto del ciclo e ricomincia

    tentativo = int(tentativo)

    # Confronto
    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        print("Sbagliato! Riprova.")
```
# INDOVINA NUMERO (V 2.0)
## Obiettivo

Implementare un semplice sistema di **suggerimenti**

## Implementazione

1. Aggiungere un suggerimento per indicare se il numero inserito è maggiore o minore di quello generato.

```python

```