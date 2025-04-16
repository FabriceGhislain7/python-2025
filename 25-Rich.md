# RICH

Integrare rich nel tuo programma migliorerà l’estetica del terminale e renderà i messaggi più leggibili e accattivanti, con colori, tabelle, pannelli, stili e molto altro

- Il sito ufficiale di rich è [rich](https://rich.readthedocs.io/en/stable/)

## INSTALLAZIONE

```bash
# creazione ambiente virtuale
python -m venv venv
# attivazione ambiente virtuale
source venv/bin/activate
# installazione rich
pip install rich
```
## USO

Componente|Scopo
---|---
Console|Per stampare messaggi con stili e colori
Panel|Per mostrare le sezioni come riquadri
Prompt|Per input utente stilizzati
Table|Per mostrare i contatti attivi in modo tabellare
box|Per personalizzare il bordo dei pannelli

## IMPORT

Aggiungi all’inizio:

```python
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box
```
E inizializza una console:

```python
console = Console()
```

## ESEMPIO

```python
# Stampa un messaggio con stile
console.print("Rubrica Telefonica", style="bold green")

# Stampa un messaggio con un pannello
console.print(Panel("Contatti attivi", title="Rubrica", border_style="blue"))

# Stampa una tabella
table = Table(title="Contatti attivi", box=box.SIMPLE)

table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
table.add_column("Telefono", style="green")
table.add_row("Nome1", "Cognome1", "1234567890")

console.print(table)

```

```python
# pulisci lo schermo
os.system('cls' if os.name == 'nt' else 'clear')
# oppure il clear di console
console.clear()
```

## ESEMPI DI INTEGRAZIONE IN RUBRICA

### Menu

```python
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
```
### Prompt stilizzati

Puoi sostituire:

```python
nome = input("Nome: ").strip().capitalize()
```
Con:
```python
nome = Prompt.ask("[bold cyan]Nome[/]").strip().capitalize()
```
### Tabella contatti attivi
```python
# Stampa una tabella dei contatti attivi
table = Table(title="Contatti Attivi", box=box.SIMPLE_HEAVY)
table.add_column("Nome", style="bold")
table.add_column("Cognome")
table.add_column("Telefono")
table.add_column("Email")
table.add_column("Attività")

for file in os.listdir("contatti"):
    if file.endswith(".json"):
        with open(f"contatti/{file}", "r", encoding="utf-8") as f:
            contatto = json.load(f)
            if contatto["attivo"]:
                table.add_row(
                    contatto["nome"],
                    contatto["cognome"],
                    contatto["telefono"],
                    contatto["email"],
                    contatto["attivita"]
                )

console.print(table)
```
### Messaggi

Al posto di print("Contatto aggiunto con successo!"), puoi usare:

```python
console.print("[bold green]Contatto aggiunto con successo![/bold green]")
```

E per errori:

```python
console.print(f"[bold red]Errore:[/] {e}")
```
### ESEMPIO AGGIUGI CONTATTO
```python
try:
    console.print(Panel("Inserimento nuovo contatto", style="bold blue", box=box.DOUBLE_EDGE))
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
except Exception as e:
    console.print(f"[bold red]Errore:[/] {e}")
```