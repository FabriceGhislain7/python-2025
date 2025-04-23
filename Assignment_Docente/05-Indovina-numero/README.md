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
import random

# Il computer genera un numero casuale tra 1 e 10
numero_casuale = random.randint(1, 10)

indovinato = False      # Flag per indicare se l'utente ha indovinato
tentativi = 0           # Contatore dei tentativi effettuati
tentativi_massimi = 3   # 
punteggio = 10          # Punteggio iniziale
penalita = 2            # Punti persi ad ogni errore

print("Benvenuto! Hai 3 tentativi per indovinare il numero tra 1 e 10.")
print("Inizi con 10 punti. Ogni errore ti costa 2 punti.")

while not indovinato and tentativi < tentativi_massimi:
    tentativo = input("Inserisci un numero: ")

    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    tentativo = int(tentativo)
    tentativi += 1

    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        punteggio -= penalita
        if tentativo > numero_casuale:
            print("Il numero è troppo alto.")
        else:
            print("Il numero è troppo basso.")

        if tentativi < tentativi_massimi:
            print("Sbagliato! Tentativi rimasti:", tentativi_massimi - tentativi)

if indovinato:
    print(f"Hai impiegato {tentativi} tentativo/i.")
    print(f"Il tuo punteggio finale è: {punteggio} punti.")
else:
    print("Game Over! Hai esaurito i tentativi.")
    print(f"Il numero corretto era: {numero_casuale}")
    print(f"Il tuo punteggio finale è: {punteggio} punti.")
```
# INDOVINA NUMERO (V 5.0)
## Obiettivo

Implementare **Livelli di Difficoltà:** Permetti all'utente di scegliere tra diversi livelli di difficoltà che modificano il munero di punti sottratti o l'intervallo dei numeri o il numero di tentativi disponibili

I livelli di difficoltà possono essere:
   - Facile: 1-10, 3 tentativi, 2 punti di penalità
   - Medio: 1-20, 5 tentativi, 3 punti di penalità
   - Difficile: 1-50, 7 tentativi, 4 punti di penalità

## Implementazione

1. Aggiungere un menu per scegliere il livello di difficolta.
2. Modificare il punteggio e i tentativi in base al livello scelto.
3. Modificare l'intervallo dei numeri in base al livello scelto.
4. Modificare la penalità in base al livello scelto.
5. Mostrare il punteggio finale e il numero di tentativi effettuati.

```python
import random

print("Scegli il livello di difficoltà:")
print("1 - Facile   (1-10, 3 tentativi, -2 punti per errore)")
print("2 - Medio    (1-20, 5 tentativi, -3 punti per errore)")
print("3 - Difficile(1-50, 7 tentativi, -4 punti per errore)")

# Selezione livello
scelta = input("Inserisci il numero del livello (1/2/3): ")

if scelta == "1":
    livello = "Facile"
    limite_superiore = 10
    tentativi_massimi = 3
    penalita = 2
elif scelta == "2":
    livello = "Medio"
    limite_superiore = 20
    tentativi_massimi = 5
    penalita = 3
elif scelta == "3":
    livello = "Difficile"
    limite_superiore = 50
    tentativi_massimi = 7
    penalita = 4
else:
    print("Scelta non valida. Verrà impostato il livello Facile.")
    livello = "Facile"
    limite_superiore = 10
    tentativi_massimi = 3
    penalita = 2

# Imposta il numero da indovinare e punteggio iniziale
numero_casuale = random.randint(1, limite_superiore)
punteggio = 10
tentativi = 0
indovinato = False

print(f"\nHai scelto il livello: {livello}")
print(f"Indovina un numero tra 1 e {limite_superiore}")
print(f"Hai a disposizione {tentativi_massimi} tentativi.")
print(f"Ogni errore costa {penalita} punti. Parti da 10 punti!")

# Inizio del gioco
while not indovinato and tentativi < tentativi_massimi:
    tentativo = input("\nInserisci un numero: ")

    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    tentativo = int(tentativo)
    tentativi += 1

    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        punteggio -= penalita
        if tentativo > numero_casuale:
            print("Troppo alto.")
        else:
            print("Troppo basso.")

        if tentativi < tentativi_massimi:
            print(f"Tentativi rimasti: {tentativi_massimi - tentativi}")

# Risultato finale
print("\n=== RISULTATO ===")
if indovinato:
    print(f"Hai indovinato in {tentativi} tentativo/i.")
else:
    print("Game Over! Hai esaurito i tentativi.")
    print(f"Il numero corretto era: {numero_casuale}")

# Evita punteggio negativo
if punteggio < 0:
    punteggio = 0

print(f"Punteggio finale: {punteggio} punti.")
```
# INDOVINA NUMERO (V 6.0)
## Obiettivo

**Storico dei Tentativi:** Mostra all'utente tutti i numeri inseriti precedentemente

## Implementazione

- Utilizza una lista per memorizzare i tentativi dell'utente.
- I tentativi sono memorizzati fino a quando l'utente indovina il numero o esaurisce i tentativi ma vengono persi quando vieneincominciata la partita successiva

```python
import random

print("Scegli il livello di difficoltà:")
print("1 - Facile   (1-10, 3 tentativi, -2 punti per errore)")
print("2 - Medio    (1-20, 5 tentativi, -3 punti per errore)")
print("3 - Difficile(1-50, 7 tentativi, -4 punti per errore)")

# Selezione livello
scelta = input("Inserisci il numero del livello (1/2/3): ")

if scelta == "1":
    livello = "Facile"
    limite_superiore = 10
    tentativi_massimi = 3
    penalità = 2
elif scelta == "2":
    livello = "Medio"
    limite_superiore = 20
    tentativi_massimi = 5
    penalità = 3
elif scelta == "3":
    livello = "Difficile"
    limite_superiore = 50
    tentativi_massimi = 7
    penalità = 4
else:
    print("Scelta non valida. Verrà impostato il livello Facile.")
    livello = "Facile"
    limite_superiore = 10
    tentativi_massimi = 3
    penalità = 2

# Imposta il numero da indovinare e punteggio iniziale
numero_casuale = random.randint(1, limite_superiore)
punteggio = 10
tentativi = 0
indovinato = False
storico_tentativi = []

print(f"\nHai scelto il livello: {livello}")
print(f"Indovina un numero tra 1 e {limite_superiore}")
print(f"Hai a disposizione {tentativi_massimi} tentativi.")
print(f"Ogni errore costa {penalità} punti. Parti da 10 punti!")

# Inizio del gioco
while not indovinato and tentativi < tentativi_massimi:
    tentativo = input("\nInserisci un numero: ")

    if not tentativo.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    tentativo = int(tentativo)
    storico_tentativi.append(tentativo)
    tentativi += 1

    if tentativo == numero_casuale:
        print("Complimenti! Hai indovinato il numero!")
        indovinato = True
    else:
        punteggio -= penalità
        if tentativo > numero_casuale:
            print("Troppo alto.")
        else:
            print("Troppo basso.")

        if tentativi < tentativi_massimi:
            print(f"Tentativi rimasti: {tentativi_massimi - tentativi}")
            print("Tentativi precedenti:", storico_tentativi)

# Risultato finale
print("\n=== RISULTATO ===")
if indovinato:
    print(f"Hai indovinato in {tentativi} tentativo/i.")
else:
    print("Game Over! Hai esaurito i tentativi.")
    print(f"Il numero corretto era: {numero_casuale}")

# Evita punteggio negativo
if punteggio < 0:
    punteggio = 0

print(f"Punteggio finale: {punteggio} punti.")
print("Storico dei tuoi tentativi:", storico_tentativi)

# stampare una lista di numeri casuali con join
lista_numeri = [str(num) for num in storico_tentativi]
print("I tuoi tentativi sono:", ", ".join(lista_numeri))
```