# METODI FILES DIRECTORIES

I metodi per la gestione dei file e delle directory sono essenziali per la manipolazione dei dati e l'interazione con il file system. Python fornisce una serie di metodi integrati per creare, leggere, scrivere, copiare, rinominare ed eliminare file e directory.

```python  
# METODI PER LA GESTIONE DEI FILE E DELLE DIRECTORY

import os  # Libreria per operazioni di file system (os.path, os.makedirs, os.remove, os.rename)
import shutil  # Libreria per operazioni di file system (shutil.copy, shutil.rmtree)
from tempfile import gettempdir, NamedTemporaryFile # gettempdir restituisce la directory temporanea NameTemporaryFile crea un file temporaneo

# Creare un file  
path = "test.txt"  
with open(path, "w") as file:  # Crea un file vuoto w per scrivere, a per aggiungere, r per leggere
    pass  # Crea un file vuoto

# Creare un file con il timestamp  
import datetime  
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  
path = f"test_{timestamp}.txt"  
with open(path, "w") as file:  
    pass

# Scrivere su un file
# la differenza tra write e writelines è che write scrive una stringa mentre writelines scrive una lista di stringhe
with open(path, "w") as file:  
    file.write("Hello, World!")

# Scrivere una lista di stringhe su un file  
lines = ["line 1", "line 2", "line 3"]  
with open(path, "w") as file:  
    file.writelines(f"{line}\n" for line in lines)

# Aggiungere testo a un file  
with open(path, "a") as file:  
    file.write("Hello, World!\n")

# Aggiungere una lista di stringhe a un file  
lines = ["line 1", "line 2", "line 3"]  
with open(path, "a") as file:  
    file.writelines(f"{line}\n" for line in lines)

# Leggere riga per riga da un file  
# utile quando il file è molto grande in quanto non carica tutto in memoria
with open(path, "r") as file:  
    for line in file:  
        print(line.strip()) # strip() rimuove gli spazi bianchi

# Leggere da un file  
# utile quando il file è piccolo in quanto carica tutto in memoria
with open(path, "r") as file:  
    content = file.read()  
print(content)

# Copiare un file  
path2 = "test2.txt"  
shutil.copy(path, path2)

# Rinominare un file  
path3 = "test3.txt"  
os.rename(path2, path3)

# Eliminare un file  
os.remove(path3)

# Creare una directory  
dir_path = "test"  
os.makedirs(dir_path, exist_ok=True)

# Eliminare una directory solo se è vuota
os.rmdir(dir_path)

# eliminare una directory con tutto il contenuto
shutil.rmtree(dir_path)

# Creare un file temporaneo  
# il vantaggio è che viene eliminato automaticamente alla chiusura del programma
with NamedTemporaryFile(delete=False) as temp_file:  
    print(temp_file.name)

# Creare una directory temporanea  
temp_dir = os.path.join(gettempdir(), "temp")  
os.makedirs(temp_dir, exist_ok=True)

# Verificare se un file esiste  
if os.path.exists(path):  
    print("File exists")

# Verificare se una directory esiste  
if os.path.isdir(dir_path):  
    print("Directory exists")

# Ottenere informazioni su un file  
if os.path.exists(path):  
    print(os.path.getsize(path))  # Dimensione del file  
    print(datetime.datetime.fromtimestamp(os.path.getctime(path)))  # Data di creazione

# Fare riferimento a un file con il path completo
path = os.path.join(dir_path, "test.txt")
print(path)

# Fare riferimento solo al path relativo
relative_path = os.path.relpath(path, dir_path)
print(relative_path)

# Fare riferimento solo al nome del file senza il path  
file_name = os.path.basename(path)  
print(file_name)

# Fare riferimento solo all'estensione del file  
extension = os.path.splitext(path)[1]  
print(extension)

# Fare riferimento al nome del file senza estensione  
file_name_without_extension = os.path.splitext(os.path.basename(path))[0]  
print(file_name_without_extension)

# Ottenere informazioni su una directory  
if os.path.isdir(dir_path):  
    print(datetime.datetime.fromtimestamp(os.path.getctime(dir_path))) # Data di creazione
    print(os.path.getsize(dir_path))  # Dimensione della directory
    print(os.listdir(dir_path))  # Contenuto della directory
    print(os.path.abspath(dir_path))  # Path assoluto della directory
    print(os.path.abspath(path))  # Path assoluto del file

# Ottenere informazioni su tutti i file in una directory  
files = os.listdir(dir_path)  
for file in files:  
    print(file)

# Eliminare un file  
os.remove(path)

# Eliminare una directory e tutto il contenuto  
shutil.rmtree(dir_path)

# Eliminare tutti i file in una directory con un filtro  
txt_files = [f for f in os.listdir(dir_path) if f.endswith(".txt")]  
for txt_file in txt_files:  
    os.remove(os.path.join(dir_path, txt_file))  
```

### **Adattamenti per Python**

1. **Creazione e scrittura dei file**:  
   * Python utilizza open() con modalità come "w", "a", e "r".  
   * Le librerie integrate come shutil forniscono funzionalità aggiuntive per copiare e spostare file.  
2. **Lettura e scrittura**:  
   * read() per leggere tutto il contenuto.  
   * readlines() per leggere riga per riga.  
3. **Directory**:  
   * os.makedirs() per creare directory.  
   * shutil.rmtree() per eliminare directory con tutto il contenuto.  
4. **File temporanei**:  
   * Usa NamedTemporaryFile per file temporanei.  
5. **Informazioni sui file e sulle directory**:  
   * os.path e os forniscono metodi per ottenere dettagli come dimensione, creazione, o estensione del file.