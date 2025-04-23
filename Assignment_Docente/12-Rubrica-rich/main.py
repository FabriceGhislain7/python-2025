# RUBRICA JSON CON RICH
import os
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box

# comando creazione ambiente virtuale
# python -m venv venv
# comando attivazione ambiente virtuale
# venv\Scripts\activate
# comando installazione rich
# pip install rich
# comando disinstallazione rich
# pip uninstall rich
# comando uscita ambiente virtuale
# deactivate

console = Console()

# Assicura che la cartella contatti esista
if not os.path.exists("contatti"):
    os.makedirs("contatti")

# Loop principale
while True:
    console.clear()
    console.print(Panel.fit(
        "[bold yellow]RUBRICA TELEFONICA JSON[/bold yellow]\n"
        "[cyan]1.[/] Aggiungi contatto\n"
        "[cyan]2.[/] Modifica contatto\n"
        "[cyan]3.[/] Elimina contatto\n"
        "[cyan]4.[/] Visualizza contatti attivi\n"
        "[cyan]5.[/] Esci",
        title="Menu",
        border_style="green",
        box=box.ROUNDED
    ))

    scelta = Prompt.ask("\n[bold]Scegli un'opzione[/]")

    if scelta == "1":
        console.clear()
        try:
            console.print(Panel("Inserimento nuovo contatto", style="bold blue", box=box.DOUBLE))
            nome = Prompt.ask("Nome").strip().capitalize()
            cognome = Prompt.ask("Cognome").strip().capitalize()
            telefono = Prompt.ask("Telefono").strip()
            email = Prompt.ask("Email").strip()

            attivo = Prompt.ask("Attivo (si/no)").lower()
            if attivo not in ["si", "no"]:
                raise ValueError("Inserire 'si' o 'no'.")
            attivo = True if attivo == "si" else False

            attivita_input = Prompt.ask("Attività (1=programmazione, 2=customer care, 3=web design)").strip()
            attivita_map = {"1": "programmatore", "2": "customer care", "3": "web designer"}
            attivita = attivita_map.get(attivita_input)
            if not attivita:
                raise ValueError("Scelta attività non valida.")

            contatto = {
                "nome": nome,
                "cognome": cognome,
                "telefono": telefono,
                "email": email,
                "attivo": attivo,
                "attivita": attivita,
                "data_creazione": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            with open(f"contatti/{nome}_{cognome}.json", "w", encoding="utf-8") as file:
                json.dump(contatto, file, indent=4, ensure_ascii=False)

            console.print("[bold green]Contatto aggiunto con successo![/bold green]")
            input("\nPremi Invio per tornare al menu...")
        except Exception as e:
            console.print(f"[bold red]Errore:[/] {e}")
            input("\nPremi Invio per tornare al menu...")

    elif scelta == "2":
        console.clear()
        try:
            nome = Prompt.ask("Nome del contatto da modificare").strip().capitalize()
            cognome = Prompt.ask("Cognome del contatto da modificare").strip().capitalize()
            path = f"contatti/{nome}_{cognome}.json"

            if not os.path.exists(path):
                raise FileNotFoundError("Contatto non trovato.")

            with open(path, "r", encoding="utf-8") as file:
                contatto = json.load(file)

            console.print(Panel(f"Modifica contatto: [bold]{nome} {cognome}[/bold]", style="bold cyan", box=box.SQUARE))
            console.print(f"Telefono attuale: [bold]{contatto['telefono']}[/bold]")
            console.print(f"Email attuale: [bold]{contatto['email']}[/bold]")

            contatto["telefono"] = Prompt.ask("Nuovo Telefono").strip()
            contatto["email"] = Prompt.ask("Nuova Email").strip()

            with open(path, "w", encoding="utf-8") as file:
                json.dump(contatto, file, indent=4, ensure_ascii=False)

            console.print("[bold green]Contatto modificato con successo![/bold green]")
            input("\nPremi Invio per tornare al menu...")
        except Exception as e:
            console.print(f"[bold red]Errore:[/] {e}")
            input("\nPremi Invio per tornare al menu...")

    elif scelta == "3":
        console.clear()
        try:
            nome = Prompt.ask("Nome del contatto da eliminare").strip().capitalize()
            cognome = Prompt.ask("Cognome del contatto da eliminare").strip().capitalize()
            path = f"contatti/{nome}_{cognome}.json"

            if not os.path.exists(path):
                raise FileNotFoundError("Contatto non trovato.")

            os.remove(path)
            console.print("[bold green]Contatto eliminato con successo![/bold green]")
            input("\nPremi Invio per tornare al menu...")
        except Exception as e:
            console.print(f"[bold red]Errore:[/] {e}")
            input("\nPremi Invio per tornare al menu...")

    elif scelta == "4":
        console.clear()
        table = Table(title="Contatti Attivi", box=box.SIMPLE_HEAVY)
        table.add_column("Nome", style="bold cyan")
        table.add_column("Cognome", style="bold cyan")
        table.add_column("Telefono")
        table.add_column("Email")
        table.add_column("Attività")

        trovati = 0
        for file in os.listdir("contatti"):
            if file.endswith(".json"):
                with open(f"contatti/{file}", "r", encoding="utf-8") as f:
                    contatto = json.load(f)
                    if contatto.get("attivo", False):
                        table.add_row(
                            contatto["nome"],
                            contatto["cognome"],
                            contatto["telefono"],
                            contatto["email"],
                            contatto["attivita"]
                        )
                        trovati += 1
        if trovati > 0:
            console.print(table)
        else:
            console.print("[bold yellow]Nessun contatto attivo trovato.[/bold yellow]")

        input("\nPremi Invio per tornare al menu...")

    elif scelta == "5":
        console.clear()
        console.print(Panel("[bold green]Uscita dal programma... A presto![/bold green]", box=box.DOUBLE))
        break

    else:
        console.print("[bold red]Scelta non valida. Riprova.[/bold red]")
        input("\nPremi Invio per tornare al menu...")