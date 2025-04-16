import os
import json
import time
import logging
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich import print
from rich import spinner 

console = Console()

# Creare la directory contatti se non esiste
path_contatti = "contatti"
os.makedirs(path_contatti, exist_ok=True)

menu = {
    "1": "Visualizza i contatti attivi",
    "2": "Aggiungi",
    "3": "Modifica o elimina un contatto",
    "0": "Exit"
}

while True:
    # console.clear()

    # Crea e stampa il testo del menu.
    menu_text = ""
    for number, option in menu.items():
        menu_text += f"[cyan]{number}.[/] {option}\n"
    console.print(Panel.fit(
        f"[bold yellow]RUBRICA TELEFONICA[/bold yellow]\n\n{menu_text}",
        title="Menu",
        border_style="green"
    ))
    try:
        scelta_utente = Prompt.ask("[bold cyan]Inserisci il numero dell'opzione: [/bold cyan]").strip().capitalize()
        if scelta_utente not in menu:
            raise ValueError("Scelta non valida. Premi 0, 1, 2 oppure 3[bold red/]")
    except ValueError as e:
        console.print(f"[bold red]Errore: {e}[/]")


    match scelta_utente:
        case "0":       # primo caso
            console.print("Grazie per aver usato la rubrica telefonica!", style="bold green" )
            break

        case "1":  # Visualizza i contatti attivi
            try:
                contatti_files = os.listdir(path_contatti)
            except FileNotFoundError:
                console.print("Errore: Cartella 'contatti' non trovata", style="bold red")
                continue
            except PermissionError:
                console.print("Errore: Permessi insufficienti per leggere la cartella", style="bold red")
                continue

            if not contatti_files:
                console.print("Rubrica telefonica vuota.", style="bold red")
                continue

            rubrica_attiva = []
            contatti_trovati = False
            for contatto_file in contatti_files:
                try:
                    path_contatto = os.path.join(path_contatti, contatto_file)
                    with open(path_contatto, "r", encoding='utf-8') as file:
                        try:
                            obj = json.load(file)
                            if obj["attivo"]:
                                


                                print(f"\nNome: {obj['nome']} {obj['cognome']}")
                                for tel in obj['telefono']:
                                    print(f"  {tel['tipo'].capitalize()}: {tel['numero']}")
                                print(f"  Attività: {', '.join(obj['attivita'])}")
                                print(f"  Note: {obj['note']}")
                                contatti_trovati = True
                        except json.JSONDecodeError:
                            console.print(f"Errore: File {contatto_file} non è un JSON valido", style="bold red")
                            continue
                        except KeyError as e:
                            console.print(f"Errore: Campo mancante nel file {contatto_file}: {str(e)}", style="bold red")
                            continue
                except FileNotFoundError:
                    console.print(f"Errore: File {contatto_file} non trovato", style="bold red")
                    continue
                except PermissionError:
                    console.print(f"Errore: Permessi insufficienti per leggere {contatto_file}",style="bold red")
                    continue

            if not contatti_trovati:
                console.print("Nessun contatto attivo trovato", style="bold red")

        case "2":  # Aggiungi un contatto
            nuovo_nome = Prompt.ask("Nome: ").strip().capitalize()
            nuovo_cognome = Prompt.ask("Cognome: ").strip().capitalize()

            telefono = []
            while True:
                tipo = Prompt.ask("Tipo di numero (es. cellulare, casa, lavoro): ").strip().lower()
                numero = Prompt.ask("Numero: ").strip()

                try:
                    if not numero.isdigit():
                        raise ValueError("Il numero deve contenere solo cifre")
                    if len(numero) < 6:
                        raise ValueError("Il numero deve avere almeno 6 cifre")

                    telefono.append({"tipo": tipo, "numero": numero})
                except ValueError as e:
                    print(f"Errore: {e}")
                    continue

                altro =Prompt.ask("Vuoi inserire un altro numero? (s/n): ").strip().lower()
                if altro != "s":
                    break

            attivita =Prompt.ask("Attività (separate da virgola): ").split(",")
            note =Prompt.ask("Note aggiuntive: ").strip()

            contatto = {
                "nome": nuovo_nome,
                "cognome": nuovo_cognome,
                "telefono": telefono,
                "attivita": [a.strip() for a in attivita],
                "note": note,
                "attivo": True,
                "data_creazione": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            try:
                nome_file = f"{nuovo_nome}_{nuovo_cognome}.json".replace(" ", "_")
                percorso_completo = os.path.join(path_contatti, nome_file)
                
                if os.path.exists(percorso_completo):
                    print("Errore: Contatto già esistente")
                    continue
                    
                with open(percorso_completo, "x", encoding='utf-8') as file:  
                    json.dump(contatto, file, indent=4, ensure_ascii=False)
                
                print(f"Contatto {nuovo_nome} {nuovo_cognome} salvato con successo!") 
            
            except OSError as e:
                print(f"Errore durante il salvataggio: {str(e)}")

        case "3":  # Modifica o elimina
            while True:
                print("\nSottomenu:")
                print("1: Modifica contatto")
                print("2: Elimina contatto")
                print("0: Torna al menu principale")

                try:
                    suboption =Prompt.ask("Scelta: ")
                    if suboption == "0":
                        break
                    if suboption not in ["1", "2"]:
                        print("Scelta non valida")
                        continue

                    nome_cercato =Prompt.ask("Inserisci il nome: ").strip().capitalize()
                    cognome_cercato =Prompt.ask("Inserisci il cognome: ").strip().capitalize()
                    nome_file = f"{nome_cercato}_{cognome_cercato}.json"
                    percorso_file = os.path.join(path_contatti, nome_file)

                    try:
                        with open(percorso_file, "r", encoding='utf-8') as file:
                            contatto = json.load(file)
                    except FileNotFoundError:
                        print("Errore: Contatto non trovato")
                        continue

                    if suboption == "1":  # Modifica
                        nuovo_nome =Prompt.ask("Nuovo nome (lascia vuoto per mantenere): ").strip().capitalize()
                        nuovo_cognome =Prompt.ask("Nuovo cognome (lascia vuoto per mantenere): ").strip().capitalize()

                        if nuovo_nome:
                            contatto["nome"] = nuovo_nome
                        else:
                            nuovo_nome = contatto["nome"]
                        if nuovo_cognome:
                            contatto["cognome"] = nuovo_cognome
                        else:
                            nuovo_cognome = contatto["cognome"]

                        try:
                            nuovo_nome_file = f"{nuovo_nome}_{nuovo_cognome}.json"
                            nuovo_percorso = os.path.join(path_contatti, nuovo_nome_file)

                            if nuovo_nome_file != nome_file:
                                try:
                                    os.rename(percorso_file, nuovo_percorso)
                                except FileExistsError:
                                    print("Errore: Esiste già un contatto con questo nome")
                                    continue

                            with open(nuovo_percorso if nuovo_nome_file != nome_file else percorso_file, 
                                    "w", encoding='utf-8') as file:
                                json.dump(contatto, file, indent=4, ensure_ascii=False)

                            print("Contatto modificato con successo!")
                        except OSError as e:
                            print(f"Errore durante il salvataggio: {str(e)}")

                    elif suboption == "2":  # Elimina
                        try:
                            os.remove(percorso_file)
                            print("Contatto eliminato con successo!")
                        except FileNotFoundError:
                            print("Errore: File già eliminato")

                except Exception as e:
                    print(f"Errore imprevisto: {str(e)}")