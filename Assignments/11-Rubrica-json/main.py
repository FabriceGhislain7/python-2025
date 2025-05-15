import os
import json
from datetime import datetime

# Creare una directory  
path_contatti = "contatti"  
os.makedirs(path_contatti, exist_ok=True)

menu = {"1": "Visualizza i contatti attivi",
        "2": "Aggiungi",
        "3": "Modifica o elimina un contatto",
        "0": "Exit."        
        }

while True:
    print(f"{'MENU':^40}\n{"-" * 40}")      # Visualizzazione del menu
    for number, option in menu.items():
        print(f"{number}: {option}")
    
    scelta_utente = input("Scegli l'operazione: ")      # Gestione della scelta dell'utente
    if not scelta_utente in menu.keys():
        print("Scelta non valida. Premi 0, 1, 2 oppure 3")
        continue

    match scelta_utente:
        case "1":       # Visualizzo i contatti attivi
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(os.listdir(path_contatti)) == 0:
                print("Rubrica telefonica vuota.")
            else:
                for contatto in os.listdir(path_contatti):
                    path_contatto = os.path.join(path_contatti, contatto)
                    with open(path_contatto, "r", encoding='utf-8') as file:
                        obj = json.load(file)
                        if obj["attivo"]:
                            print(f"nome: {obj['nome']} Cognome: {obj['Cognome']}")
                            print(f"Tipo: {obj['telefono'][0]['tipo']} Numero: {obj['telefono'][0]['numero']}")
                            print(f"Tipo: {obj['telefono'][1]['tipo']} Numero: {obj['telefono'][1]['numero']}")
                            print(f"Attivo: {obj['attivo']} Note: {obj['Note']}")
                            print(f"Attività: {obj['attivita']}")
                        else:
                            pass

        case "2":        # Aggiungi un contatto
            nuovo_nome = input("Inserisci il nome: ")
            nuovo_cognome = input("Inserisci il cognome: ")
            tel_tipo_casa = input("Numero telefono di casa: ")
            tel_tipo_cel = input("Numero di cellulare: ")
            attivo = input("Sei attivo(a)? (si/no): ")
            attivita = input("Inserisci la tua attivita: ")
            note = input("Inserisci una nota: ") 

            nome_file = nuovo_nome + nuovo_cognome
            

        case "3": # Modifica o elimina 
            print("Sotto menu")
            while True:
                suboption_user = ("1: Modifica contatto.\n2: Elimina contatto.\n Scelta: ")
                if not suboption_user in ["1", "2"]:
                    continue
                else:
                    break
            if suboption_user == "1":       # A
                print("Case 3")

        case "0":
            print("Hai deciso di uscire dalla rubrica")
            exit()

    

    
