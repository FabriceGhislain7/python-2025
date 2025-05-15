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
from rich.align import Align

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
    # os.system('cls' if os.name == 'nt' else 'clear')

    menu_text = ""
    for number, option in menu.items():
        menu_text += f"[cyan]{number}.[/] {option}\n"
    console.print(Panel.fit(
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
        continue

    match scelta_utente:
        case "0":
            console.print("Grazie per aver usato la rubrica telefonica!", style="bold green")
            break

        case "1":
            try:
                with console.status("[bold green]Caricamento contatti attivi...[/]", spinner="dots"):
                    time.sleep(1)
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

            table = Table(title="Contatti Attivi", box=box.SIMPLE_HEAVY)
            table.add_column("Nome", style="bold")
            table.add_column("Cognome")
            table.add_column("Telefono")
            table.add_column("Email")
            table.add_column("Attività")
            table.add_column("Note")

            for contatto_file in contatti_files:
                try:
                    path_contatto = os.path.join(path_contatti, contatto_file)
                    with console.status(f"[yellow]Apertura {contatto_file}...[/]", spinner="line"):
                        time.sleep(0.3)
                        with open(path_contatto, "r", encoding='utf-8') as file:
                            obj = json.load(file)

                    if obj.get("attivo", False):
                        nome = obj.get("nome", "N/D")
                        cognome = obj.get("cognome", "N/D")
                        email = obj.get("email", "N/D")
                        attivita = ", ".join(obj.get("attivita", []))
                        note = obj.get("note", "Nessuna")

                        telefoni = []
                        for tel in obj.get("telefono", []):
                            tipo = tel.get('tipo', 'N/D').capitalize()
                            numero = tel.get('numero', 'N/D')
                            telefoni.append(f"{tipo}: {numero}")
                        telefono_str = "\n".join(telefoni)

                        table.add_row(nome, cognome, telefono_str, email, attivita, note)
                        contatti_trovati = True
                except (json.JSONDecodeError, KeyError) as e:
                    console.print(f"Errore in {contatto_file}: {e}", style="bold red")
                except (FileNotFoundError, PermissionError) as e:
                    console.print(f"Errore: {e}", style="bold red")

            if contatti_trovati:
                console.print(table)
            else:
                console.print("Nessun contatto attivo trovato", style="bold red")

            altro = Prompt.ask("Vuoi proseguire con altre operazioni? (s/n): ").strip().lower()
            if altro != "s":
                break

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

            attivita = Prompt.ask("Attività (separate da virgola): ").split(",")
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

                with console.status("[green]Salvataggio contatto...[/]", spinner="earth"):
                    time.sleep(1)
                    with open(percorso_completo, "x", encoding='utf-8') as file:
                        json.dump(contatto, file, indent=4, ensure_ascii=False)

                console.print(f"Contatto {nuovo_nome} {nuovo_cognome} salvato con successo!")

            except OSError as e:
                console.print(f"Errore durante il salvataggio: {str(e)}", style="bold red")

        case "3":
            while True:
                sotto_menu = {
                    "1": "Modifica contatto",
                    "2": "Elimina contatto",
                    "0": "Torna al menu principale"
                }

                sotto_menu_text = ""
                for number, option in sotto_menu.items():
                    sotto_menu_text += f"[cyan]{number}.[/] {option}\n"
                console.print(Panel.fit(
                    f"[bold yellow]Sotto menu(modifica o elimina)[/bold yellow]\n\n{sotto_menu_text}",
                    title="Menu",
                    border_style="green"
                ))

                try:
                    suboption = Prompt.ask("Scelta: ")
                    if suboption == "0":
                        break
                    if suboption not in ["1", "2"]:
                        console.print("Scelta non valida", style="bold red")
                        continue

                    nome_cercato = Prompt.ask("Inserisci il nome: ").strip().capitalize()
                    cognome_cercato = Prompt.ask("Inserisci il cognome: ").strip().capitalize()
                    nome_file = f"{nome_cercato}_{cognome_cercato}.json"
                    percorso_file = os.path.join(path_contatti, nome_file)

                    with console.status(f"[cyan]Ricerca contatto {nome_file}...[/]", spinner="runner"):
                        time.sleep(1)

                    try:
                        with open(percorso_file, "r", encoding='utf-8') as file:
                            contatto = json.load(file)
                    except FileNotFoundError:
                        console.print("Errore: Contatto non trovato", style="bold red")
                        continue

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

                        nuovo_nome_file = f"{nuovo_nome}_{nuovo_cognome}.json"
                        nuovo_percorso = os.path.join(path_contatti, nuovo_nome_file)

                        try:
                            if nuovo_nome_file != nome_file:
                                os.rename(percorso_file, nuovo_percorso)

                            with console.status("[yellow]Modifica in corso...[/]", spinner="bouncingBar"):
                                time.sleep(1)
                                with open(nuovo_percorso if nuovo_nome_file != nome_file else percorso_file, "w", encoding='utf-8') as file:
                                    json.dump(contatto, file, indent=4, ensure_ascii=False)

                            console.print("Contatto modificato con successo!", style="bold green")
                        except OSError as e:
                            console.print(f"Errore durante il salvataggio: {str(e)}", style="bold red")

                    elif suboption == "2":
                        try:
                            with console.status("[red]Eliminazione contatto...[/]", spinner="dots"):
                                time.sleep(1)
                                os.remove(percorso_file)
                            console.print("Contatto eliminato con successo!", style="bold green")
                        except FileNotFoundError:
                            console.print("Errore: File già eliminato", style="bold red")

                except Exception as e:
                    console.print(f"Errore imprevisto: {str(e)}", style="bold red")
