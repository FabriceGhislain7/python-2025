# SORTEGGIO (V1.0)

## Obiettivo 

Scrive un programma che permette di sorteggiare un numero casuale di partecipanti a un evento e dividerli in due squadre 

## Implementazione
 - l'enlenco dei partecipanti è inizialmente memorizzata su una lista.
 - Successivamente, assegna i partecipanti disponibili alle squadre in modo casuale.
 - i partecipanti che avanzano vengono assegnati alla squadra che vogliamo

Se i partecipanti sono 10 , il programma farà due squadre di 3 poi una squadra di 4
```python 

partecipaanti = [
    "Partecipante 1", "Partecipante 2", "Partecipante 3", "Partecipante 4", "Partecipante 5",
    "Partecipante 6", "Partecipante 7", "Partecipante 8", "Partecipante 9", "Partecipante 10",
]

# Generiamo le nostre squadre di partecipanti
squadra1 = []
squadra2 = []

for i in range(len(partecipaanti)):
    if i % 2 == 0:
        squadra1.append(partecipaanti[i])
    else:
        squadra2.append(partecipaanti[i])

# stampa con il join
print(f"Squadra 1: {",".join(squadra1)}")
print(f"Squadra 1: {",".join(squadra1)}")

```
### ALTRO METODO DI STAMPARE
```python

# Stampa con il for 
print("Squadra 1:")
for nome in squadra1:
    print(nome)
print("Squadra 2:")
for nome in squadra2:
    print(nome)

# stampa con il join
print("Squadra 1:")
print(",".join(squadra1))
print("Squadra 2:")
print(",".join(squadra2))

```

# SORTEGGIO (V2.0)

## Obiettivo 

 - Visualizzare il numero dei partecipanti per squadra 
 - Sorteggi multipli in sequenza (Premi INVIO oer fare un nuovo sorteggio...).
 - Permettere all'utente di aggiungere partecipanti prima del sorteggio.
 - Mostrare chi è il capitano della squadra (es. primo della lista).

Se i partecipanti sono 10 , il programma farà due squadre di 3 poi una squadra di 4

## Suggerimenti 
Posso usare delle list, funzione copy()
# SORTEGGIO (V3.0)

## Obiettivo 

Scrive un programma che permette di sorteggiare un numero casuale di partecipanti a un evento e dividerli in due squadre 

## Implementazione
 - l'enlenco dei partecipanti è inizialmente memorizzata su una lista.
 - il programma chiede all'utente il numero di squadra in cui dividerli.
 - Successivamente, genera un numero casuale di partecipanti e li assegna alle squadre in modo casuale.
 - il programma genera le liste delle squadre e le stampa a video.

Se i partecipanti sono 10 , il programma farà due squadre di 3 poi una squadra di 4

## Suggerimenti 
Posso usare 