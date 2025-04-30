# METODI STATICI

# Uso della classe statica nel GDR(InterfacciaUtente)

- Creazione di una interfaccia utente
- i metodi come chhiedi_input, chiedi_numero, conferma non hanno bisogno de dati dell'utente(self)
- Sono solo funzioni di utilità 

# Creazione interfaccia.py

/utils/interfaccia.py
|Metodo | Funzionalità|
----|----
|chiedi_input| Chiede una risposta testuale, valida solo se rientra nelle opzioni|
|chiedi_numero| Chiede un numero intero, opzionalmente dentro un range minimo/massimo|
|conferma| Chiede un si/no (s/n) e ritorna True o False|

```python

class InterfacciaUtente:
    @staticmethod
    def chiedi_input(messaggio, opzioni=None):
        while True:
            risposta = input(messaggio).strip()
            if opzioni:
                if risposta.lower() in [o.lower() for o in opzioni]:
                    return risposta
                else:
                    print(f"input non valido. Scelte valide: {', '.join(opzioni)}")
            else:
                return risposta
            
    @staticmethod
    def chiedi_numero(messaggio, minimo=None, massimo=None):
        while True:
            try:
                numero = int(input(messaggio).strip())
                if minimo is not None and numero <= minimo:
                    print(f"Il numero deve essere maggiore o uguale a {minimo}.")
                    continue
                if massimo is not None and numero >= massimo:
                    print(f"Il numero deve essere minore o uguale a {massimo}.")
                    continue
                return numero

            except ValueError:
                print("Input non valido. Inserisci un numero intero.")

    @staticmethod
    def conferma(messaggio):
        while True:
            risposta = input (messaggio + " (s/n): ").strip().lower()
            if risposta == 's':
                return True
            elif risposta == 'n':
                return False
            else:
                print("Input non valido. Rispondi con 's' o 'n'.")
```

# esempio di uso
```python
from utils.interfaccia import InterfacciaUtente
# Scegli una classe manualmente
classe = InterfacciaUtente.chiedi_input(
    "Scegli il personaggio (Guerriero/Mago/Ladro): ",
    opzioni=["Guerriero", "Mago", "Ladro"]
)
print(f"Hai scelto la classe: {classe}")
```

```python
# Scegli un numero tra 1 e 5
from utils.interfaccia import InterfacciaUtente

numero = InterfacciaUtente.chiedi_numero("Inserisci un numero tra 1 e 5: ", minimo=1, massimo=5)
print(f"Hai scelto il numero: {numero}")
```
```python
# Conferma di voler continuare
from utils.interfaccia import InterfacciaUtente
se_gioca = InterfacciaUtente.conferma("Vuoi iniziare il torneo?")
if se_gioca:
    print("Iniziamo il torneo!")
else:
    print("Torneo annullato.")
```

## Esempio di as con alias in modo da evitare di scrivere InterfacciaUtente
```python
from utils.interfaccia import InterfacciaUtente as IU
# Scegli una classe manualmente 
classe = IU.chiedi_input(
    "Scegli il personaggio (Guerriero/Mago/Ladro): ",
    opzioni=["Guerriero", "Mago", "Ladro"]
)
print(f"Hai scelto la classe: {classe}")
```
# vantaggi 
- Tutta la geszione input/output è centralizzata
- Se vuoi cambiare i messaggi o migliorare i controlli in futuro -> cambi solo in InterfacciaUtente.
- Pulizia totale nei file di gioco(torneo.py, personaggio.py, ecc.)

# IMPLEMENTAZIONE

