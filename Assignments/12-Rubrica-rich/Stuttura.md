```markdown
# Rubrica Telefonica - Terminale

Una semplice rubrica telefonica da terminale scritta in Python, con interfaccia testuale usando `rich`. In questo proggetto non verranno usate delle nozioni avanzate come le funzioni, le classi.  

## Requisiti

- Python 3.7+
- Libreria `rich`

Installazione:
```bash
pip install rich
```

## creazione della cartella rubrica

```bash
python rubrica.py
```

## Funzionalità


-  Visualizza contatti attivi
-  Aggiungi nuovo contatto
-  Modifica contatto
-  Elimina contatto
-  Salvataggio locale in JSON

## Struttura File

Ogni contatto è salvato come un file `.json` nella cartella `contatti/`, con nome basato su Nome_Cognome.

---

## Diagramma di Flusso (Mermaid)

```mermaid
flowchart TD
    A[Start] --> B[Mostra menu]
    B --> C{Scelta utente}
    C -->|0| Z[Esci dal programma]
    C -->|1| D[Carica contatti attivi]
    D --> E[Mostra tabella contatti]
    E --> F[Chiedi se continuare]
    F -->|No| Z
    F -->|Sì| B

    C -->|2| G[Inserisci nuovo contatto]
    G --> H[Validazione telefono]
    H --> I[Salva su file JSON]
    I --> F

    C -->|3| J[Submenu Modifica/Elimina]
    J --> K{Scelta}
    K -->|Modifica| L[Carica contatto]
    L --> M[Modifica dati]
    M --> N[Salva modifiche]
    N --> F

    K -->|Elimina| O[Carica contatto]
    O --> P[Elimina file JSON]
    P --> F
```

---

## Esempio di contatto (JSON)

```json
{
  "nome": "Mario",
  "cognome": "Rossi",
  "telefono": [
    {
      "tipo": "cellulare",
      "numero": "3331234567"
    }
  ],
  "attivita": ["cliente", "sviluppatore"],
  "note": "Contatto importante",
  "attivo": true,
  "data_creazione": "2025-04-17 15:00:00"
}
```

---

## Autore

```
