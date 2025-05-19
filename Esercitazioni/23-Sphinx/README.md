# SPHINX
## GDR
```bash
gdr/
│
├── personaggio/
│   └── personaggio.py
├── missioni/
│   └── missione.py
├── inventario/
│   └── oggetto.py
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── (altri .rst)
├── main.py
├── requirements.txt
└── venv/
```
Creazione ambiente virtuale
```bash
python -m venv venv
source venv/bin/activate  # Su Windows usa 'venv\Scripts\activate'
```
Installa i pacchetti:
```bash
pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints
```
Crea la struttura del progetto
Da dentro gdr/ (dove c’è main.py), esegui:
```bash
sphinx-quickstart docs
```
Quando chiede:

- Project name: gdr
- Separate source/build: n
- suffix: .rst

Modifica docs/conf.py
```python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # per importare i moduli di personaggio, missioni, ecc.
# sys.path
# Se conf.py è in gdr/docs/	sys.path.insert(0, os.path.abspath('..'))
# Se conf.py è in gdr/docs/source/	sys.path.insert(0, os.path.abspath('../..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints'
]

html_theme = 'sphinx_rtd_theme'
```
Dalla cartella principale (dove c’è main.py), esegui:
Genera i .rst per ogni pacchetto
```bash
sphinx-apidoc -o docs ./personaggi
sphinx-apidoc -o docs ./missioni
sphinx-apidoc -o docs ./inventario
```
Questo creerà file .rst come personaggio.rst, missioni.rst, inventario.rst in docs/

Aggiungi questi moduli nel docs/index.rst
```rst
.. toctree::
   :maxdepth: 2
   :caption: Moduli

   personaggio
   missioni
   inventario
```
Genera l’HTML
in docs/:
```bash
cd docs
make.bat html # per Windows
make html # per Linux
```
Oppure:
```bash
python -m sphinx -b html . _build/html
```
Cambiare themes
```bash
pip install furo
```
 In conf.py:
```python
html_theme = 'furo'
```
Da dentro gdr/ (dove c’è main.py), esegui:
```bash
sphinx-quickstart docs
```
