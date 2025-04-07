# CALCOLATRICE RANDOM (V 1.0)
## Obiettivo

Il programma genera a caso due numeri e un’operazione (+, -, *, /), poi chiede all’utente il risultato. Se è corretto, stampa un messaggio
- l ’utente ha 1 tentativo per ogni operazione ed il punteggio viene incrementato di 1 se la risposta è corretta
- il punteggio viene decrementato di 1 se la risposta è errata
- tiene il punteggio e salva i risultati su file
- l utente puo scegliere se riprendere una partita gia incominciata oppure ricominciare da zero tramite un menu di scelta
- il punteggio viene salvato su file e puo essere visualizzato in un secondo momento
- il programma deve essere in grado di gestire gli errori (es. divisione per zero, operazione non valida, ecc.)
- In totale il programma chiedera all utente di risolvere 10 operazioni in modo da conludere la partita

## Argomenti
- Uso di liste e random.shuffle
- Cicli for e while
- Gestione dell'input utente
- Lettura da file txt
- Salvataggio su file .txt in modalità append ("a")
- Gestione di un sistema di punteggio

## Suggerimenti
- Se serve e possibile specificare la codifica del file txt cosi:
> with open("parole.txt", "r", encoding="utf-8") as file:

## Check

- [ ] Menu iniziale: nuova partita o continua
- [ ] 10 operazioni totali (conta i progressi)
- [ ] 1 solo tentativo per ogni operazione
- [ ] +1 punto per risposta corretta, -1 per sbagliata
- [ ] Salvataggio continuo su file
- [ ] Visualizzazione punteggio salvato
- [ ] Gestione errori semplificata

```python

```