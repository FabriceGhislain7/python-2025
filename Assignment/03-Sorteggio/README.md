# SORTEGGIO (V 1.0)
## Obiettivo
Scrivere un programma che permetta di sorteggiare i partecipanti a un evento e dividerli in due squadre in modo casuale.

## Implementazione
- L'elenco dei partecipanti inizialmente è memorizzato su una lista.
- Successivamente, assegna i partecipanti disponibili alle squadre in modo casuale.
- i  partecipanti che avanzano vengono assegnati alla squadra che vogliamo

## Suggerimenti
> Posso stampare la lista dei partecipanti usando il metodo `join` cosi `print(", ".join(partecipanti))` dove partecipanti è la lista dei partecipanti.

```python
import random

partecipanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3", "Partecipante 4", "Partecipante 5",
    "Partecipante 6", "Partecipante 7", "Partecipante 8", "Partecipante 9", "Partecipante 10", "Partecipante 11"
]

# Mischio i partecipanti per rendere il sorteggio casuale
random.shuffle(partecipanti)

 Creo le liste vuote per le squadre
squadra1 = [] # Creo una lista vuota per la squadra 1
squadra2 = [] # Creo una lista vuota per la squadra 2

# ciclo in modo da assegnare i partecipanti alle squadre in modo alternato
for i in range(len(partecipanti)):
    if i % 2 == 0:  # se il resto della divisione tra i e 2 è 0
        squadra1.append(partecipanti[i]) # aggiungo il partecipante alla squadra 1
    else:
        squadra2.append(partecipanti[i]) # altrimenti aggiugo il partecipante alla squadra 2

# stampa con il join e f-string (interpolazione di stringhe)
print(f"Squadra 1: {', '.join(squadra1)}")
print(f"Squadra 2: {', '.join(squadra2)}")
```

### STAMPA ALTERNATIVA
```python
# queste sono due alternative di stampa

# stampa con il for
print("Squadra 1:")
for nome in squadra1:
    print(nome)
print("\nSquadra 2:")
for nome in squadra2:
    print(nome)

# stampa con il join
print("Squadra 1:")
print(", ".join(squadra1))
print("Squadra 2:")
print(", ".join(squadra2))
```
# SORTEGGIO (V 2.0)
## Obiettivo
Implementare le seguenti funzionalità:
- Visualizzare il numero di partecipanti per squadra
- Sorteggi multipli in sequenza (Premi INVIO per fare un nuovo sorteggio...)
- Permettere all’utente di aggiungere partecipanti prima del sorteggio
- Mostrare chi è il capitano della squadra (es. primo della lista)

## Suggerimenti
- Posso accedere ad un elemento specifico di una lista cosi `partecipanti[0]` dove partecipanti è la lista dei partecipanti.

```python
import random

partecipanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3",
    "Partecipante 4", "Partecipante 5", "Partecipante 6",
    "Partecipante 7", "Partecipante 8", "Partecipante 9",
    "Partecipante 10", "Partecipante 11"
]

# Aggiunta partecipanti extra
while True:
    nuovo = input("Aggiungi un partecipante (o premi INVIO per terminare): ")
    if nuovo == "":
        break
    partecipanti.append(nuovo)

# Ciclo per sorteggi multipli
while True:
    random.shuffle(partecipanti)

    squadra1 = []
    squadra2 = []

    for i in range(len(partecipanti)):
        if i % 2 == 0:
            squadra1.append(partecipanti[i])
        else:
            squadra2.append(partecipanti[i])

    print(f"\nSquadra 1 ({len(squadra1)}): {', '.join(squadra1)}")
    print(f"Capitano Squadra 1: {squadra1[0]}") # stampo il capitano della squadra 1
    
    print(f"\nSquadra 2 ({len(squadra2)}): {', '.join(squadra2)}")
    print(f"Capitano Squadra 2: {squadra2[0]}") # stampo il capitano della squadra 2

    risposta = input("\nVuoi sorteggiare di nuovo? (s/n): ").lower()
    if risposta != "s":
        break
```
