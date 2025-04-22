# MAIN()

la struttura main() in Python, uno degli strumenti più utili per organizzare programmi più grandi o complessi.

In molti linguaggi (come C o Java), il punto d’ingresso del programma è sempre una funzione chiamata main().

In Python non è obbligatorio, ma è buona pratica usare main() per migliorare:

- la leggibilità
- la modularità
- la riutilizzabilità (es. import del file da altri moduli)

## Struttura tipica
```python
def main():
    # Tutto il codice principale va qui
    print("Programma avviato")
    nome = input("Come ti chiami? ")
    print(f"Ciao, {nome}!")

# Punto d'ingresso del programma
if __name__ == "__main__":
    main()
```
## Cosa significa if __name__ == "__main__":
Questa riga dice:

- "Esegui la funzione main() solo se questo file è lanciato direttamente, non se è importato da un altro script."

## Esempio pratico
Supponi di avere questo file:

- rubrica.py

```python
def saluta(nome):
    print(f"Ciao, {nome}!")

def main():
    nome = input("Inserisci il tuo nome: ")
    saluta(nome)

if __name__ == "__main__":
    main()
```
Se lo esegui direttamente (python rubrica.py), parte main().

Ma se lo importi in un altro file:

- altra_rubrica.py

```python
import rubrica

rubrica.saluta("Marco")
```
> main() NON parte automaticamente, perché stai solo importando.

## Vantaggi dell’uso di main()
- Organizzazione chiara del codice
-Puoi riusare funzioni importando il file
- Puoi scrivere test automatici più facilmente
- Capisci subito da dove parte il programma

## Struttura consigliata per un file .py
```python
# importazioni
import datetime

# definizione funzioni
def saluta(nome):
    print(f"Ciao, {nome}!")

# funzione principale
def main():
    nome = input("Inserisci nome: ")
    saluta(nome)

# punto d'ingresso
if __name__ == "__main__":
    main()
```
