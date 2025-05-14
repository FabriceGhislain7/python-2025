# Implementazioni al Gdr (develop)

# Obiettivo
- espandere un progetto con nuove responsabilità, entità chiare e interazioni tra classi
- imparare le tecniche di versionamento e gestione del codice sorgente
- imparare a scrivere codice in ambiente condiviso in moduli, facilmente testabile e manutenibile, estendibile, riutilizzabile, chiaro e ben documentato
- imparare a creare un applicazione in modo modulare, con classi e metodi ben definiti con documentazione chiara e precisa
- imparare a usare GitHub per la gestione del codice sorgente e il versionamento
- imparare la gestione di un progetto in team, con responsabilità e ruoli definiti

**Approfondire i seguenti argomenti:**
- Incapsulamento
- Responsabilità delle classi
- Ereditarietà
- Polimorfismo
- Composizione

## Proposte didattiche per imparare OOP
- Classe Ambiente – è semplice, utile, immediata
- Classe Missione – organizza tutto e ti abitua a gestire moduli
- Livello / Esperienza – cominci ad astrarre la crescita
- Log e salvataggio – utile per debugging e salvataggio futuro

# 1. Classe Ambiente
- influenza combattimento, oggetti, abilità

Esempio:

```python
class Ambiente:
    def __init__(self, nome, modifica_attacco=0, modifica_cura=0):
        self.nome = nome
        self.modifica_attacco = modifica_attacco
        self.modifica_cura = modifica_cura
```
> Effetti possibili:

"Foresta" -> bonus a certe classi

"Vulcano" -> potenzia BombaAcida

"Palude" -> riduce cura del 30%

> argomenti:
**l’uso della composizione (Ambiente dentro Turno), e della configurabilità**

# 2. Classe Missione
Contiene: obiettivi, nemici, ambiente, oggetti, vincoli

```python
class Missione:
    def __init__(self, nome, ambiente, nemici, premi):
        self.nome = nome
        self.ambiente = ambiente
        self.nemici = nemici
        self.premi = premi
```
> Esempi:
- Missione “Assalto nella Nebbia”: ambiente = “Nebbia”, nemici = 2 Ladri, premio = Medaglione
- Missione “Duello nel Vulcano”: ambiente = “Vulcano”, nemico = 1 Guerriero + 1 BombaAcida

> argomenti:
**l’aggregazione (missione = ambiente + nemici + oggetti) e a gestire scenari modulari**

# 3. Classe Giocatore (separata da Personaggio)
Così puoi avere più giocatori che usano personaggi, scelgono oggetti, gestiscono punteggi ecc.

```python
class Giocatore:
    def __init__(self, nome, personaggio):
        self.nome = nome
        self.personaggio = personaggio
        self.punteggio = 0
```
> argomenti:
**l’associazione tra oggetti e separazione tra “logica del giocatore” e “logica del combattente”**

#  4. Sistema Livello / Esperienza
Aggiungi punti esperienza per ogni nemico sconfitto, sblocchi abilità, aumenti attacco ecc.

```python
class Progressione:
    def __init__(self):
        self.livello = 1
        self.exp = 0
        self.exp_per_salire = 100

    def guadagna_exp(self, punti):
        self.exp += punti
        while self.exp >= self.exp_per_salire:
            self.livello += 1
            self.exp -= self.exp_per_salire
            print(f"Sali di livello! Ora sei al livello {self.livello}.")
```
> argomenti:
**incapsulamento del comportamento e gestione dello stato interno**

# 5. Sistema di Log o Cronologia
Ogni azione viene salvata in una lista o file: chi ha attaccato, quanto danno, quale oggetto usato…

```python
class Registro:
    def __init__(self):
        self.eventi = []

    def registra(self, messaggio):
        self.eventi.append(messaggio)
        print(f"> {messaggio}")
```
> argomenti:
**a raccogliere eventi, utile per debug, replay o salvataggi**

# 6. Salvataggio/Caricamento JSON
Salvi Missioni, Giocatore, Inventari, ecc. in file .json e li ricarichi.
- Creazione di una classe con metodi statici per caricare e salvare oggetti
- Uso di json.dumps e json.loads per serializzare e deserializzare oggetti
- Esempio di classe per il salvataggio e il caricamento
```python
import json

class Salvataggio:
    @staticmethod
    def salva_giocatore(giocatore, filename):
        with open(filename, 'w') as file:
            json.dump(giocatore.__dict__, file)
    
    @staticmethod
    def carica_giocatore(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return Giocatore(**data)
```
> argomenti:
**a usare i metodi statici, gestire oggetti serializzabili, salvare stati complessi**

# 7. Nemici intelligenti (Strategy pattern base)
Ogni nemico può usare una strategia diversa: aggressiva, difensiva, casuale

```python
class StrategiaAttacco:
    def esegui(self, nemico, bersaglio):
        raise NotImplementedError()

class Aggressiva(StrategiaAttacco):
    def esegui(self, nemico, bersaglio):
        if bersaglio.salute < 40:
            nemico.attacca(bersaglio)
        else:
            # usa oggetto se disponibile
            pass
```
> argomenti:
**il concetto di comportamento intercambiabile, un design pattern reale**

# 8. Effetti
- classe incaricata di gestire effetti che modificano l'andamento dei turni o le dinamiche di gioco

- Esempio di classe per gestire effetti temporanei
```python
class Effetto:
    def __init__(self, nome, durata, effetto):
        self.nome = nome
        self.durata = durata
        self.effetto = effetto

    def applica(self, personaggio):
        # Applica l'effetto al personaggio
        pass

    def scade(self):
        # Gestisce la scadenza dell'effetto
        pass
```
> argomenti:
**la gestione dello Stato: Gli effetti possono alterare temporaneamente lo stato dei personaggi o dell'ambiente, insegnandoti a gestire stati complessi e transitori nel tuo sistema**
**Composizione e Modularità: Separando gli effetti in una classe dedicata, promuovi la composizione rispetto all'ereditarietà**
---
- Ambiente
- Missione
- Log
- Json
- Nemici intelligenti
- Gestione stato

> Opzionale:
- Giocatore
- Livelli

# Modalita di sviluppo
- accesso ad un repository GitHub dove può lavorare in parallelo
- documentare il proprio codice e per le funzionalità implementate
- organizzare le modifiche o le implementazioni in fasi piu piccole e gestibili
- fare commit frequenti e scrivere messaggi chiari per ogni modifica
- testare le modifiche prima di fare pull request
- branch principale e può creare branch secondari per le funzionalità
- fare pull request per unire le modifiche al branch principale

# 1. Classe Ambiente
La classe Ambiente deve applicare modificatori ai personaggi e agli oggetti in gioco. Può essere utilizzata per influenzare il combattimento, gli oggetti e le abilità.
- Influenzare i personaggi (es: bonus/malus ai danni, cura, difesa…)
- Influenzare l’uso dell’inventario (es: oggetti vietati o potenziati)
- Influenzare gli oggetti stessi (es: le pozioni curano meno, le bombe fanno più danno…)
```python
class Ambiente:
    """Classe che rappresenta un ambiente di gioco, con modificatori e oggetti vietati."""
    def __init__(self, nome, modificatori=None, oggetti_vietati=None):
        self.nome = nome
        self.modificatori = modificatori or {}  # es: {"cura": -0.2, "danno": +0.1}
        self.oggetti_vietati = oggetti_vietati or []  # es: ["Pozione Rossa"]

    def modifica_cura(self, base_cura):
        """Modifica la cura in base all'ambiente."""
        fattore = self.modificatori.get("cura", 0)
        return int(base_cura * (1 + fattore))

    def modifica_danno(self, base_danno):
        """Modifica il danno in base all'ambiente."""
        fattore = self.modificatori.get("danno", 0)
        return int(base_danno * (1 + fattore))

    def oggetto_consentito(self, nome_oggetto):
        """Controlla se l'oggetto è vietato nell'ambiente."""
        return nome_oggetto not in self.oggetti_vietati

    def __str__(self):  # __str__ e un __repr__ per la rappresentazione dell'oggetto cioè per la stampa
        """Restituisce una stringa che rappresenta l'ambiente."""
        descr = f"Ambiente: {self.nome}"
        if self.descrizione:
            descr += f" - {self.descrizione}"
        if self.modificatori:
            modifiche = [f"{chiave}: {int(val*100)}%" for chiave, val in self.modificatori.items()]
            descr += "\n Modificatori: " + ", ".join(modifiche)
        if self.oggetti_vietati:
            descr += "\n Oggetti vietati: " + ", ".join(self.oggetti_vietati)
        return descr
    
    def ambienti_standard():
        """Restituisce una lista di ambienti standard."""
        return [
            Ambiente(
                nome="Vulcano",
                modificatori={"danno": 0.2, "cura": -0.3},
                oggetti_vietati=["Pozione Blu"],
                descrizione="Un luogo rovente. Le cure sono meno efficaci, i danni aumentano."
            ),
            Ambiente(
                nome="Foresta",
                modificatori={"cura": 0.2},
                descrizione="La natura aiuta la rigenerazione. Le cure sono più efficaci."
            ),
            Ambiente(
                nome="Palude",
                modificatori={"danno": -0.2},
                oggetti_vietati=["Bomba Acida"],
                descrizione="Un terreno viscido. I danni fisici sono ridotti."
            )
        ]
```
**Metodo**
- modifica_cura(50) | se "cura": -0.3 → ritorna 35
- modifica_danno(100) | se "danno": +0.2 → ritorna 120
- oggetto_consentito("Pozione Blu") | ritorna False se è vietata

**Negli oggetti:**

Aggiorna i metodi usa() di oggetti come PozioneCura, BombaAcida, ecc. per accettare un parametro opzionale ambiente, e modificare l’effetto in base a quello.

In Oggetto:
```python
# Nessun import richiesto

class Oggetto:
    def __init__(self, nome, tipo="neutro"):
        self.nome = nome
        self.tipo = tipo
        self.usato = False

    def usa(self, utilizzatore, bersaglio=None):
        raise NotImplementedError("Questo oggetto non ha effetto definito.")

class PozioneCura(Oggetto):
    def __init__(self, nome="Pozione Rossa", valore=30):
        super().__init__(nome, tipo="curativo")
        self.valore = valore
        self.tipo = "curativo"
        
    def usa(self, utilizzatore, bersaglio=None, ambiente=None):
        base = self.valore
        if ambiente:
            valore_effettivo = ambiente.modifica_cura(base)
        else:
            valore_effettivo = base

        target = bersaglio if bersaglio else utilizzatore
        target.salute = min(target.salute + valore_effettivo, target.salute_max)
        print(f"{target.nome} usa {self.nome} e recupera {valore_effettivo} salute!")
        self.usato = True

class BombaAcida(Oggetto):
    def __init__(self, nome="Bomba Acida", danno=30):
        super().__init__(nome)
        self.danno = danno
        self.tipo = "offensivo"

    def usa(self, utilizzatore, bersaglio=None, ambiente=None):
        if bersaglio is None:
            print(f"{utilizzatore.nome} cerca di usare {self.nome}, ma non ha un bersaglio!")
            return

        danno = self.danno
        if ambiente:
            danno = ambiente.modifica_danno(danno)

        bersaglio.subisci_danno(danno)
        print(f"{utilizzatore.nome} lancia {self.nome} su {bersaglio.nome}, infliggendo {danno} danni!")
        self.usato = True

class Medaglione(Oggetto):
    def __init__(self):
        super().__init__("Medaglione")
        self.tipo = "offensivo"

    def usa(self, utilizzatore, bersaglio=None, ambiente=None):
        target = bersaglio if bersaglio else utilizzatore
        target.attacco_max += 10
        print(f"{target.nome} indossa {self.nome} e aumenta il suo attacco massimo di 10!")
        self.usato = True
```
In torneo:
```python
from ambiente.ambiente import ambienti_standard
```
In gioca()
```python
ambienti_possibili = ambienti_standard()

for nemico in self.nemici:
    ambiente = random.choice(ambienti_possibili)
    print(f"\n[ {ambiente} ]")  # usa __str__ per stampare bene
    turno = Turno(self.giocatore, nemico, ambiente)
    turno.esegui()
```
Modificare utils utils.py per stampare i dettagli dell’ambiente e gli effetti applicati
```python
def mostra_ambiente(ambiente=None):
    if ambiente:
        print("\n=== Condizioni Ambientali ===")
        print(str(ambiente))
        print("=============================")
```
Modificare torneo.py per stampare i dettagli dell’ambiente e gli effetti applicati
```python
from ambiente.ambiente import ambienti_standard
from utils.utils import mostra_ambiente

# esempio ambiente casuale
ambiente = random.choice(ambienti_standard())
mostra_ambiente(ambiente)
```
# 2. Classe Missione
Un contenitore strutturato di:
- Ambienti
- Personaggi nemici
- Oggetti iniziali
- Premio (es. un oggetto)

> Completata quando il giocatore vince 3 tornei

missione.py
```python
class Missione:
    def __init__(self, nome, ambienti, oggetti_iniziali=None, nemici=None, premio=None, descrizione=""):
        self.nome = nome
        self.ambienti = ambienti
        self.oggetti_iniziali = oggetti_iniziali or []
        self.nemici = nemici or []
        self.premio = premio
        self.descrizione = descrizione
        self.tornei_vinti = 0
        self.completata = False

    def registra_vittoria(self):
        self.tornei_vinti += 1
        print(f"Torneo vinto! ({self.tornei_vinti}/3)")
        if self.tornei_vinti >= 3:
            self.completata = True
            print(f"\nMissione '{self.nome}' completata!")
            if self.premio:
                print(f"Hai ottenuto il premio: {self.premio.nome}")

    def get_ambiente_random(self):
        import random
        return random.choice(self.ambienti)

    def __str__(self):
        info = f"{self.nome}"
        if self.descrizione:
            info += f"{self.descrizione}"
        info += f"Tornei richiesti: 3 - Completati: {self.tornei_vinti}"
        if self.premio:
            info += f"\nPremio finale: {self.premio.nome}"
        return info
```
main.py
```python
# importa la classe principale Torneo

from utils.interfaccia import InterfacciaUtente
from torneo.torneo import Torneo
from missioni.missione import Missione
from ambiente.ambiente import ambienti_standard
from oggetti.oggetto import Medaglione

import os

def main():
    ambienti = ambienti_standard()
    missione = Missione(
        nome="Il Cammino del Campione",
        ambienti=ambienti,
        premio=Medaglione(),
        descrizione="Vinci 3 tornei per ottenere il leggendario Medaglione."
    )

    while True:
        print("\n=== MENU PRINCIPALE ===")
        scelta = InterfacciaUtente.chiedi_input(
            "Scegli un'opzione:\n1) Nuova partita\n2) Esci\n> ",
            opzioni=["1", "2"]
        )

        if scelta == "1":
            # pulisci lo schermo
            os.system('cls' if os.name == 'nt' else 'clear')
            torneo = Torneo(missione=missione)
            torneo.gioca()
        elif scelta == "2":
            print("Grazie per aver giocato!")
            break

if __name__ == "__main__":
    main()
```
torneo.py
```python
# random serve per scegliere il personaggio
import random
from utils.utils import mostra_benvenuto
from utils.utils import mostra_ambiente
from utils.utils import mostra_missione
from utils.interfaccia import InterfacciaUtente  # <--- nuovo import
from torneo.turno import Turno
from personaggi.classi import Mago, Guerriero, Ladro
from oggetti.oggetto import PozioneCura, BombaAcida, Medaglione
from inventario.inventario import Inventario
from ambiente.ambiente import ambienti_standard
from missioni.missione import Missione

class Torneo:
    def __init__(self, missione=None):
        self.giocatore = None
        self.nemici = []
        self.nemici_sconfitti = 0
        self.missione = missione

    def setup(self):
        mostra_benvenuto()
        # esempio ambiente casuale
        ambiente = random.choice(ambienti_standard())
        mostra_missione(self.missione)
        mostra_ambiente(ambiente)
        
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
            if self.missione:
                self.missione.registra_vittoria()
                if self.missione.completata:
                    self.giocatore.inventario.aggiungi(self.missione.premio)

        print("\nHai vinto il torneo!")
        print(f"Hai sconfitto {self.nemici_sconfitti} nemici.")
```
utils.py
```python
def mostra_ambiente(ambiente=None):
    if ambiente:
        print("\n=== Condizioni Ambientali ===")
        print(str(ambiente))
        print("=============================")
```
# 3. Classe Log
- Registrare ogni azione importante (attacchi, cure, uso oggetti, ambienti, eventi speciali)
- Mostrare o salvare un resoconto completo della missione o del torneo
- Scrivere su file per salvataggio o debug

log.py
```python
from datetime import datetime

class Log:
    def __init__(self):
        self.eventi = []

    def registra(self, messaggio):
        timestamp = datetime.now().strftime("%H:%M:%S")
        voce = f"[{timestamp}] {messaggio}"
        self.eventi.append(voce)
        print(voce)  # opzionale: stampa a schermo in tempo reale

    def mostra(self):
        print("\nRegistro eventi:")
        for evento in self.eventi:
            print(" -", evento)

    def salva_su_file(self, filename="registro.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for evento in self.eventi:
                f.write(evento + "\n")
        print(f"\nRegistro salvato su file: {filename}")
```
uso
```python
log = Log()
# durante il turno

log.registra(f"{self.giocatore.nome} attacca {self.nemico.nome}")
            log.salva_su_file()

log.mostra()
log.salva_su_file("log_partita.txt")
```

# 4. Classe Salvataggio/Caricamento JSON
```python

```
# 5. Classe Nemici intelligenti (Strategy pattern base)
```python

```
# 6. Classe Effetti
```python

```