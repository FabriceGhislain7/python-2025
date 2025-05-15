# GDR STATIC INTERFACCIA
## Obiettivi didattici

- Creazione interfaccia.py
- /utils/interfaccia.py

Metodo | Funzionalita
---|---
chiedi_input | Chiede una risposta testuale, valida solo se rientra nelle opzioni
chiedi_numero | Chiede un numero intero, opzionalmente dentro un range min max
conferma | Chiede un sì/no (s/n) e ritorna True o False

**interfaccia.py**
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
                    print(f"Input non valido! Scelte valide: {', '.join(opzioni)}")
            else:
                return risposta

    @staticmethod
    def chiedi_numero(messaggio, minimo=None, massimo=None):
        while True:
            try:
                numero = int(input(messaggio))
                if minimo is not None and numero <= minimo:
                    print(f"Devi inserire un numero maggiore o uguale a {minimo}.")
                    continue  # uso continue in modo da tornare all inizio del ciclo
                if massimo is not None and numero >= massimo:
                    print(f"Devi inserire un numero minore o uguale a {massimo}.")
                    continue
                return numero

            except ValueError:
                print("Input non valido! Devi inserire un numero intero.")

    @staticmethod
    def conferma(messaggio):
        while True:
            risposta = input(messaggio + " (s/n): ").strip().lower()
            if risposta == 's':
                return True
            elif risposta == 'n':
                return False
            else:
                print("Rispondi con 's' o 'n'.")
```
Esempio di uso:
```python
from utils.interfaccia import InterfacciaUtente

# Scegli una classe manualmente
classe = InterfacciaUtente.chiedi_input(
    "Scegli il tuo personaggio (mago/guerriero/ladro): ",
    opzioni=["mago", "guerriero", "ladro"]
)
print(f"Hai scelto: {classe}")

# Scegli un numero tra 1 e 5
numero = InterfacciaUtente.chiedi_numero("Inserisci un numero da 1 a 5: ", minimo=1, massimo=5)
print(f"Hai inserito il numero {numero}")

# Conferma di voler continuare
se_gioca = InterfacciaUtente.conferma("Vuoi iniziare il torneo?")
if se_gioca:
    torneo.gioca()
else:
    print("Torneo annullato!")
```
Esempio di `as` con alias in modo da evitare di scrivere InterfacciaUtente
```python
from utils.interfaccia import InterfacciaUtente as IU
# Scegli una classe manualmente
classe = IU.chiedi_input(
    "Scegli il tuo personaggio (mago/guerriero/ladro): ",
    opzioni=["mago", "guerriero", "ladro"]
)
print(f"Hai scelto: {classe}")
```
## Vantaggi
- Tutta la gestione input/errore è centralizzata.
- Se vuoi cambiare i messaggi o migliorare i controlli in futuro -> cambi solo in InterfacciaUtente.
- Pulizia totale nei file di gioco (torneo.py, turno.py ecc.)
# IMPLEMENTAZIONE
turno.py
```python
# gli oggetti vengono aggiunti all'inventario del giocatore nel turno
from utils.interfaccia import InterfacciaUtente

class Turno:
    def __init__(self, giocatore, nemico):
        self.giocatore = giocatore
        self.nemico = nemico
        self.numero_turno = 1

    def mostra_inventario(self):
        print("\n--- Inventario ---")
        if not self.giocatore.inventario.oggetti:
            print("Inventario vuoto.")
        else:
            for idx, oggetto in enumerate(self.giocatore.inventario.oggetti, 1):
                print(f"{idx}) {oggetto.nome}")
        print("-------------------")

    def esegui(self):
        while True:
            print(f"\n--- Turno {self.numero_turno} ---")

            # Mostra inventario
            self.mostra_inventario()

            # Chiedi se vuole usare un oggetto prima di attaccare
            if self.giocatore.inventario.oggetti:
                usa = InterfacciaUtente.conferma("Vuoi usare un oggetto prima di attaccare?")
                if usa:
                    nomi_oggetti = [oggetto.nome for oggetto in self.giocatore.inventario.oggetti]
                    oggetto_scelto = InterfacciaUtente.chiedi_input(
                        "Quale oggetto vuoi usare? Scrivi il nome esatto: ",
                        opzioni=nomi_oggetti
                    )
                    self.giocatore.inventario.usa_oggetto(oggetto_scelto, self.giocatore, self.nemico)

            # Attacco normale
            self.giocatore.attacca(self.nemico)

            if self.nemico.sconfitto():
                print(f"Hai vinto contro {self.nemico.nome}!")
                self.giocatore.recupera_hp()
                self.giocatore.inventario.usa_oggetto("Pozione Rossa", self.giocatore)
                self.giocatore.prendi_inventario(self.nemico)
                break

            # Azioni del nemico
            self.nemico.attacca(self.giocatore)

            if self.giocatore.sconfitto():
                print(f"Sei stato sconfitto da {self.nemico.nome}!")
                break

            self.numero_turno += 1
```
torneo.py
```python
# random serve per scegliere il personaggio
import random
from utils.utils import mostra_benvenuto
from utils.interfaccia import InterfacciaUtente  # <--- nuovo import
from torneo.turno import Turno
from personaggi.classi import Mago, Guerriero, Ladro
from oggetti.oggetto import PozioneCura, BombaAcida, Medaglione
from inventario.inventario import Inventario

class Torneo:
    def __init__(self):
        self.giocatore = None
        self.nemici = []
        self.nemici_sconfitti = 0

    def setup(self):
        mostra_benvenuto()
        
        # Interattività: scelta manuale del personaggio
        scelta = InterfacciaUtente.chiedi_input(
            "Scegli il tuo personaggio (mago/guerriero/ladro): ",
            opzioni=["mago", "guerriero", "ladro"]
        ).lower()

        if scelta == "mago":
            self.giocatore = Mago("Tu (Mago)")
        elif scelta == "guerriero":
            self.giocatore = Guerriero("Tu (Guerriero)")
        elif scelta == "ladro":
            self.giocatore = Ladro("Tu (Ladro)")

        self.giocatore.inventario = Inventario()  # Assegna inventario
        print(f"\nHai scelto: {self.giocatore.nome}\n")

        # Configurazione nemici
        self.nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
        
       # Randomizzazione dei nemici
        random.shuffle(self.nemici)

    def gioca(self):
        self.setup()
        
        # Aggiungi una pozione iniziale al giocatore
        self.giocatore.inventario.aggiungi(PozioneCura("Pozione Rossa"))
    
        for nemico in self.nemici:
            
            # Aggiungi un oggetto random all'inventario di ogni nemico
            oggetto_random = random.choice([
                PozioneCura("Pozione Rossa"),
                PozioneCura("Pozione Blu", valore=50),
                BombaAcida(),
                Medaglione()
            ])
            nemico.inventario = Inventario()  # Assicuriamoci che ogni nemico abbia un inventario
            nemico.inventario.aggiungi(oggetto_random)
            
            print(f"\nSta per iniziare uno scontro contro {nemico.nome}!")

            # Conferma opzionale prima di ogni combattimento
            if not InterfacciaUtente.conferma("Sei pronto ad affrontarlo?"):
                print("Hai deciso di ritirarti dal torneo.")
                return

            turno = Turno(self.giocatore, nemico)
            turno.esegui()

            if self.giocatore.sconfitto():
                print(f"Hai sconfitto {self.nemici_sconfitti} nemici")
                return

            self.nemici_sconfitti += 1

        print("\nHai vinto il torneo!")
        print(f"Hai sconfitto {self.nemici_sconfitti} nemici.")
```
main.py
```python
# importa la classe principale Torneo
from utils.interfaccia import InterfacciaUtente
from torneo.torneo import Torneo

def main():
    while True:
        print("\n=== MENU PRINCIPALE ===")
        scelta = InterfacciaUtente.chiedi_input(
            "Scegli un'opzione:\n1) Nuova partita\n2) Esci\n> ",
            opzioni=["1", "2"]
        )

        if scelta == "1":
            torneo = Torneo()
            torneo.gioca()
        elif scelta == "2":
            print("Grazie per aver giocato!")
            break

if __name__ == "__main__":
    main()
```