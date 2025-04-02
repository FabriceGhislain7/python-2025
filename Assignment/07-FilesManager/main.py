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
    






