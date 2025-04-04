# FILE VIEWER (V 1.0)
## Obiettivo

Creare uno script che mostri tutte le cartelle e i file presenti in una directory data, con opzioni per:

- Visualizzare il tipo (file o cartella)
- Visualizzare il nome
- Visualizzare la dimensione
- Visualizzare la data di creazione

## Implementazione

- os.listdir(), os.path.getsize(), os.path.getctime()
- os.path.isdir(), os.path.isfile()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- datetime.fromtimestamp(), strftime()

```python
import os
from datetime import datetime

percorso = input("Inserisci il percorso della directory da esplorare: ")

if not os.path.isdir(percorso):
    print("La directory non esiste.")
else:
    print(f"Contenuto di: {os.path.abspath(percorso)}\n")
    elementi = os.listdir(percorso)
    for elemento in elementi:
        full_path = os.path.join(percorso, elemento)
        tipo = "Cartella" if os.path.isdir(full_path) else "File"
        dimensione = os.path.getsize(full_path)
        data = datetime.fromtimestamp(os.path.getctime(full_path)).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{tipo:8} | {elemento:30} | {dimensione:10} bytes | Creato: {data}")
```
# FILE VIEWER (V 2.0)
## Obiettivo

Implementare un menu di opzioni in modo da poter visualizzare i file o filtrare i files in base ad un estensione specificata dall utente

## Implementazione

- os.listdir(), os.path.getsize(), os.path.getctime(), os.path.splitext()
- datetime, os.path.isfile(), os.path.isdir()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- os.path.splitext()
- datetime.fromtimestamp(), strftime()

```python
import os
from datetime import datetime

percorso = input("Inserisci il percorso della directory da esplorare: ")

if not os.path.isdir(percorso):
    print("La directory non esiste.")
else:
    print(f"Contenuto di: {os.path.abspath(percorso)}\n")

    elementi = []

    for elemento in os.listdir(percorso):
        full_path = os.path.join(percorso, elemento)
        if os.path.isfile(full_path):  # solo file
            tipo = "File"
            dimensione = os.path.getsize(full_path)
            data = datetime.fromtimestamp(os.path.getctime(full_path))
            elementi.append({
                "nome": elemento,
                "dimensione": dimensione,
                "data": data,
                "estensione": os.path.splitext(elemento)[1].lower()
            })

    while True:
        print("\nMENU:")
        print("1. Visualizza tutti i file")
        print("2. Filtra file per estensione")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            for item in elementi:
                print(f"{item['nome']:30} | {item['dimensione']:10} bytes | Creato: {item['data'].strftime('%Y-%m-%d %H:%M:%S')}")

        elif scelta == "2":
            ext = input("Inserisci l'estensione da cercare (es. .txt): ").lower()
            trovati = []
            for elemento in elementi:
                if elemento["estensione"] == ext:
                    trovati.append(elemento)
            # Stampa i file trovati
            print(f"Trovati {len(trovati)} file con estensione {ext}:")
            if trovati:
                for item in trovati:
                    print(f"{item['nome']:30} | {item['dimensione']:10} bytes | Creato: {item['data'].strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"Nessun file con estensione {ext} trovato.")

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")
```
# FILE VIEWER (V 3.0)
## Obiettivo

Creare uno script che mostri tutte le cartelle e i file presenti in una directory data, con opzioni per:

- Visualizzare dimensioni
- Filtrare per estensione
- Ordinare per dimensione

## Implementazione

- os.listdir(), os.path.getsize(), os.path.getctime()
- os.path.isdir(), os.path.isfile()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- os.path.splitext()
- datetime, os.path.isfile(), os.path.isdir()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- os.path.splitext()
- datetime.fromtimestamp(), strftime()

```python
import os  # Importa il modulo os per interagire con il sistema operativo
from datetime import datetime  # Importa la classe datetime per gestire le date e le ore
# la differenza fra modulo e classe è che il modulo è un insieme di funzioni e classi, mentre la classe è un modello per creare oggetti

percorso = input("Inserisci il percorso della directory da esplorare: ")
if not os.path.isdir(percorso):
    print("La directory non esiste.")
else:
    elementi = []  # Inizializza una lista vuota per memorizzare gli elementi
    for elemento in os.listdir(percorso):
        full_path = os.path.join(percorso, elemento)  # Ottiene il percorso completo dell'elemento
        if os.path.isfile(full_path):
            tipo = "File"  # Se l'elemento è un file
        elif os.path.isdir(full_path):
            tipo = "Cartella"  # Se l'elemento è una cartella
        dimensione = os.path.getsize(full_path)  # Ottiene la dimensione dell'elemento
        data = datetime.fromtimestamp(os.path.getctime(full_path))  # Ottiene la data di creazione dell'elemento
        
        elementi.append({  # Aggiunge un dizionario con le informazioni dell'elemento alla lista
            "nome": elemento,
            "tipo": tipo,
            "dimensione": dimensione,
            "data": data,
            "path": full_path
        })

    while True:
        print("\nMENU:")
        print("1. Visualizza tutti")
        print("2. Filtra per estensione")
        print("3. Ordina per data")
        print("4. Ordina per dimensione")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")  # Chiede all'utente di scegliere un'opzione
        
        print("Scelta:", scelta)

        if scelta == "1":
            for item in elementi:
                print(f"{item['tipo']:8} | {item['nome']:30} | {item['dimensione']:10} bytes | Creato: {item['data'].strftime('%Y-%m-%d %H:%M:%S')}")

        elif scelta == "2":
            ext = input("Inserisci l'estensione (es. .txt): ").lower()
            # filtrati = [e for e in elementi if e['nome'].lower().endswith(ext)]
            filtrati = []  # Inizializza una lista vuota per memorizzare gli elementi filtrati
            # Filtra gli elementi in base all'estensione
            for elemento in elementi:
                if elemento['nome'].lower().endswith(ext):  # Controlla se il nome dell'elemento termina con l'estensione specificata e['nome'] indica il campo nome del dizionario
                    filtrati.append(e)
            if not filtrati:
                print("Nessun file trovato con questa estensione.")
            else:
                print(f"Trovati {len(filtrati)} file con estensione {ext}:")
            # Stampa i file filtrati
            for item in filtrati:
                print(f"{item['tipo']:8} | {item['nome']:30} | {item['dimensione']:10} bytes | Creato: {item['data'].strftime('%Y-%m-%d %H:%M:%S')}")

        elif scelta == "3":
            ordinati = []  # Inizializza una lista vuota per memorizzare gli elementi ordinati
            # Ordina gli elementi in base alla data
            for e in elementi:
                ordinati.append(e)
            # ordinati = sorted(elementi, key=lambda x: x['data'], reverse=True)
            ordinati = sorted(ordinati, key=lambda x: x['data'], reverse=True)  # Ordina gli elementi in base alla data
            # key=lambda x: x['data'] indica che vogliamo ordinare in base al campo data del dizionario
            # reverse=True indica che vogliamo ordinare in ordine decrescente
            # Stampa i file ordinati
            print(f"Trovati {len(ordinati)} file ordinati per data:")
            # Stampa i file ordinati
            for item in ordinati:
                print(f"{item['tipo']:8} | {item['nome']:30} | {item['dimensione']:10} bytes | Creato: {item['data'].strftime('%Y-%m-%d %H:%M:%S')}")

        elif scelta == "4":
            ordinati = sorted(elementi, key=lambda x: x['dimensione'], reverse=True)
            for item in ordinati:
                print(f"{item['tipo']:8} | {item['nome']:30} | {item['dimensione']:10} bytes | Creato: {item['data'].strftime('%Y-%m-%d %H:%M:%S')}")

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")
```
# SIMPLE BACKUP (V 1.0)
## Obiettivo

Copiare tutti i file da una directory sorgente a una di backup, aggiungendo timestamp ai nomi dei file o creando una cartella con timestamp

## Implementazione

- os.makedirs(), os.path.isfile(), shutil.copy()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- datetime, os.path.isfile(), os.path.isdir()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- os.path.splitext()
- datetime.fromtimestamp(), strftime()

```python
import os # Importa il modulo os per interagire con il sistema operativo
import shutil # Importa il modulo shutil per operazioni di copia e spostamento di file
from datetime import datetime

sorgente = input("Cartella da salvare: ")  # Chiede all'utente di inserire il percorso o il nome della cartella sorgente
destinazione = input("Cartella destinazione backup: ")  # Chiede all'utente di inserire il percorso o il nome della cartella di destinazione

if not os.path.isdir(sorgente):  # Controlla se la cartella sorgente esiste
    print("La cartella sorgente non esiste.")
else:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Crea un timestamp unico per la cartella di backup
    backup_folder = os.path.join(destinazione, f"backup_{timestamp}")  # Crea un nome unico per la cartella di backup (destinazione) usando os.path.join
    # in pratica crea un percorso completo per la cartella di backup dove gli argomenti sono:
    # (destinazione, f"backup_{timestamp}") cioe la cartella di destinazione e il nome della cartella di backup, quindi la facciamo dentro la cartella di destinazione
    os.makedirs(backup_folder, exist_ok=True)  # Crea la cartella di backup se non esiste già exist_ok=True indica che non deve sollevare un'eccezione se la cartella esiste già
    
    # itero su tutti i files nella cartella sorgente
    for filename in os.listdir(sorgente):
        source_file = os.path.join(sorgente, filename)  # Ottiene il percorso completo del file sorgente
        # ottengo il percorso completo del file sorgente
        if os.path.isfile(source_file):  # Controlla se è un file
            shutil.copy(source_file, backup_folder)  # Copia il file nella cartella di backup
            
    print(f"Backup completato in: {backup_folder}")  # Stampa il percorso della cartella di backup
```
# FILE REPORT (V 1.0)
## Obiettivo

Scansiona una directory e genera un file .txt contenente:

- Nome file
- Estensione
- Dimensione
- Data di creazione
- Path assoluto

## Implementazione

- os.makedirs(), os.path.isfile(), shutil.copy()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- datetime, os.path.isfile(), os.path.isdir()
- os.path.join(), os.path.abspath()
- os.path.isdir(), os.path.isfile()
- os.path.getsize(), os.path.getctime()
- os.path.splitext()
- datetime.fromtimestamp(), strftime()

```python
import os
from datetime import datetime

percorso = input("Inserisci il percorso della directory da analizzare: ")
output = "report.txt"

if not os.path.isdir(percorso):
    print("Directory non trovata.")
else:
    with open(output, "w") as f:
        f.write("Nome File, Estensione, Dimensione (byte), Data Creazione, Path Assoluto\n")
        for file in os.listdir(percorso):
            full_path = os.path.join(percorso, file)  # Ottiene il percorso completo del file
            if os.path.isfile(full_path):
                nome, est = os.path.splitext(file)  # Ottiene il nome e l'estensione del file
                size = os.path.getsize(full_path)  # Ottiene la dimensione del file
                data = datetime.fromtimestamp(os.path.getctime(full_path)).strftime("%Y-%m-%d %H:%M:%S")  # Ottiene la data di creazione del file
                f.write(f"{nome},{est},{size},{data},{os.path.abspath(full_path)}\n")

    print(f"Report salvato in: {output}")
```
# FILE MANAGER (V 1.0)
## Obiettivo

- Separare i files all interno di una folder a seconda della tipologia
- Le folders devono avere il nome dell estensione dei files contenuti

## Implementazione

Scansiona una cartella e sposta ogni file nella sottocartella corretta:

Esempio:
- img.jpg -> jpg/
- song.mp3 -> mp3/
- doc.pdf -> pdf/

- os.makedirs(), os.rename(), os.path.splitext()

```python
import os
import shutil

percorso = input("Inserisci il percorso della cartella da organizzare: ")

if not os.path.isdir(percorso):
    print("Directory non valida.")
else:
    for file in os.listdir(percorso):
        file_path = os.path.join(percorso, file)
        if os.path.isfile(file_path):
            estensione = os.path.splitext(file)[1][1:]  # Questo è un slicing delle stringhe: significa prendi dal secondo carattere in poi
            # oppure invece di usare i due punti si può usare il metodo replace
            # estensione = file.replace(".", "")
            if estensione == "":
                estensione = "senza_estensione"
            cartella_dest = os.path.join(percorso, estensione)
            os.makedirs(cartella_dest, exist_ok=True)
            shutil.move(file_path, os.path.join(cartella_dest, file)) # gli argomenti di move sono il file da spostare e la destinazione

    print("Organizzazione completata.")
```