# RUBRICA JSON CON RICH (V1.0)

## Obiettivo 
Implementare le funzionalità di una rubrica telefonica utilizzando i commandi 
La rubrica deve essere in grado di gestire, numero di telefono e indirizzi maile deve supportare operazioni come aggiunere, modificare e visualizzare i contatti.

Nello specifico, i moduli di Rich che useremo sono:
- Console. Per stampare messaggi e sessioni con stilo  
- Panel:  Per mostrare le sezioni come riquadri
- Prompt: Per Per input utente stilizzati
- Table: per mostrare i contatti attivi in modo tabellare
- Box: Per personalizzare il bordo dei pannelli.
- spinner: Per mostrare un'animazione di caricamento

Gestiremo la console in modo ad ottimizzare la pulizia dello schermo e l'input dell'utente. 

## Suggerimenti
Usare il virtual environment per installare rich:
```bash
# Commando di creazione ambiente virtule
python -m venv venv
# Commando di attivazione ambiente virtuale
venv\Scripts\activate
# Commando di istallazione rich
pip install rich
# Commando di uscita dall'ambiente virtuale
deactivate
# Commando di disistallazione rich
pip install rich

```