# Guida pratica: Ambienti Virtuali in Python

## Obiettivo

Imparare a:
- creare ambienti virtuali con `venv`
- attivarli e disattivarli correttamente
- installare pacchetti localmente
- esportare e importare le dipendenze con `requirements.txt`
- risolvere errori comuni durante l'uso

---

## Cos'è un ambiente virtuale?

Un ambiente virtuale isola le librerie Python di un progetto dagli altri presenti sul sistema. Serve per:

- Evitare conflitti tra versioni
- Tenere pulito il sistema
- Collaborare con team in modo coerente

---

## Creazione ambiente virtuale

**Comando:**

```powershell
python -m venv venv
```

Questo crea una cartella `venv/` nel progetto contenente l’ambiente isolato.

---

## Attivazione (Windows PowerShell)

**Comando:**

```powershell
venv\Scripts\activate
```

**Errore comune:**

```
venv : The term 'venv' is not recognized...
```

**Soluzione**: assicurati di non scrivere solo `venv`, ma tutto il percorso:

```powershell
venv\Scripts\activate
```

---

## Disattivazione ambiente

**Comando:**

```powershell
deactivate
```

---

## Installazione pacchetti nell'ambiente

Esempio:

```powershell
pip install rich
```

Tutti i pacchetti installati rimangono solo dentro quell’ambiente virtuale.

---

## Esportare le dipendenze

Crea un file `requirements.txt`:

```powershell
pip freeze > requirements.txt
```

---

## Importare le dipendenze in un altro progetto

Nel nuovo progetto:

1. Crea un ambiente virtuale:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

2. Installa tutto da `requirements.txt`:
   ```powershell
   pip install -r requirements.txt
   ```

---

## Cambio ambiente

Disattiva il precedente:

```powershell
deactivate
```

Vai in un’altra cartella e attiva l’ambiente lì:

```powershell
cd ..\nome_cartella
venv\Scripts\activate
```

---

## Pulizia

Per eliminare un ambiente virtuale basta cancellare la cartella `venv/`.

---

## Verifica ambiente attivo

Se attivo, vedrai il nome dell'ambiente all'inizio del prompt:

```
(venv) PS C:\Users\python\Documents\progetto>
```

---

## Consigli

- Ogni progetto ha il suo `venv/`
- Evita di attivare ambienti dentro ambienti
- Ricorda sempre di attivare l’ambiente prima di eseguire o installare

---

## Risorse utili

- [Documentazione ufficiale venv](https://docs.python.org/3/library/venv.html)
- [Gestione pacchetti con pip](https://pip.pypa.io/en/stable/)
```

---
