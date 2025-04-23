from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from rich import print
# spinner
from time import sleep
from rich.progress import Progress, SpinnerColumn, TextColumn
# import os

# crea un oggetto Console per la stampa stilizzata
console = Console()

# pulisci lo schermo
# os.system('cls' if os.name == 'nt' else 'clear')
console.clear()

# stampa il messaggio stilizzato -----------------------------------------------
console.print("Rubrica Telefonica", style="bold green")
console.print("[bold green]Rubrica Telefonica[/bold green]")
console.print("[bold magenta]Benvenuto nella Rubrica Telefonica![/bold magenta]")

# Stampa un messaggio con un pannello ------------------------------------------
console.print(Panel("Contatti attivi", title="Rubrica", border_style="blue"))

menu = """
[1] Visualizza contatti
[2] Aggiungi contatto
[3] Modifica contatto
[4] Elimina contatto
[5] Esci
"""
console.print(Panel(menu, title="Menu Principale", subtitle="Rubrica v1.0", style="bold blue"))

# Stampa una tabella -----------------------------------------------------------
table = Table(title="Contatti attivi", box=box.SIMPLE)

table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
table.add_column("Telefono", style="green")
table.add_row("Nome1", "Cognome1", "1234567890")

console.print(table)

# Stampa tabella dinamica ------------------------------------------------------
table = Table(title="Rubrica Contatti")

table.add_column("Codice", justify="center", style="cyan", no_wrap=True)
table.add_column("Nome", style="green")
table.add_column("Telefono", style="magenta")
table.add_column("Email", style="yellow")

# lista di contatti
contatti = [
    {"codice": "001", "nome": "Nome1", "telefono": "1234567890", "email" : "sdfsfsf@sdfsdfs.fsdf"},
    {"codice": "002", "nome": "Nome2", "telefono": "1234567890", "email" : "dfgdfgsf@sdfsdfs.fsdf"}
]

# aggiungi i contatti alla tabella
for c in contatti:
    table.add_row(c["codice"], c["nome"], c["telefono"], c["email"])
    
# Stampa la tabella
console.print(table)

# Stampa prompt ----------------------------------------------------------------
nome = Prompt.ask("[cyan]Nome[/cyan]")
telefono = Prompt.ask("[green]Telefono[/green]")
email = Prompt.ask("[yellow]Email[/yellow]")
genere = Prompt.ask("[blue]Genere[/blue]", choices=["Maschio", "Femmina", "Altro"], default="Altro")

newsletter = Confirm.ask("[magenta]Vuoi iscriverti alla newsletter?[/magenta]")

print(f"\n[bold]Genere:[/bold] {genere}")
print(f"[bold]Email:[/bold] {email}")

print(f"[bold]Newsletter:[/bold] {'Iscritto' if newsletter else 'Non iscritto'}")

# Menu interattivo con scelta numerica -----------------------------------------
console.print("\n[bold blue]=== Menu Rubrica ===[/bold blue]")
console.print("[1] Visualizza contatti")
console.print("[2] Aggiungi contatto")
console.print("[3] Esci")

scelta = Prompt.ask("[bold green]Scegli un'opzione[/bold green]", choices=["1", "2", "3"], default="1")

# stampa la scelta
if scelta == "1":
    console.print("[bold green]Hai scelto di visualizzare i contatti.[/bold green]")
    # qui puoi aggiungere il codice per visualizzare i contatti
elif scelta == "2":
    console.print("[bold green]Hai scelto di aggiungere un contatto.[/bold green]")
    # qui puoi aggiungere il codice per aggiungere un contatto
elif scelta == "3":
    console.print("[bold green]Hai scelto di uscire.[/bold green]")
    # qui puoi aggiungere il codice per uscire
# Stampa un messaggio di uscita
console.print("[bold red]Grazie per aver utilizzato la Rubrica Telefonica![/bold red]")

# spinner ----------------------------------------------------------------------
with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
    task = progress.add_task("[cyan]Caricamento in corso...", total=None)
    sleep(2)
    progress.remove_task(task)
    
# il sito ufficiale di rich è [rich](https://rich.readthedocs.io/en/stable/)