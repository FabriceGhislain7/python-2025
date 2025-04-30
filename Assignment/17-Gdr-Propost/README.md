# Gioco di Combattimento - GDR Didattico in Python

Questo progetto è un **gioco di ruolo (GDR)** sviluppato con l'obiettivo **didattico** di esercitarsi nell'utilizzo della **programmazione ad oggetti (OOP)** in Python. Il progetto integra anche l’uso di **metodi statici** per operazioni utilitarie e gestione globale del gioco.

## Obiettivo del Progetto

L'obiettivo principale è simulare un **torneo tra personaggi** (come maghi, guerrieri e ladri), ognuno dotato di **oggetti** con abilità speciali, all’interno di un sistema ben strutturato in moduli.

---

## 🗂️ Struttura del Progetto

```
📁 Gioco-di-combattimento/
│
├── inventario/
│   ├── __init__.py
│   └── inventario.py         # Classe per gestire l'inventario del Pers. 
│
├── oggetti/
│   ├── __init__.py
│   └── oggetto.py            # Classi(Oggetto, PozioneCura, BombaAcida..)
│
├── personaggi/
│   ├── __init__.py
│   ├── classi.py             # Classi specifiche (Guerriero, Mago, Ladro)
│   └── personaggio.py        # Classe base Personaggio
│
├── torneo/
│   ├── __init__.py
│   ├── torneo.py             # Classe per la gestione del torneo
│   └── turno.py              # Classe per la gestione dei turni di gioco
│
├── utils/
│   ├── __init__.py
│   ├── creation.py           # File per la creazione e la geszione dei files e cartelle del progetto 
│   ├── interfaccia.py        # Interfaccia utente per l’interazione(contenendo funzioni statiche  `@staticmethod`)
│   └── utils.py              # Funzioni di utilità generali(messaggio di benvenuto)
│
├── main.py                   # Punto di ingresso del gioco
├── setup.py                  # Script per installazione e dipendenze
└── README.md                 # Questo file
```

---

## Classi Principali

- **Personaggi**
  - `Personaggio`: Classe base
  - `Guerriero`, `Mago`, `Ladro`: Sottoclassi con abilità uniche

- **Oggetti**
  - `Oggetto`: Classe base
  - `Pozione`, `Bomba`, `Scudo`, ecc.: Oggetti con effetti speciali

- **Inventario**
  - Gestione di oggetti per ogni personaggio

- **Torneo**
  - Sistema di scontri a turni, gestione dei round e dei vincitori

- **Utils**
  - Metodi statici per generazione e supporto (es. `creation.py`, `utils.py`)

---

## ⚙️ Requisiti

- Python 3.10+
- Nessuna libreria esterna necessaria

---

## ▶️ Avvio del Gioco

Esegui il file principale per iniziare una sessione:

```bash
python main.py
```

Segui le istruzioni a schermo per creare i personaggi, selezionare gli oggetti e iniziare il torneo.

---

## 🧠 Obiettivi Didattici

✅ Comprendere l'uso della programmazione a oggetti  
✅ Lavorare con ereditarietà e polimorfismo  
✅ Usare metodi statici per organizzare meglio il codice  
✅ Gestire un progetto Python strutturato in pacchetti e moduli  

---

## 📌 Note Finali

Questo progetto è pensato come **esercitazione per studenti** del corso di programmazione orientata agli oggetti. Può essere ampliato con nuove classi di personaggi, più oggetti, interfaccia grafica, salvataggio del gioco e altro ancora!

