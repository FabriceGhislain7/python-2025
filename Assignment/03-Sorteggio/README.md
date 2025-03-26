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
print(f"\nSquadra 1: {', '.join(squadra1)}")
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
Scrivere un programma che permetta di sorteggiare un numero casuale di partecipanti a un evento e dividerli in squadre

## Implementazione
- L'elenco dei partecipanti inizialmente è memorizzato su una lista.
- Il programma chiede all'utente il numero di squadre in cui dividerli.
- Successivamente, assegna i partecipanti disponibili alle squadre in modo casuale.
- Il programma genera le liste delle squadre e le stampa a video.
> Se i partecipanti sono 10 e le squadre sono 3 il programma dovrebbe fare 2 squadre da 3 ed una squadra da 4.

## Suggerimenti
- posso trovare il numero di elementi di una lista cosi `num_partecipanti = len(partecipanti)` dove partecipanti è la lista dei partecipanti.
- si puo usare l operatore // per la divisione intera cioè `num_partecipanti // num_squadre` per trovare il numero di partecipanti per squadra.
- si puo usare il metodo `remove` sulla lista per rimuovere un elemento cosi `partecipanti.remove(partecipante)` in modo da rimuovere un partecipante dalla lista.
- si puo usare il metodo `copy` sulla lista per copiarla cosi `squadra1 = partecipanti.copy()` in modo da copiare la lista.
- si puo usare il metodo `append` sulla lista per aggiungere un elemento cosi `squadra1.append(partecipante)` in modo da aggiungere un partecipante alla lista.

```python

```