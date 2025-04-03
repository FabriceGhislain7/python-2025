# METODI FILES E DIRECTORIES
import os #  Libreria per le operazoni sui file systema, (os.path, os.system, os.remove, os.rename, os.mkdir, os.makedirs, os.rmdir, os.listdir, os.getcwd, os.chdir)
import shutil # Libreria per le operazioni di copia e spostamento dei file (shutil.copy, shutil.move, shutil.rmtree, shutil.copytree)
import datetime # Libreria per la gestione delle date e degli orari (datetime.datetime, datetime.date, datetime.timedelta)

# Creare un file
path = "esercitazioni/11-Metodi-files/test.txt" # Percorso del file creato
# oppure path = "test.txt" # Percorso del file creato
with open(path, "w") as file: # Apre il file in scrittura (write)
    # pass # Il file viene chiuso automaticamente al termine del blocco with
    file.write("Ciao, Antonio.") # Scrive nel file
print("-" * 40)

# Agiungere testo a un file.
with open(path, "a") as file: # a per aggiungere (add)
    file.write("\nCome va?.") # Aggiunge una nuova riga al file
    file.write("\nTutto bene.") # Aggiunge una nuova riga al file

# Scrivere una lista di strighe in un file.
lines = ["line 1", "line 2", "line 3"] # Lista di stringhe
with open(path, "w") as file: # w per scrivere (write)
    for line in lines:
        file.write(line + "\n") # Aggiunge una nuova riga al file
        # oppure
        file.writelines(f"{line}\n" for line in lines) # Aggiunge una nuova riga al file

# Agiungere una lista di strighe a un file.
lines2 = ["line 4", "line 5", "line 6"] # Lista di stringhe
with open(path, "a") as file: # a per aggiungere (add)
    for line in lines2:
        file.write(line + "\n") # Aggiunge una nuova riga al file
        # oppure
        file.writelines(f"{line}\n" for line in lines2) # Aggiunge una nuova riga al file

# La differenza tra write e writelines è che write scrive una stringa,
#  mentre writelines scrive una lista di stringhe.

# Leggere un file riga per riga.
# Utile quando il file è molto grande in quanto non carica tutto il file in memoria.
with open(path, "r") as file: # r per leggere (read)
    for line in file:
        print(line.strip()) # Stampa la riga senza il carattere di fine riga

# Leggere da un file 
path_test = "esercitazioni/11-Metodi-files/giardino.txt" # Percorso del file creato
with open(path_test, "a") as file: # r per leggere (read)
    file.write("\nCiao, Antonio.") # Scrive nel file
    file.write("\nCome va?.") # Aggiunge una nuova riga al file
    file.write("\nTutto bene.") # Aggiunge una nuova riga al file

with open(path_test, "r") as file: # r per leggere (read)
    for line in file:
        content = file.read() # Legge tutto il file e lo carica in una stringa
        print(content) # Stampa il contenuto del file

# Coppiare un file.
path2 = "esercitazioni/11-Metodi-files/test2.txt" # Percorso del file creato
shutil.copy(path, path2) # Copia il contenuto del file test.txt in test2.txt

# Rinominare un file.
# os.rename(path2, "esercitazioni/11-Metodi-files/test3.txt") # Rinomina il file test2.txt in test_renamed.txt

# Eliminare un file.
# os.remove(path2) # Elimina il file test2.txt
# oppure 
# os.remove("esercitazioni/11-Metodi-files/test2.txt") # Elimina il file test2.txt
# oppure


# Creare un file con il timestamp.
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Crea un timestamp corrente.
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Crea un timestamp corrente.
path4 = f"test_{timestamp}.txt" # Percorso del file creato
with open(path4, "w") as file: # Apre il file in scrittura (write)
    file.write("Ciao, Antonio.") # Scrive nel file  

# Verificare se un file esiste.
if os.path.exists(path): # Verifica se il file esiste
    print(f"Il file {path} esiste.") # Stampa il messaggio se il file esiste

# Ottenere informazioni su un file.
if os.path.exists(path): # Verifica se il file esiste
    print(os.path.getsize(path)) # Stampa la dimensione del file in byte
    print(datetime.datetime.fromtimestamp(os.path.getmtime(path))) # Stampa la data di creazione
    print(datetime.datetime.fromtimestamp(os.path.getatime(path))) # Stampa la data di accesso
    print(datetime.datetime.fromtimestamp(os.path.getctime(path))) # Stampa la data di modifica

# Fare riferimento solo al nome del file senza il percorso.
file_name = os.path.basename(path) # Ottiene solo il nome del file senza il percorso
print(file_name) # Stampa il nome del file

# Fare riferimento al nome del file senza estensione.
file_name_no_ext = os.path.splitext(file_name)[0] # Ottiene solo il nome del file senza estensione
print(file_name_no_ext) # Stampa il nome del file senza estensione

# Fare riferimento solo all'estensione del file.
extensione = os.path.splitext(file_name)[1] # Ottiene solo l'estensione del file
print(extensione) # Stampa l'estensione del file

# Fare riferimento solo al percorso del file senza il nome.
file_path = os.path.dirname(path) # Ottiene solo il percorso del file senza il nome

# Spostare un file 
shutil.remove(path, "test2/test.txt") # 

# DIRECTORIES
# Creazione di una directory.
dir_path = "test_dir" # Percorso della directory creata
os.makedirs(dir_path, exist_ok=True) # Crea la directory test_dir se non esiste già

# Eliminare una directory solo se è vuota.
os.rmdir(dir_path) # Elimina la directory test_dir se è vuota

# Eliminare una directory e tutto il suo contenuto.
# shutil.rmtree(dir_path) # Elimina la directory test_dir e tutto il suo contenuto

# Verificare se una directory esiste.
if os.path.exists(dir_path): # Verifica se la directory esiste
    print(f"La directory '{dir_path}' esiste.") # Stampa il messaggio se la directory esiste
else:
    # crea la directory se non esiste
    os.makedirs(dir_path, exist_ok=True)
    print(f"La directory {dir_path} è stata creata.")
    
# Otenere le informazini su una directory.
if os.path.isdir(dir_path): # Verifica se il percorso è una directory.
    print(datetime.datetime.fromtimestamp(os.path.getmtime(dir_path))) # Stampa la data di modifica della directory
    print(os.path.getsize(dir_path)) # Stampa la dimensione della directory in byte
    print(os.listdir(dir_path)) # Stampa il contenuto della directory
    print(os.path.abspath(dir_path)) # Stampa il percorso assoluto della directory
