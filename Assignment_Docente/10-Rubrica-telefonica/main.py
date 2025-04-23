import os
from datetime import datetime

rubrica = []
FILE = "rubrica.txt"
BACKUP_DIR = "backup"

# Creazione cartella backup
if not os.path.exists(BACKUP_DIR):
    try:
        os.mkdir(BACKUP_DIR)
    except OSError as e:
        print("Errore nella creazione della cartella backup:", e)

# Caricamento dati da file
if os.path.exists(FILE):
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for r in f:
                p = r.strip().split("|")
                if len(p) == 6:
                    rubrica.append({"codice": p[0], "nome": p[1], "cognome": p[2], "telefono": p[3], "email": p[4], "data": p[5]})
    except OSError as e:
        print("Errore nella lettura del file:", e)

print("RUBRICA v4.0")

while True:
    print("\n1. Visualizza 2. Aggiungi  3. Modifica  4. Elimina  5. Cerca  6. Backup  7. Esci")
    scelta = input("Scelta: ").strip()

    if scelta == "1":
        if rubrica:
            print("Contatti:")
            for c in rubrica:
                print(f"{c['codice']} - {c['nome']} {c['cognome']} - {c['telefono']} - {c['email']}")
            print(f"Totale: {len(rubrica)} contatti.")
        else:
            print("Nessun contatto presente.")

    elif scelta == "2":
        try:
            dati = input("Inserisci: nome,cognome,telefono,email > ").strip().split(",")
            if len(dati) != 4:
                raise ValueError("Numero di campi non valido.")

            nome, cognome, telefono, email = [x.strip().capitalize() for x in dati]

            if len(nome) < 3 or len(cognome) < 3:
                raise ValueError("Nome o cognome troppo corti.")
            if not telefono.isdigit() or len(telefono) != 10:
                raise ValueError("Numero di telefono non valido.")
            if "@" not in email:
                raise ValueError("Email non valida.")

            codice = (nome[:2] + cognome[:2] + telefono[-2:]).upper()
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            trovato = False
            for c in rubrica:
                if c["codice"] == codice:
                    conferma = input("Contatto esistente. Sovrascrivere? (s/n): ").lower()
                    if conferma == "s":
                        c.update({"nome": nome, "cognome": cognome, "telefono": telefono, "email": email, "data": data})
                        print("Contatto aggiornato.")
                        trovato = True
                    break

            if not trovato:
                rubrica.append({
                    "codice": codice, "nome": nome, "cognome": cognome,
                    "telefono": telefono, "email": email, "data": data
                })
                print("Contatto aggiunto.")

        except ValueError as e:
            print("Errore dati:", e)

    elif scelta == "3":
        codice = input("Codice contatto: ").strip().upper()
        trovato = False
        for c in rubrica:
            if c["codice"] == codice:
                campo = input("Campo da cambiare (nome, cognome, telefono, email): ").lower().strip()
                nuovo = input("Nuovo valore: ").strip()

                if campo == "telefono":
                    if not nuovo.isdigit() or len(nuovo) != 10:
                        print("Numero non valido.")
                        break
                elif campo == "email":
                    if "@" not in nuovo:
                        print("Email non valida.")
                        break

                if campo in ["nome", "cognome"]:
                    c[campo] = nuovo.capitalize()
                elif campo in ["telefono", "email"]:
                    c[campo] = nuovo
                else:
                    print("Campo non valido.")
                    break

                c["data"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Contatto aggiornato.")
                trovato = True
                break

        if not trovato:
            print("Contatto non trovato.")

    elif scelta == "4":
        codice = input("Codice da eliminare: ").strip().upper()
        prima = len(rubrica)
        rubrica = [c for c in rubrica if c["codice"] != codice]
        print("Contatto eliminato." if len(rubrica) < prima else "Contatto non trovato.")

    elif scelta == "5":
        testo = input("Testo da cercare: ").strip().lower()
        risultati = [c for c in rubrica if
                     testo in c["nome"].lower() or testo in c["cognome"].lower() or
                     testo in c["telefono"] or testo in c["email"].lower()]
        print(f"Trovati: {len(risultati)}")
        for c in risultati:
            print(f"{c['codice']} - {c['nome']} {c['cognome']} - {c['telefono']} - {c['email']}")

    elif scelta == "6":
        try:
            nome_file = f"{BACKUP_DIR}/rubrica_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(nome_file, "w", encoding="utf-8") as f:
                for c in rubrica:
                    f.write(f"{c['codice']}|{c['nome']}|{c['cognome']}|{c['telefono']}|{c['email']}|{c['data']}\n")
            print(f"Backup creato in: {nome_file}")
        except OSError as e:
            print("Errore nella creazione del backup:", e)

    elif scelta == "7":
        print("Uscita dal programma.")
        break

    else:
        print("Scelta non valida.")

    # Salvataggio automatico dopo ogni azione
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            for c in rubrica:
                f.write(f"{c['codice']}|{c['nome']}|{c['cognome']}|{c['telefono']}|{c['email']}|{c['data']}\n")
    except OSError as e:
        print("Errore durante il salvataggio:", e)