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
            destinazione = os.path.join(cartella_dest, file)
            shutil.move(file_path, os.path.join(destinazione)) # gli argomenti di move sono il file da spostare e la destinazione

    print("Organizzazione completata.")