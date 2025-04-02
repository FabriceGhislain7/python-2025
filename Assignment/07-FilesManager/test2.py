import os
path_valido = False
while True:
    path_cartella = input("Inserisci il path della directory per visualizzare le opzioni: ")
    if path_valido == os.path.exists(path_cartella):
        print("La directory non esite. Inserire una directory valida.")
        continue
    else:
        print(f"La directory esiste.")
        path_valido = True 
        break