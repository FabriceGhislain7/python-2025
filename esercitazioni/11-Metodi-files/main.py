# METODI FILES E DIRECTORIES

# FILES

import os  # Libreria per operazioni di file system (os.path, os.makedirs, os.remove, os.rename)
import shutil  # Libreria per operazioni di file system (shutil.copy, shutil.move, shutil.rmtree)
import datetime  # Libreria per operazioni di data e ora (datetime.datetime.now, datetime.timedelta)

# Creare un file
path = "test.txt"
with open(path, "w") as file:  # Crea un file vuoto w per scrivere
    # pass  # Il file viene chiuso automaticamente al termine del blocco with
    file.write("ciao")  # Scrive una stringa nel file
    
# Aggiungere testo a un file
with open(path, "a") as file:  # a per aggiungere (add)
    file.write("\ncome va?")  # Aggiunge una nuova riga e una stringa al file
    file.write("\nsto bene")  # Aggiunge un'altra riga e stringa al file
    
# Scrivere una lista di stringhe su un file
lines = ["line 1", "line 2", "line 3"]
with open(path, "w") as file:
    for line in lines:
        file.write(line + "\n")  # Scrive ogni stringa della lista su una nuova riga
    # oppure
    file.writelines(f"{line}\n" for line in lines)  # Scrive ogni stringa della lista su una nuova riga

# Aggiungere una lista di stringhe a un file
lines2 = ["line 4", "line 5", "line 6"]
with open(path, "a") as file:
    for line in lines2:
        file.write(line + "\n")  # Aggiunge ogni stringa della lista su una nuova riga
    # oppure
    file.writelines(f"{line}\n" for line in lines2)  # Aggiunge ogni stringa della lista su una nuova riga
    
# la differenza tra write e writelines è che write scrive una stringa mentre writelines scrive una lista di stringhe

# Leggere riga per riga da un file
# utile quando il file è molto grande in quanto non carica tutto in memoria
with open(path, "r") as file:
    for line in file:
        print(line.strip())  # Stampa ogni riga del file, rimuovendo gli spazi bianchi iniziali e finali
        
# Leggere da un file
# utile quando il files è piccolo perche viene caricato tutto in memoria
with open(path, "r") as file:  
    content = file.read()  # read legge tutto il file e lo carica in una stringa
print(content)  # Stampa il contenuto del file

# Copiare un file
path2 = "test2.txt"
shutil.copy(path, path2)  # Copia il file test.txt in test2.txt

# Rinominare un file
# os.rename(path2, "test3.txt")  # Rinomina test2.txt in test3.txt

# Eliminare un file
# os.remove("test3.txt")  # Elimina test3.txt
# oppure
# os.remove(path2)  # Elimina test2.txt

# Creare un file con il timestamp
# timestamp = datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%S")  # Ottiene il timestamp corrente
timestamp = datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%S")
path4 = f"test_{timestamp}.txt"
with open(path4, "w") as file:
    # file.write("ciao")  # Scrive una stringa nel file
    pass  # Il file viene chiuso automaticamente al termine del blocco with
    
# Verificare se un file esiste
if os.path.exists(path):  
    print("File exists")
    
# Ottenere informazioni su un file
if os.path.exists(path):
    print(os.path.getsize(path))  # Dimensione del file in byte
    print(datetime.datetime.fromtimestamp(os.path.getctime(path)))  # Data di creazione
    print(datetime.datetime.fromtimestamp(os.path.getmtime(path)))  # Data di modifica
    print(datetime.datetime.fromtimestamp(os.path.getatime(path)))  # Data di accesso
    
# Fare riferimento solo al nome del file senza il path
file_name = os.path.basename(path)  
print(file_name)

# Fare riferimento al nome del file senza estensione
file_name_no_ext = os.path.splitext(file_name)[0]
print(file_name_no_ext)

# Fare riferimento solo all'estensione del file  
extension = os.path.splitext(path)[1]  
print(extension)

# Spostare un file
shutil.move(path, "test2/test.txt")  # Sposta test.txt in test2/test.txt

src = "/home/user/documento.txt"
dst = "/home/user/testi/documento.txt"
shutil.move(src, dst)
    
# DIRECTORIES

#  creazione di una directory
dir_path = "test"  # Nome della directory da creare
os.makedirs(dir_path, exist_ok=True)  # Crea una directory test se non esiste già

# Fare riferimento a un file con il path completo
path = os.path.join(dir_path, "test.txt")
print(path)

# Fare riferimento solo al path relativo
relative_path = os.path.relpath(path, dir_path)
print(relative_path)

# Eliminare una directory solo se è vuota
# os.rmdir(dir_path)  # Elimina la directory solo se è vuota

# eliminare una directory con tutto il contenuto
# shutil.rmtree(dir_path)  # Elimina la directory e tutto il suo contenuto

# Verificare se una directory esiste
if os.path.isdir(dir_path):
    print("Directory exists")
else:
    # creo la directory
    os.makedirs(dir_path)
    print("Directory created")
    
# Ottenere informazioni su una directory  
if os.path.isdir(dir_path):  
    print(datetime.datetime.fromtimestamp(os.path.getctime(dir_path)))  # Data di creazione
    print(os.path.getsize(dir_path))  # Dimensione della directory
    print(os.listdir(dir_path))  # Contenuto della directory
    print(os.path.abspath(dir_path))  # Path assoluto della directory
    # C:\Users\Allievo\Documents\python-2025\Esercitazioni\11-Metodi-files
    # python-2025\Esercitazioni\11-Metodi-files\main.py