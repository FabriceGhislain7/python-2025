# Sphinx

 è un potente generatore di documentazione che può leggere i docstring in stile reStructuredText o Google/Numpy-style dai tuoi file .py e generare documentazione in HTML, PDF o altri formati

creazione ambiente virtuale
```bash
python -m venv venv
source venv/bin/activate 
# Su Windows usa 'venv\Scripts\activate'
```

Passaggi per generare la documentazione in Python con Sphinx

1. Installa Sphinx
```bash
pip install sphinx
```

2. Crea la struttura del progetto

Nella cartella del tuo progetto Python, esegui:

```bash
sphinx-quickstart docs
```
Dovrebbe creare una cartella `docs` con una struttura di base per la documentazione
```bash
progetto_google_doc/
│
├── modulo/
│   └── calcolatrice.py        # Modulo Python con Google-style docstring
│
├── docs/                      # Cartella documentazione Sphinx
│   ├── conf.py                # Configurazione
│   ├── index.rst              # Indice principale
│   ├── modulo.rst             # Documentazione automatica
│   └── _build/                # Output HTML (vuoto finché non esegui `make html`)
│
└── requirements.txt           # (opzionale)
```

3. Configura Sphinx

Apri il file `docs/conf.py` e aggiungi il percorso del tuo progetto Python:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

extensions = [
    'sphinx.ext.autodoc',  # per generare doc dai docstrings
    'sphinx.ext.napoleon', # per supporto Google/Numpy style docstrings
    'sphinx_autodoc_typehints', # mostra i tipi come annotazioni
]

html_theme = 'sphinx_rtd_theme'
```

4. Crea i file .rst per i tuoi moduli

Puoi farlo manualmente o con:
```bash
sphinx-apidoc -o docs/source ../tuo_pacchetto
```

Sostituisci tuo_pacchetto con la cartella che contiene i tuoi file .py

5. Costruisci la documentazione

Esegui:

```bash
cd docs
make html  # oppure 'make.bat html' su Windows
```
Troverai la documentazione HTML in docs/_build/html/index.html