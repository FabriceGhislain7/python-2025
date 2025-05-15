# FILE VIEWER (V1.0)

# Obiettivo
Creare uno  script che mostra tutte le cartelle presenti in una directory datda, con opzioni per:
 - Visualizzare dimensioni 
 - Filtrare estensione
 - Ordinare per data o dimensione

 # Implementazione

 - os.listdir(), os.path.getsize(), os.path.getctime(), os.path.splitext()

 # Codice (codice non terminato)
 ```python
import os 

# Gestione della validità della directory
path_valido = False
while True:
    path_cartella = input("Inserisci il path della directory per accedere al menu: ")
    if path_valido == os.path.exists(path_cartella):
        print("La directory non esite. Inserisce una directory valida.")
        continue
    else:
        print(f"La directory esiste.")
        path_valido = True 
        break
print("-" * 40)

# MENU 
menu = {"1": "Visualizzazione la directory",
        "2": "Filtrare estensione dei files",
        "3": "Ordinare per data",
        "4": "Ordina per dimensione",
        "0": "Esci"}

# print il MENU
for numero, opzione in menu.items():
    print(f"{numero} : {opzione}")

# Gestione scelta
scelta_operazione = ""
while not scelta_operazione in menu:
    scelta_operazione = input("Inserisci il numero dell'operazione: ").strip()

# Esci dal programma se 
if scelta_operazione == "0":
    exit()

# 1. Visualizzo le dimensioni dei files.
if scelta_operazione == "1":
    for cartella in os.listdir(path_cartella):
        print(cartella)

# 2.Filtro per estensione.
if scelta_operazione == "2":
    filtrati = []
    non_filtrati = []  
    input
    for elemento in os.listdir(path_cartella):
        if os.path.splitext(elemento)[1]:       # Questa funzione prende solo nome, non prende path
            filtrati.append(elemento)
        else: 
            non_filtrati.append(elemento)
    for filtrato in non_filtrati:
        print(filtrato)
    
# 3. Ordino i file per data 

# 4. ordino i file per dimensione
if scelta_operazione == "4":
    dim_cartelle = []
    for cartella in os.listdir(path_cartella):
        dim_cartelle.append(os.path.getsize(path_cartella))

 ```
# SIMPLE BACKUP (v 1.0)

# Obiettivo 
Copiare tutti i file da una directory sorgente a una di backup, aggiungendo timestamp ai nomi dei file o creando una cartella non timestamp.

## Implementazione
- shutil.copy(), os.makedirs(), datetime, os.path.join()

### Codice 

# FILE REPORT (V1.0) 
# Obiettivo

Scansiona una directory e genera un file .txt contenente:
 - Nome file 
 - Estensione 
 - Dimensione 
 - Data di creazione 
 - Path assoluto

 ## Implementazione
 - open(), writeline(), os.path.splitext(), os.path.getsize(), os.path.getctime(), os.path.abspath() 
```python
import os
from datetime import datetime

# Gestisco la validità della Cartella scansionata
while True:
    cartella = input("Cartella scansionata: ")
    if os.path.exists(cartella):
        print("La cartella esiste.")
        break
    else: 
        print("Cartella non valida.")
        continue

# Informazioni della cartella principale csansionata
print("la cartella scansionata esiste.")
nome_cartella = os.path.basename(cartella)
data_cartella = datetime.fromtimestamp(os.path.getctime(cartella))
estensione_cartella = os.path.splitext(cartella)[1]
dim_cartella = os.path.getsize(cartella)
path_assoluto = os.path.abspath(cartella)

path_info = input("Cartella da scansionare") + ".txt"

info_scansionata = []
info_scansionata.append(f"Nome della cartella: {nome_cartella}")
info_scansionata.append(f"Data di creazione: {data_cartella}")
info_scansionata.append("estensione_cartella:" + estensione_cartella)
info_scansionata.append("dim_cartella " + str(dim_cartella))
info_scansionata.append("path_assoluto " + path_assoluto)

with open(path_info, "w") as file:
    print("")
    file.writelines(f"{linea}\n" for linea in info_scansionata)

```
# FILE MANAGER

## Obiettivo
 - Separare i files all interno di un folder a seconda della tipogia
 - La folder deve avere il nome dell'estensione dei files contenuti.  

## Implementazione 
Scansione una cartella e sposta ogni file nella sotto cartella corretta:
Esempio:
 - img.jpg -> immagini/
 - song.mp3 -> musica/
 - doc.pdf -> pdf/
 - os.makedirs(), os.rename(), os.path.splitext()

## Codice
```python 
import os
import shutil

# Verifica della validità della cartella_origine.
while True:
    cartella_origine = input("Inserisci la cartella_origine: ")
    if os.path.exists(cartella_origine):
        print("la cartella_origine esiste.")
        break
    else: 
        print("La cartella_origine non esiste.")
        continue

cartella_destinazione = input("Cartella destinazione: ")
os.makedirs(cartella_origine, exist_ok=True)

# Verifica la tipologia di ogni cartella_origine.
for elemento in os.listdir(cartella_origine):
    path_elemento = os.path.join(cartella_origine, elemento)
    if os.path.isfile(path_elemento):
        estensione_file = os.path.splitext(elemento)[1][1:]
        path_cartelle_estensione = os.path.join(cartella_destinazione,estensione_file)
        os.makedirs(path_cartelle_estensione, exist_ok=True)
        shutil.move(path_elemento, path_cartelle_estensione)  
    else:
        print(f"{elemento} non è un file, è una cartella.")
```  