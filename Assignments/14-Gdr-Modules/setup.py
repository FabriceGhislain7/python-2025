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