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
from rich.align import Align

console = Console()
# contenuto = Align.center("La mia Rubrica telefonica")

# panel = Panel(contenuto)
# console.print(panel)

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
    console.print(Panel(
        Align.center(f"[bold yellow]RUBRICA TELEFONICA[/bold yellow]\n\n{menu_text}"),
        title="Menu",
        border_style="green"
    ))
    try:
        scelta_utente = Prompt.ask("[bold cyan]Inserisci il numero dell'opzione: [/bold cyan]").strip().capitalize()
        if scelta_utente not in menu.keys():
            raise ValueError("Scelta non valida. Premi 0, 1, 2 oppure 3[bold red/]")
    except ValueError as e:
        console.print(f"[bold red]Errore: {e}[/]")


    match scelta_utente:

        # primo caso
        case "0":
            console.print("Grazie per aver usato la rubrica telefonica!", style="bold green" )
            break

        # Visualizza i contatti attivi
        case "1":
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

             # Generiamo una lista vuota per stampare i contatti attivi
            rubrica_attiva = []
            contatti_trovati = False

            # Creazione della tabella per i contatti attivi
            table = Table(title="Contatti Attivi", box=box.SIMPLE_HEAVY)
            table.add_column("Nome", style="bold")
            table.add_column("Cognome")
            table.add_column("Telefono")
            table.add_column("Email")
            table.add_column("Attività")
            table.add_column("Note")

            path_contatti = "contatti"  # o il path desiderato
            contatti_files = os.listdir(path_contatti)

            for contatto_file in contatti_files:
                try:
                    path_contatto = os.path.join(path_contatti, contatto_file)
                    with open(path_contatto, "r", encoding='utf-8') as file:
                        try:
                            obj = json.load(file)

                            if obj.get("attivo", False):
                                nome = obj.get("nome", "N/D")
                                cognome = obj.get("cognome", "N/D")
                                email = obj.get("email", "N/D")
                                attivita = ", ".join(obj.get("attivita", []))
                                note = obj.get("note", "Nessuna")

                                # Formattazione dei numeri di telefono
                                telefoni = []
                                for tel in obj.get("telefono", []):
                                    tipo = tel.get('tipo', 'N/D').capitalize()
                                    numero = tel.get('numero', 'N/D')
                                    telefoni.append(f"{tipo}: {numero}")
                                telefono_str = "\n".join(telefoni)

                                # Aggiunta alla tabella
                                table.add_row(nome, cognome, telefono_str, email, attivita, note)
                                contatti_trovati = True

                            else:
                                raise ValueError("Il Contatto non è attivo")

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
                    console.print(f"Errore: Permessi insufficienti per leggere {contatto_file}", style="bold red")
                    continue

            if contatti_trovati:
                console.print(table)
            else:
                console.print("Nessun contatto attivo trovato", style="bold red")

            altro = Prompt.ask("Vuoi proseguire con altre operazioni? (s/n): ").strip().lower()
            if altro != "s":
                break


        # Aggiunge un contatto
        case "2":
            nuovo_nome = Prompt.ask("Nome: ").strip().capitalize()
            nuovo_cognome = Prompt.ask("Cognome: ").strip().capitalize()

            telefono = []
            while True:
                tipo = Prompt.ask("Inserisci il tipo di numero (es. cellulare, casa, lavoro): ").strip().lower()
                numero = Prompt.ask("Numero: ").strip()

                try:
                    if not numero.isdigit():
                        raise ValueError("Il numero deve contenere solo cifre")
                    if len(numero) != 10:
                        raise ValueError("Il numero deve avere esatamente 10 cifre")

                    telefono.append({"tipo": tipo, "numero": numero})
                except ValueError as e:
                    print(f"Errore: {e}")
                    continue

                altro = Prompt.ask("Vuoi inserire un altro numero? (s/n): ").strip().lower()
                if altro != "s":
                    break

            attivita =Prompt.ask("Attività (separate da virgola): ").split(",")
            note = Prompt.ask("Note aggiuntive: ").strip()

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
                    console.print("Errore: Contatto già esistente", style="bold red")
                    continue

                with open(percorso_completo, "x", encoding='utf-8') as file:
                    json.dump(contatto, file, indent=4, ensure_ascii=False)

                console.print(f"Contatto {nuovo_nome} {nuovo_cognome} salvato con successo!")

            except OSError as e:
                console.print(f"Errore durante il salvataggio: {str(e)}", style="bold red")

        # Modifica o elimina
        case "3":
            while True:
                sotto_menu = {
                    "1": "Modifica contatto",
                    "2": "Elimina contatto",
                    "0": "Torna al menu principale"
                    }

                # Stampa del sotto menu (modifica, Elimina)
                sotto_menu_text = ""
                for number, option in sotto_menu.items():
                    sotto_menu_text += f"[cyan]{number}.[/] {option}\n"
                console.print(Panel.fit(
                    f"[bold yellow]Sotto menu(modifica o elimina)[/bold yellow]\n\n{sotto_menu_text}",
                    title="Menu",
                    border_style="green"
                ))

                # Test della validità della scelta del sotto menu
                try:
                    suboption = Prompt.ask("Scelta: ")
                    if suboption == "0":
                        break
                    if suboption not in ["1", "2"]:
                        console.print("Scelta non valida", style="bold red")
                        continue

                    # Raccolta dei dati dell'utente
                    nome_cercato = Prompt.ask("Inserisci il nome: ").strip().capitalize()
                    cognome_cercato = Prompt.ask("Inserisci il cognome: ").strip().capitalize()
                    nome_file = f"{nome_cercato}_{cognome_cercato}.json"
                    percorso_file = os.path.join(path_contatti, nome_file)

                    try:
                        with open(percorso_file, "r", encoding='utf-8') as file:
                            contatto = json.load(file)
                    except FileNotFoundError:
                        console.print("Errore: Contatto non trovato", style="bold red")
                        continue

                    # Modifica del contatto
                    if suboption == "1":
                        nuovo_nome = Prompt.ask("Nuovo nome (lascia vuoto per mantenere): ").strip().capitalize()
                        nuovo_cognome = Prompt.ask("Nuovo cognome (lascia vuoto per mantenere): ").strip().capitalize()

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
                                    console.print("Errore: Esiste già un contatto con questo nome", style="bold red")
                                    continue

                            with open(nuovo_percorso if nuovo_nome_file != nome_file else percorso_file, 
                                    "w", encoding='utf-8') as file:
                                json.dump(contatto, file, indent=4, ensure_ascii=False)

                            console.print("Contatto modificato con successo!", style="bold green")
                        except OSError as e:
                            console.print(f"Errore durante il salvataggio: {str(e)}", style="bold red")

                    # Eliminzione  del contatto
                    elif suboption == "2":
                        try:
                            os.remove(percorso_file)
                            console.print("Contatto eliminato con successo!", style="bold green")
                        except FileNotFoundError:
                            console.print("Errore: File già eliminato", style="bold red")

                except Exception as e:
                    console.print(f"Errore imprevisto: {str(e)}", style="bold red")

