# RUBRICA JSON (v1.0)
import os
import json
from datetime import datetime

if not os.path.exists("contatti"):
    os.makedirs("contatti")
    
# clear screen
os.system('cls' if os.name == 'nt' else 'clear')
    
while True:
    print("\nRUBRICA TELEFONICA JSON (v1.0)")
    print("-" * 80)
    print("1. Aggiungi contatto")
    print("2. Modifica contatto")
    print("3. Elimina contatto")
    print("4. Visualizza contatti attivi")
    print("5. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        # Aggiungi contatto
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear') # nt significa windows
        print("Inserimento")
        print("-" * 80)
        nome = input("Nome: ").strip().capitalize()
        cognome = input("Cognome: ").strip().capitalize()
        telefono = input("Telefono: ").strip()
        email = input("Email: ").strip()
        try:
            attivo = input("Attivo (si/no): ").lower()
            if attivo not in ["si", "no"]:
                raise ValueError("Opzione non valida. Riprova.")
        except ValueError as e:
            print(f"Errore: {e}")
            continue
        if attivo == "si":
            attivo = True
        else:
            attivo = False
        try:
            attivita = input("Attività scegli tra (1) programmazione, (2) customer care, (3) web design: ").strip()
            if attivita not in ["1", "2", "3"]:
                raise ValueError("Opzione non valida. Riprova.")
        except ValueError as e:
            print(f"Errore: {e}")
            continue
        if attivita == "1":
            attivita = "programmatore"
        elif attivita == "2":
            attivita = "customer care"
        elif attivita == "3":  
            attivita = "web designer"

        contatto = {
            "nome": nome,
            "cognome": cognome,
            "telefono": telefono,
            "email": email,
            "attivo": attivo,
            "attivita": attivita,
            "data_creazione": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(f"contatti/{nome}_{cognome}.json", "w") as file:
            json.dump(contatto, file, indent=4)
        print("Contatto aggiunto con successo!")
    elif scelta == "2":
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        nome = input("Nome del contatto da modificare: ")
        cognome = input("Cognome del contatto da modificare: ")

        try:
            with open(f"contatti/{nome}_{cognome}.json", "r") as file:
                contatto = json.load(file)

            print("Contatto trovato!")
            print(f"Nome: {contatto['nome']}")
            print(f"Cognome: {contatto['cognome']}")
            print(f"Telefono: {contatto['telefono']}")
            print(f"Email: {contatto['email']}")
            print(f"Attivo: {'Si' if contatto['attivo'] else 'No'}")
            print(f"Attività: {contatto['attivita']}")
            print(f"Data di creazione: {contatto['data_creazione']}")

            contatto["telefono"] = input("Nuovo Telefono: ")
            contatto["email"] = input("Nuova Email: ")

            with open(f"contatti/{nome}_{cognome}.json", "w") as file:
                json.dump(contatto, file, indent=4)
            print("Contatto modificato con successo!")
        except FileNotFoundError:
            print("Contatto non trovato.")
    elif scelta == "3":
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        nome = input("Nome del contatto da eliminare: ")
        cognome = input("Cognome del contatto da eliminare: ")

        try:
            os.remove(f"contatti/{nome}_{cognome}.json")
            print("Contatto eliminato con successo!")
        except FileNotFoundError:
            print("Contatto non trovato.")
    elif scelta == "4":
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Contatti attivi:")
        print("-" * 80)
        for file in os.listdir("contatti"):
            if file.endswith(".json"):
                with open(f"contatti/{file}", "r") as f:
                    contatto = json.load(f)
                    if contatto["attivo"]:
                        print(f"{contatto['nome']} {contatto['cognome']} - {contatto['telefono']} - {contatto['email']} - {contatto['attivita']}")
                        # print(f"Data di creazione: {contatto['data_creazione']}")
                        print("-" * 80)
    elif scelta == "5":
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Uscita dal programma...")
        break
    else:
        print("Opzione non valida. Riprova.")