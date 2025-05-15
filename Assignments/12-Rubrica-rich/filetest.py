from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box
# Stampa una tabella

console = Console()
table = Table(title="Contatti attivi", box=box.SIMPLE)

table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
table.add_column("Telefono", style="green")
table.add_row("Alberto", "Carini", "1234567890")

console.print(table)