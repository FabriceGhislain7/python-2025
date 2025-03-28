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
    
    # se il numero è piu alto del numero casuale
    if tentativo > numero_casuale:
        print("Il numero è troppo alto.")
        
    # se il numero è piu basso del numero casuale
    elif tentativo < numero_casuale:
        print("Il numero è troppo basso.")

    # Confronto
    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        print("Sbagliato! Riprova.")
```
# INDOVINA NUMERO (V 3.0)
## Obiettivo

Implementare un sistema di **tentativi limitati** che permetta all'utente di indovinare il numero in un numero fisso di tentativi.

## Implementazione

1. Aggiungere un contatore per tenere traccia dei tentativi effettuati.
2. Limitare il numero di tentativi a 3.
3. Mostrare un messaggio di "Game Over" se l'utente non indovina entro i tentativi consentiti.
4. Mostrare il numero casuale se l'utente non indovina entro i tentativi consentiti.
5. Il gioco termina quando l'utente indovina il numero o esaurisce i tentativi.

```python
import random  # Importa il modulo random

# Il computer genera un numero casuale tra 1 e 10
numero_casuale = random.randint(1, 10)

indovinato = False  # Flag per indicare se l'utente ha indovinato
tentativi = 0       # Contatore dei tentativi massimi
tentativi_massimi = 3

print("Benvenuto! Hai 3 tentativi per indovinare il numero tra 1 e 10.")

# Continua a chiedere finché l'utente non indovina o finisce i tentativi
while not indovinato and tentativi < tentativi_massimi:
    tentativo = input("Inserisci un numero: ")

    # Verifica che l'input sia un numero
    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    tentativo = int(tentativo)
    tentativi += 1  # Aumenta il contatore dei tentativi

    if tentativo > numero_casuale:
        print("Il numero è troppo alto.")
    elif tentativo < numero_casuale:
        print("Il numero è troppo basso.")
    
    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato in", tentativi, "tentativo/i!")
        indovinato = True
    elif tentativi < tentativi_massimi:
        print("Sbagliato! Tentativi rimasti:", tentativi_massimi - tentativi)
    else:
        print("Game Over! Hai esaurito i tentativi.")
        print("Il numero corretto era:", numero_casuale)
```
# INDOVINA NUMERO (V 4.0)
## Obiettivo

Implementare un sistema di **punteggi** che tenga conto del numero di tentativi effettuati.
Più tentativi impiega, minore sarà il punteggio.

## Implementazione

1. Il giocatore inizia con un punteggio tipo 10
2. Ad ogni tentativo fallito sottrai un certo numero di punti tipo 2
3. Alla fine del gioco mostra il punteggio dell utente ed il numero di tentativi

```python

```