# setup.py
- Il file `setup.py` è un file di configurazione utilizzato per creare e distribuire pacchetti Python.
- Contiene informazioni sul pacchetto, come nome, versione, autore e dipendenze.
- È possibile utilizzare `setup.py` per installare il pacchetto localmente o distribuirlo su PyPI (Python Package Index).
- **Devi metterlo nella root del progetto, insieme a main.py**

## A cosa serve installarlo invece che copiarlo
Quando installi (pip install .) un progetto, Python fa queste cose importanti:


Funzione | Cosa fa esattamente
---|---
Copia automatica | Copia il tuo pacchetto dentro la cartella ufficiale di Python (site-packages)
Rende disponibile ovunque | Da qualsiasi cartella puoi fare import torneo, import personaggi, ecc., senza toccare i percorsi
Gestisce dipendenze | Se il progetto avesse librerie esterne (es. numpy, requests), pip le installa automaticamente
Crea dati descrittivi | Python sa che versione del tuo pacchetto è installata (es. 0.1.0)
Aggiornamento facile | Puoi aggiornare il pacchetto con un semplice pip install . --upgrade
Preparazione per PyPI | Se un giorno vuoi caricarlo online come pacchetto pubblico, sei già pronto

## Se invece copio a mano i files

Cosa succede | Limiti
---|---
Funziona, sì | Ma devi sempre gestire tu i percorsi a mano (PYTHONPATH, sys.path.append, ecc.)
Nessuna gestione versioni | Nessun modo semplice di sapere quale versione è usata
Niente dipendenze automatiche | Devi installare a mano ogni libreria esterna
Meno ordine | Più errori possibili su progetti più grandi

# setup.py
setup.py
```python
from setuptools import setup, find_packages  # Importa le funzioni necessarie
# setuptoos e il gestore di pacchetti Python
# setup e il modulo che gestisce le funzionalita di importazione
# find_packages serve a rendere accessibile il package creato in ambiente PyPi
setup(
    name="gioco_torneo",  # Nome del pacchetto (metti un nome breve, tipo gioco_torneo)
    version="0.1.0",  # Versione iniziale (0.1.0 è perfetto per ora)
    description="Gioco di combattimento a torneo con classi, oggetti e turni",
    author="Il Tuo Nome",
    packages=find_packages(),  # Cerca automaticamente tutte le cartelle con __init__.py
    install_requires=[],  # Dipendenze esterne (vuoto, perché in questo caso usiamo solo Python base)
    python_requires=">=3.8",  # Versione minima consigliata di Python
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],  # Categorie per PyPI o documentazione
)
```
# Installare localmente il tuo progetto con pip install .
- eseguire il comando `pip install .` nella cartella principale del progetto (dove c'è setup.py)
- Questo installerà il pacchetto localmente, rendendolo disponibile per l'importazione in altri script Python.

> Facendo pip install .

- Il punto . significa "installa questo progetto dalla cartella attuale"
- Pip legge il file setup.py
- Capisce che cartelle e moduli (torneo, personaggi, inventario, ecc.) deve installare
- Li copia nella cartella di `site-packages` di Python (dove stanno tutte le librerie)
- I moduli sono disponibili ovunque sul tuo computer
- Ora da qualsiasi file Python puoi scrivere:
```python
from torneo.torneo import Torneo
from personaggi.classi import Guerriero
```

> Se vogliamo disinstallarlo
- Esegui il comando `pip uninstall gioco_torneo` per rimuovere il pacchetto installato.

> Meglio installarlo dentro un virtual environment (env)
- Se modifichi il progetto o sbagli qualcosa, basta cancellare la cartella dell'env

Altrimenti senza venv il package viene installato in `site-packages` della installazione di Python

# Crea l'ambiente virtuale
```bash
python -m venv env  # Crea un ambiente virtuale chiamato "env"
```
Attiva l'ambiente virtuale
```bash
# Windows
env\Scripts\activate  # Attiva l'ambiente virtuale su Windows
# Linux/Mac
source env/bin/activate  # Attiva l'ambiente virtuale su Linux/Mac
```
Disattiva l'ambiente virtuale
```bash
deactivate  # Disattiva l'ambiente virtuale
```
> Se vuoi installare il pacchetto in un ambiente virtuale, attiva l'ambiente e poi esegui `pip install .` come prima cosa.
- In questo modo, il pacchetto sarà installato solo all interno dell'ambiente virtuale e non influenzerà il resto del sistema.
- Questo è utile per evitare conflitti tra diverse versioni di pacchetti o progetti.