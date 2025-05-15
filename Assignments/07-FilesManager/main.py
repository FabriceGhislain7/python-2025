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
        print(f"{elemento} non è un file, è una cartella_origine.")

