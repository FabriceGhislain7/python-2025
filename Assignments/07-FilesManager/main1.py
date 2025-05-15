import os
import shutil
from datetime import datetime

sorgente = input("Cartella da salvare: ")  # Percorso della cartella sorgente o nome della cartella 
destinazione = input("Cartella destinazione backup: ") # Percorso della cartella di destinazione o nome della cartella


if not os.path.exists(sorgente):
    print(f"La cartella sorgente '{sorgente}' non esiste.")
    os.makedirs(sorgente) # 
else:
    print(f"La cartella di destinazione '{destinazione}' esiste già. Procedo con il backup...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # crea un timestamp uninco per la cartella di backup
    backup_folder = os.path.join(destinazione, f"backup_{timestamp}") # Crea un percorso per la cartella di backup
    # in pratica crea un percorso per un percorso completo pe la cartella di backup dove gli argomenti sono:
    # (destinazione, f"backup_{timestamp}") cioe la carta di destinazione + il nome della cartella di backup quindi lo facciamo dentro 
    os.makedirs(backup_folder, exist_ok=True) # Crea la cartella di backup se non esiste

    # itero su tutti i file e le cartelle nella cartella sorgente
    for filename in os.listdir(sorgente):
        source_file = os.path.join(sorgente, filename) # Ottiene il percorso completo del file sorgente
        # Ottengo il percorso completo del file sorgente
        if os.path.isfile(source_file):  # Controlla se è un file 
            shutil.copy(source_file, backup_folder)  # Copia il file nella cartella di backup

    print(f"Backup completato in {backup_folder}") # Stampa il percorso della cartella di backup