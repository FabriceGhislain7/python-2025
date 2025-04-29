# MODULES, PACKAGES, AND NAMESPACES

In Python:

- i moduli sono file di codice sorgente Python che possono essere importati in altri file.
- I pacchetti sono directory che contengono moduli e un file speciale chiamato `__init__.py`.
- I namespace sono spazi in cui i nomi delle variabili, funzioni e classi sono definiti e gestiti.

Perché dividere in file (e moduli)?

Senza divisione (tutto in uno) | Con divisione (file separati)
---|---
File unico gigante da gestire | File piccoli, facili da leggere
Confusione se il progetto cresce | Ogni file ha un solo scopo
Difficile trovare errori o cambiare cose | Puoi lavorare su singole parti
Nessuna riusabilità | Puoi riutilizzare classi/oggetti in altri progetti
Più errori di distrazione | Più ordine mentale
Niente espansioni serie | Puoi costruire espansioni, DLC, mod facilmente

Vantaggi pratici subito:

Senza divisione (tutto in uno) | Con divisione (file separati)
---|---
Tutto in un file | Ogni file ha il suo scopo
Difficile trovare errori | Facile trovare errori
Difficile cambiare cose | Cambi solo quello che serve
Difficile riutilizzare | Riusi facilmente
Difficile testare | Testi facilmente

## __init__.py
In Python, il file `__init__.py` serve principalmente a due scopi:

Indicare che una cartella è un "package":
Quando Python vede un file `__init__.py` in una cartella, capisce che quella cartella può essere trattata come un modulo o package importabile.

> Prima di Python 3.3 era obbligatorio avere `__init__.py` per far riconoscere una cartella come package.

Da Python 3.3 in poi, grazie ai "namespace packages", non è più obbligatorio, ma è comunque consigliato metterlo, soprattutto in progetti ordinati o complessi.

## Eseguire codice di inizializzazione:
Dentro `__init__.py` puoi scrivere codice che vuoi venga eseguito automaticamente quando il package viene importato.

Per esempio, puoi:
- Importare automaticamente dei moduli
- Definire variabili o funzioni di uso comune
- Configurare impostazioni iniziali

Esempio semplice:

Supponiamo che hai questa struttura di cartelle:

```bash
mio_progetto/
│
├── modulo1.py
├── modulo2.py
└── __init__.py
```
Se dentro `__init__.py` scrivi:

```python
print("Inizializzazione del package mio_progetto")
```
Quando importi mio_progetto:

```python
import mio_progetto
```
Vedrai:

```python
Inizializzazione del package mio_progetto
```
## Importare moduli e pacchetti
Import precisi e ordinati:
```python
from prodotti.articolo import Articolo
from prodotti.prodotto import Prodotto
from prodotti.inventario import Inventario
```
Non usare mai:
```python
from prodotti import *
from prodotti.articolo import *
from prodotti.prodotto import *
from prodotti.inventario import *
```
**Manutenzione facilissima:**

Se vuoi cambiare come funziona l'inventario, modifichi solo inventario.py.

**Espansione futura semplice:**

Aggiungere nuove classi, tipi di oggetti diventa banalissimo.

**Test automatici più facili:**

Se vuoi, puoi testare una classe per volta in futuro.

**Professionalità:**

Se mandi il progetto a qualcuno o lo metti su GitHub, sembra subito professionale.

## 1. Moduli
- Un modulo è un file Python che contiene definizioni e istruzioni.
- I moduli possono essere importati in altri moduli o script Python.
- Per importare un modulo, si utilizza la parola chiave `import` seguita dal nome del modulo.
- Esempio:
```python
# modulo.py
def stampa(nome):
    print(f"Ciao, {nome}!")
```
```python
# main.py
import modulo
modulo.stampa("Nome")
```
- È possibile importare solo una parte di un modulo utilizzando la sintassi `from modulo import funzione`.
- Esempio:
```python
# main.py
from modulo import stampa
stampa("Nome")
```
- È possibile importare un modulo con un alias utilizzando la sintassi `import modulo as m`.
- Esempio:
```python
# main.py
import modulo as m
m.stampa("Nome")
```
- È possibile importare tutti i membri di un modulo utilizzando la sintassi `from modulo import *`, ma non è consigliato poiché può causare conflitti di nomi.
- Esempio:
```python
# main.py
from modulo import *
stampa("Nome")
```
- È possibile utilizzare la funzione `dir()` per visualizzare gli attributi e i metodi di un modulo.
- Esempio:
```python
# main.py
import modulo
print(dir(modulo))
```
- È possibile utilizzare la funzione `help()` per visualizzare la documentazione di un modulo.
- Esempio:
```python
# main.py
import modulo
help(modulo)
```
- È possibile utilizzare la funzione `__name__` per verificare se un modulo è stato eseguito come script principale o importato in un altro modulo.
- Esempio:
```python
# modulo.py
if __name__ == "__main__":
    print("Il modulo è stato eseguito come script principale.")
else:
    print("Il modulo è stato importato in un altro modulo.")
```
- È possibile utilizzare la funzione `__all__` per definire quali membri di un modulo devono essere importati quando si utilizza la sintassi `from modulo import *`.
- Esempio:
```python
# modulo.py
__all__ = ["stampa"]
def stampa(nome):
    print(f"Ciao, {nome}!")
def arrivederci(nome):
    print(f"Arrivederci, {nome}!")
```
```python
# main.py
from modulo import *
stampa("Nome")
# arrivederci("Nome")  # Questo causerà un errore poiché arrivederci non è in __all__
```
- È possibile utilizzare la funzione `importlib` per importare moduli in modo dinamico.
- Esempio:
```python
# main.py
import importlib
modulo = importlib.import_module("modulo")
modulo.stampa("Nome")
```

## 2. Pacchetti
- Un pacchetto è una directory che contiene moduli e un file speciale chiamato `__init__.py`.
- Il file `__init__.py` può essere vuoto o contenere codice di inizializzazione per il pacchetto.
- I pacchetti possono essere importati in modo simile ai moduli.
- Esempio:
```python
# pacchetto/modulo.py
def stampa(nome):
    print(f"Ciao, {nome}!")
```
```python
# main.py
from pacchetto.modulo import stampa
stampa("Nome")
```
- È possibile importare un pacchetto con un alias utilizzando la sintassi `import pacchetto as p`.
- Esempio:
```python
# main.py
import pacchetto as p
p.modulo.stampa("Nome")
```
- È possibile utilizzare la funzione `dir()` per visualizzare gli attributi e i metodi di un pacchetto.
- Esempio:
```python
# main.py
import pacchetto
print(dir(pacchetto))
```
- È possibile utilizzare la funzione `help()` per visualizzare la documentazione di un pacchetto.
- Esempio:
```python
# main.py
import pacchetto
help(pacchetto)
```
- È possibile utilizzare la funzione `__all__` per definire quali membri di un pacchetto devono essere importati quando si utilizza la sintassi `from pacchetto import *`.
- Esempio:
```python
# pacchetto/__init__.py
__all__ = ["modulo"]
```
```python
# main.py
from pacchetto import *
modulo.stampa("Nome")
```
```python
# pacchetto/__init__.py
__all__ = ["modulo"]
```
```python
# main.py
from pacchetto import *
modulo.stampa("Nome")
```
- È possibile utilizzare la funzione `importlib` per importare pacchetti in modo dinamico.
- Esempio:
```python
# main.py
import importlib
pacchetto = importlib.import_module("pacchetto")
pacchetto.modulo.stampa("Nome")
```
- È possibile utilizzare la funzione `pkgutil` per esplorare i pacchetti e i moduli all'interno di un pacchetto.
- Esempio:
```python
# main.py
import pkgutil
import pacchetto
for loader, module_name, is_pkg in pkgutil.walk_packages(pacchetto.__path__):
    print(f"Modulo: {module_name}, Pacchetto: {is_pkg}")
```
- Usare la funzione `__path__` per ottenere il percorso di un pacchetto.
- Esempio:
```python
# main.py
import pacchetto
print(pacchetto.__path__)
```

## 3. Namespace
- Un namespace è un contenitore che mappa i nomi degli oggetti ai loro oggetti reali.
- I namespace sono utilizzati per evitare conflitti di nomi tra variabili, funzioni e classi.
- I namespace possono essere globali, locali o incorporati.
- I namespace globali sono accessibili in tutto il modulo.
- I namespace locali sono accessibili solo all'interno di una funzione o di un blocco di codice.
- I namespace incorporati sono forniti da Python e contengono funzioni e variabili predefinite.
- È possibile utilizzare la funzione `globals()` per ottenere il namespace globale.

- Esempio di namespace:
```python
# main.py
x = 10  # Variabile globale
def funzione():
    x = 5  # Variabile locale
    print(f"Namespace locale: {locals()}")  # Mostra il namespace locale
    return x  # Restituisce il valore di x
print(f"Namespace globale: {globals()}")  # Mostra il namespace globale
print(funzione())  # Stampa il valore di x nella funzione
print(x)  # Stampa il valore di x globale
```
- È possibile utilizzare la funzione `globals()` per ottenere il namespace globale.
- Esempio:
```python
# main.py
def funzione():
    x = 10
    print(globals())  # Mostra il namespace globale
    return x  # Restituisce il valore di x
print(funzione())
```
- È possibile utilizzare la funzione `locals()` per ottenere il namespace locale.
- Esempio:
```python
# main.py
def funzione():
    x = 10
    print(locals())  # Mostra il namespace locale
    return x  # Restituisce il valore di x
print(funzione())
```
- È possibile utilizzare la funzione `builtins` per accedere ai namespace incorporati.
- Esempio:
```python
# main.py
import builtins
print(dir(builtins))  # Mostra le funzioni e le variabili incorporate
```
- È possibile utilizzare la funzione `__dict__` per ottenere il namespace di un oggetto.
- Esempio:
```python
# main.py
class Prodotto:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
prodotto = Prodotto("Nome Prodotto")
print(prodotto.__dict__)  # Mostra il namespace dell'oggetto prodotto
```
- È possibile utilizzare la funzione `vars()` per ottenere il namespace di un oggetto.
- Esempio:
```python
# main.py
class Prodotto:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
prodotto = Prodotto("Nome Prodotto")
print(vars(prodotto))  # Mostra il namespace dell'oggetto prodotto
```
- È possibile utilizzare la funzione `__name__` per ottenere il nome del namespace di un modulo o di una classe.
- Esempio:
```python
# main.py
class Prodotto:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
prodotto = Prodotto("Nome Prodotto")
print(prodotto.__class__.__name__)  # Mostra il nome della classe dell'oggetto prodotto
```

## 4. Come funzionano gli import

Se hai i file così:

```bash
catalogo_prodotti/prodotti/prodotto.py
```
Dentro prodotto.py avrai:

```python
from catalogo_prodotti.prodotti import prodotto
```
E in main.py:
```python
# main.py
from catalogo_prodotti.prodotti.prodotto import Prodotto
```