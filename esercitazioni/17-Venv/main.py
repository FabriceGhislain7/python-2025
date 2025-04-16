from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich import print
from rich.progress import track
from rich.traceback import install
from rich.logging import RichHandler
from rich.live import Live
from rich.syntax import Syntax
from rich.markdown import Markdown

import time
import logging

import os

# Oggetto console per output stilizzato
console = Console()

# --- Stampa semplice con stile ---
console.print("Rubrica telefonica del nostro annuario", style="bold green")
print("-" * 40)

# --- Titoli colorati e messaggi ---
console.print("[bold green]Rubrica telefonica[/bold green]")
print("-" * 40)

console.print("[bold magenta]Benvenuti alla Rubrica telefonica![/bold magenta]")
print("-" * 40)

# --- Uso di Panel ---
console.print(Panel("Contatti attivi", title="Rubrica", border_style="blue"))
print("-" * 40)

# --- Menù principale con panel ---
menu = """
[1] Visualizza contatti
[2] Aggiungi contatto
[3] Modifica contatto
[4] Elimina contatto
[5] Esci
"""

console.print(Panel(menu, title="Menu Principale", subtitle="Rubrica V1.0", style="bold blue"))
print("-" * 40)

# --- Tabella contatti ---
table = Table(title="Contatti attivi", box=box.SIMPLE)

table.add_column("Nome", style="cyan", no_wrap=True)
table.add_column("Cognome", style="magenta")
table.add_column("Telefono", style="green")

table.add_row("Mario", "Rossi", "3291234567")
table.add_row("Luca", "Bianchi", "3287654321")

console.print(table)
print("-" * 40)

# --- Prompt interattivo (commentato se usato come demo) ---
# scelta = Prompt.ask("Scegli un'opzione", choices=["1", "2", "3", "4", "5"], default="1")
# console.print(f"Hai scelto: [bold yellow]{scelta}[/bold yellow]")

# --- Link utile ---
console.print("Per info visita: [bold blue]https://rich.readthedocs.io/en/stable/[/bold blue]")

# rich_demo.py

# Esempi pratici delle funzionalità più usate di rich
# Assicurati di avere installato 'rich' nel tuo ambiente:
# pip install rich

# ----------------------------------------------------------------------------------
# Inizializza Console
console = Console()

# Installa Rich per traceback
install()

# === 1. Messaggi base con stili ===
console.print("\n[bold green]Rubrica telefonica del nostro annuario[/bold green]")
console.print("-" * 40)
console.print("[bold magenta]Benvenuti alla Rubrica telefonica![/bold magenta]")
console.print("-" * 40)

# === 2. Panel con titolo ===
console.print(Panel("Contatti attivi", title="Rubrica", border_style="blue"))

# === 3. Tabella semplice ===
table = Table(title="Contatti attivi", box=box.SIMPLE)
table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
table.add_column("Telefono", style="green")
table.add_row("Mario", "Rossi", "3331122333")
table.add_row("Luca", "Bianchi", "3399988776")
console.print(table)

# === 4. Menu in un pannello ===
menu = """
[1] Aggiungi contatto
[2] Elimina contatto
[3] Visualizza contatti
[4] Cerca
[5] Esci
"""
console.print(Panel(menu, title="Menu Principale", subtitle="Rubrica V1.0", style="bold blue"))

# === 5. Progress Bar ===
console.print("\n[bold yellow]Esempio: Progress Bar[/bold yellow]")
for step in track(range(10), description="Elaborazione in corso..."):
    time.sleep(0.2)

# === 6. Traceback decorato (decommenta per testare) ===
# def crash():
#     return 1 / 0
# crash()

# === 7. Logging colorato ===
console.print("\n[bold yellow]Esempio: Logging[/bold yellow]")
logging.basicConfig(level="NOTSET", handlers=[RichHandler()])
logger = logging.getLogger("rich")
logger.debug("Messaggio di debug")
logger.info("Messaggio informativo")
logger.warning("Messaggio di warning")
logger.error("Messaggio di errore")

# === 8. Live Table ===
console.print("\n[bold yellow]Esempio: Aggiornamento Live[/bold yellow]")
live_table = Table()
live_table.add_column("Task")
live_table.add_column("Stato")

with Live(live_table, refresh_per_second=4):
    for i in range(3):
        live_table.add_row(f"Operazione {i+1}", "[yellow]In corso[/yellow]")
        time.sleep(0.5)
        live_table.columns[1]._cells[i] = "[green]Completata[/green]"
        time.sleep(0.5)

# === 9. Syntax Highlighting ===
console.print("\n[bold yellow]Esempio: Syntax Highlighting[/bold yellow]")
code = '''def saluta(nome):
    print(f"Ciao, {nome}!")
'''
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)

# === 10. Markdown ===
console.print("\n[bold yellow]Esempio: Markdown[/bold yellow]")
md = Markdown("""
# Titolo Principale
## Sottotitolo

**Testo in grassetto**

- Voce 1
- Voce 2
- Voce 3

Visita [Rich Docs](https://rich.readthedocs.io)
""")
console.print(md)

# Fine script
console.print("\n[bold green]--- Fine dimostrazione Rich ---[/bold green]")
