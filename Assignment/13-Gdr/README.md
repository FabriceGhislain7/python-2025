# GDR Obiettivi didattici

- Usare funzioni con parametri e valori di ritorno
- Simulare cicli di gioco
- Gestire l'input dell'utente
- Gestire errori
- Gestire la letture e scrittura su file json

| FASE | Argomento Python                   | Implementazione nel gioco                              |
| ---- | ---------------------------------- | ------------------------------------------------------ |
| 1    | Funzioni                           | Struttura modulare con def                             |
| 2    | Parametri e ritorni (return)       | crea_personaggio(nome) restituisce un dizionario       |
| 3    | Dizionari                          | Gestione di salute, attacco, nome                      |
| 4    | Condizioni (if, else)              | Controllo della salute per capire se qualcuno ha perso |
| 5    | Cicli (while)                      | Turni di combattimento                                 |
| 6    | Import di librerie (import random) | Generare danni casuali                                 |
| 7    | List comprehension                 | Inventario o log dei danni subiti                      |
| 8    | Classi e oggetti (class)           | Trasformare personaggio da dict a oggetto              |
| 9    | File (open, read, write)           | Salvare e caricare le partite attraverso una classe    |
| 10   | Gestione errori (try, except)      | Input dell'utente attraverso una classe                |

# V 1.0

## Obiettivi del programma

- Creare un gioco a turni dove due personaggi si scontrano
- Usare funzioni in modo da gestire:
- attacco
- turni
- salute

## Funzioni principali

- Funzione: stampa un messaggio di benvenuto
- Funzione: crea un personaggio con le seguenti caratteristiche:

```json
{
  "nome": "Nome del personaggio",
  "salute": 100,
  "attacco_min": 10,
  "attacco_max": 20
}
```

- Funzione: esegue un attacco
- Funzione: controlla se qualcuno è sconfitto
- Funziome principale: gestisce il ciclo di gioco

```python
import random

# Funzione senza parametri: stampa un messaggio di benvenuto
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")  # Non prende input, non restituisce nulla. Serve solo a stampare testo

# Funzione con parametri: crea un personaggio
def crea_personaggio(nome):  # restituisce un dizionario
    personaggio = {
        "nome": nome,
        "salute": 100,
        "attacco_min": 10,
        "attacco_max": 20
    }
    return personaggio

# Funzione con parametri: esegue un attacco
def esegui_attacco(attaccante, difensore):  # prende due personaggi
    danno = random.randint(attaccante["attacco_min"],attaccante["attacco_max"])  # sceglie un numero casuale tra attacco_min ed attacco_max
    difensore["salute"] -= danno  # sottrae il danno alla salute dell altro personaggio
    # stampo il messaggio di attacco
    print(f"{attaccante['nome']} attacca {difensore['nome']} e infligge {danno} danni!")  # stampa il messaggio di attacco
    # Se la salute scende sotto 0, la riportiamo a zero
    if difensore["salute"] < 0:
        difensore["salute"] = 0
    # stampo la salute del difensore
    print(f"{difensore['nome']} ha {difensore['salute']} punti salute rimasti.")  # stampa la salute del difensore

# Funzione con parametri: controlla se qualcuno è sconfitto
def personaggio_sconfitto(personaggio):  # prende il personaggio
    # ritorna un valore booleano
    return personaggio["salute"] <= 0  # controlla se la salute è zero

# stampo il messaggio di benvenuto
mostra_benvenuto()

# provo la funzione di creazione del personaggio
nome = input("Inserisci il nome del tuo personaggio: ")
personaggio = crea_personaggio(nome)
# stampo il personaggio
print(f"Personaggio creato: {personaggio['nome']}, Salute: {personaggio['salute']}, Attacco min: {personaggio['attacco_min']}, Attacco max: {personaggio['attacco_max']}")

# creo due personaggi dummy
giocatore = crea_personaggio("Personaggio amico")
nemico = crea_personaggio("Nemico")

#stampo i personaggi
print(giocatore)
print(nemico)
# oppure lo stampo formattato
print(f"Personaggio amico: {giocatore['nome']}, Salute: {giocatore['salute']}, Attacco min: {giocatore['attacco_min']}, Attacco max: {giocatore['attacco_max']}")
print(f"Nemico: {nemico['nome']}, Salute: {nemico['salute']}, Attacco min: {nemico['attacco_min']}, Attacco max: {nemico['attacco_max']}")

# stampo il messaggio di inizio combattimento
print("Inizia il combattimento!")

# provo la funzione attacco
esegui_attacco(giocatore, nemico)
esegui_attacco(nemico, giocatore)

# provo personaggio sconfitto
if personaggio_sconfitto(nemico):
    print(f"{nemico['nome']} è sconfitto!")
else:
    print(f"{nemico['nome']} è ancora in piedi!")

if personaggio_sconfitto(giocatore):
    print(f"{giocatore['nome']} è sconfitto!")
else:
    print(f"{giocatore['nome']} è ancora in piedi!")
```

# V 2.0

## Obiettivi del programma

- Inserire la logica di gioco proncipale (il loop nel quale avviene il duello) all interno di una funzione specifica
- Creare il blocco main() per eseguire la logica di gioco principale

## Descrizione della logica di gioco

- Il giocatore attacca (incomincia il turno)
- Si controlla se il nemico è sconfitto
- Il secondo personaggio attacca
- Si controlla se il giocatore è sconfitto
- Si ripete finché uno dei due ha salute = 0

```python
def gioca_duello():
    # stampo il messaggio di benvenuto
    mostra_benvenuto()

    # Creiamo i personaggi
    giocatore = crea_personaggio("Personaggio Principale")
    nemico = crea_personaggio("Nemico")

    # definiamo un contatore per i turni
    turno = 1

     # Ciclo finché qualcuno perde (quando la salute è zero)
    while True:
        print(f"Turno {turno}:")

        # Attacco del giocatore
        esegui_attacco(giocatore, nemico)

        # controlla se il nemico è sconfitto
        if personaggio_sconfitto(nemico):
            print("Hai vinto il duello!")
            break  # esci dal ciclo nel caso di vittoria

        # Attacco del nemico
        esegui_attacco(nemico, giocatore)

        # controlla se il giocatore è sconfitto
        if personaggio_sconfitto(giocatore):
            print("Sei stato sconfitto!")
            break # esci dal ciclo nel caso di sconfitta

        # incremento il contatore dei turni
        turno += 1

# punto di ingresso
def main():
    gioca_duello()

# Esegui il gioco
if __name__ == "__main__":
    main()
```

# V 3.0

## Obiettivi del programma

- Implementare una lista che memorizza quanti danni ogni personaggio subisce turno dopo turno

Modifica la funzione crea_personaggio così:

```python
def crea_personaggio(nome):
    return {
        "nome": nome,
        "salute": 100,
        "attacco_min": 5,
        "attacco_max": 80,
        "storico_danni_subiti": []  # <--- nuova lista
         }
```

- Aggiorna la funzione esegui_attacco da così:

```python
# Funzione con parametri: esegue un attacco
def esegui_attacco(attaccante, difensore):  # prende due personaggi
    danno = random.randint(attaccante["attacco_min"],attaccante["attacco_max"])  # sceglie un numero casuale tra attacco_min ed attacco_max
    difensore["salute"] -= danno  # sottrae il danno alla salute dell altro personaggio
    # stampo il messaggio di attacco
    print(f"{attaccante['nome']} attacca {difensore['nome']} e infligge {danno} danni!")  # stampa il messaggio di attacco
    # Se la salute scende sotto 0, la riportiamo a zero
    if difensore["salute"] < 0:
        difensore["salute"] = 0
    # stampo la salute del difensore
    print(f"{difensore['nome']} ha {difensore['salute']} punti salute rimasti.")  # stampa la salute del difensore
```

A così:

```python
def esegui_attacco(attaccante, difensore):  # prende due personaggi
    danno = random.randint(attaccante["attacco_min"],attaccante["attacco_max"])
    difensore["salute"] -= danno
    difensore["storico_danni_subiti"].append(danno)  # <--- salviamo il danno
    print(f"{attaccante['nome']} attacca {difensore['nome']} e infligge {danno} danni!")
    if difensore["salute"] < 0:
        difensore["salute"] = 0
    print(f"{difensore['nome']} ha {difensore['salute']} punti salute rimasti.")
```

- stampare lo storico dei danni subiti da ogni personaggio:

```python
print("Storico danni subiti dal nemico:", nemico["storico_danni_subiti"])
print("Storico danni subiti dal giocatore:", giocatore["storico_danni_subiti"])
```

# V 4.0

## Obiettivi del programma

- usare le comprehensions (list comprehensions) in modo da creare più personaggi in un modo compatto

Senza list comprehension:

```python
nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
nemici = []
for nome in nomi_nemici:
    nemici.append(crea_personaggio(nome))
print(nemici)
```

Con list comprehension:

```python
nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
nemici = [crea_personaggio(nome) for nome in nomi_nemici]
print(nemici)
```

Aggiorna la funzione gioca_duello da così:

```python
# Creiamo i personaggi
giocatore = crea_personaggio("Personaggio Principale")
nemico = crea_personaggio("Nemico")
```

A così:

```python
# Creazione del giocatore
giocatore = crea_personaggio("Personaggio Principale")

# Creazione di più nemici
nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
nemici = [crea_personaggio(nome) for nome in nomi_nemici]

# Scegliamo il primo nemico per iniziare il duello
nemico = nemici[0]

# Oppure scelgo casualmente un nemico
nemico = random.choice(nemici)
```

# V 5.0

## Obiettivi del programma

- Modificare il valore di attacco tra 5 e 35
- Implementare il passaggio al prossimo nemico se il primo viene sconfitto
- Se perde, il gioco finisce

## Funzionalita del torneo

- Il giocatore inizia con 100 di salute come il nemico
- Se il giocatore vince, affronta il prossimo nemico
- Se perde, finisce il gioco
- Alla fine viene mostrato un riepilogo del torneo con l elenco dei nemici sconfitti dal giocatore (sia il numero che i nomi)

```python
def gioca_duello():
    # stampo il messaggio di benvenuto
    mostra_benvenuto()

    # Creazione del giocatore
    giocatore = crea_personaggio("Personaggio Principale")

    # Creazione di più nemici
    nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
    nemici = [crea_personaggio(nome) for nome in nomi_nemici]

    # Faccio lo shuffle dei nemici
    random.shuffle(nemici)

    # Statistiche torneo
    nemici_sconfitti = 0

    # Loop sul torneo: un nemico alla volta
    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico['nome']}")

        # definiamo un contatore per i turni
        turno = 1

        # Ciclo finché qualcuno perde (quando la salute è zero)
        while True:
            print(f"Turno {turno}:")

            # Attacco del giocatore
            esegui_attacco(giocatore, nemico)

            # stampo lo storico dei danni subiti dal nemico
            print("Storico danni subiti dal nemico:", nemico["storico_danni_subiti"])

            # controlla se il nemico è sconfitto
            if personaggio_sconfitto(nemico):
                print(f"Hai vinto il duello contro {nemico['nome']}!")

                # incrementa il contatore dei nemici sconfitti
                nemici_sconfitti += 1

                break  # Passa al prossimo nemico

            # Attacco del nemico
            esegui_attacco(nemico, giocatore)

            # stampo lo storico dei danni subiti dal giocatore
            print("Storico danni subiti dal giocatore:", giocatore["storico_danni_subiti"])

            # controlla se il giocatore è sconfitto
            if personaggio_sconfitto(giocatore):
                print("Sei stato sconfitto!")

                # stampa quanti nemici hai sconfitto
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")

                # break → il ciclo continua dopo la sconfitta
                return # esci dalla funzione nel caso di sconfitta

            # incremento il contatore dei turni
            turno += 1

    # Se il giocatore ha sconfitto tutti
    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")
```

# V 6.0

## Obiettivi del programma

- Implementare funzionalità di recupero salute tra un nemico e l'altro
- Dopo ogni vittoria il giocatore recupera una percentuale fissa di salute che gli è rimasta (30%)
- Se la salute è maggiore di 100, la riporto a 100
- Dopo ogni nemico sconfitto, il giocatore recupera salute e stampiamo un riepilogo della salute attuale

```python
if personaggio_sconfitto(nemico):
    print(f"Hai vinto il duello contro {nemico['nome']}!")

    # Recupero salute tra scontri (30)
    percentuale_recupero = 0.3
    salute_recuperata = int(giocatore["salute"] * percentuale_recupero)

    # Limitiamo il recupero della salute a 100
    if giocatore["salute"] + salute_recuperata > 100:
        salute_recuperata = 100

    # recupero salute
    giocatore["salute"] += salute_recuperata

    # stampo la salute del giocatore
    print(f"\nHai recuperato {salute_recuperata} punti salute! Salute attuale: {giocatore['salute']}")

    # incrementa il contatore dei nemici sconfitti
    nemici_sconfitti += 1

    break  # Passa al prossimo nemico
```

# V 7.0

## Obiettivi del programma

> Creare una versione dimostrativa che spiega i concetti base della programmazione ad oggetti
Trasformare il personaggio in una classe (trasformare il dizionario in una classe)
Implementare le basi della programmazione orientata agli oggetti (OOP) in modo da:

- Creare una classe Personaggio che rappresenta un personaggio del gioco

## Obiettivi didattici

Capire cosa sono:

- Le classi
- I metodi
- Il costruttore `__init__()`
- L’uso di self

- `__init__()` il costruttore della classe. Viene eseguito automaticamente quando crei un oggetto da una classe
- `self` È il riferimento all'istanza attuale dell'oggetto. Ogni volta che chiami un metodo su un oggetto, self rappresenta quell’oggetto

Creazione della classe Personaggio

```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 10
        self.attacco_max = 20
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
```
## REGOLA
- Se il metodo risponde a una domanda, usa return
- Se il metodo fa un’azione, modifica o stampa, non serve return

Uso della classe Personaggio

da cosi (versione con funzioni)
```python
# creo due personaggi dummy
giocatore = crea_personaggio("Personaggio Principale")
nemico = crea_personaggio("Nemico")
```

A cosi (versione ad oggetti)
```python
# creo due personaggi dummy
giocatore = Personaggio("Personaggio Principale")
nemico = Personaggio("Nemico")
# uso un metodo della classe
giocatore.attacca(nemico)  # uso l oggetto giocatore non la classe Personaggio
```
## REGOLA
Quando scriviamo:
- giocatore = Personaggio("Personaggio Principale")
Il programma intende:
- Personaggio.__init___(giocatore, "Personaggio Principale") cioe (self, nome)

# Vantaggi pratici delle classi
Vantaggio | Descrizione
---|---
Organizzazione | Raggruppa dati e comportamenti nello stesso posto
Riutilizzabilità | Puoi creare più oggetti dalla stessa classe
Espandibilità | Puoi aggiungere metodi senza riscrivere tutto
Leggibilità | Il codice è più chiaro
Modularità | Ogni classe è un modulo a sé stante
Non ripetitività | Non ripeti codice, ma lo riutilizzi
Incapsulamento | Protegge i dati interni e maschera la complessità

# V 8.0

## Obiettivi del programma
- Usare a classe Personaggio in modo da gestire il duello singolo
```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 10
        self.attacco_max = 20
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")
        
def gioca_duello():
    mostra_benvenuto()
    
    giocatore = Personaggio("Personaggio Principale")
    nemico = Personaggio("Nemico")
    
    turno = 1
    
    while True:
        print(f"Turno {turno}")
        
        giocatore.attacca(nemico)
        if nemico.sconfitto():
            print("Hai vinto il duello!")
            break
        
        nemico.attacca(giocatore)
        if giocatore.sconfitto():
            print("Sei stato sconfitto... Riprova!")
            break

        turno += 1

    print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)
    print("Storico danni subiti dal giocatore:", giocatore.storico_danni_subiti)
    
def main():
    gioca_duello()
    
if __name__ == "__main__":
    main()
```

# V 9.0

## Obiettivi del programma
- Implementare la logica del torneo
```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")
        
def gioca_torneo():
    mostra_benvenuto()

    # Creazione del giocatore
    giocatore = Personaggio("Personaggio Principale")

    # Creazione dei nemici
    nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
    nemici = [Personaggio(nome) for nome in nomi_nemici]
    random.shuffle(nemici)

    nemici_sconfitti = 0

    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico.nome}")
        turno = 1

        while True:
            print(f"Turno {turno}:")

            giocatore.attacca(nemico)
            print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)

            if nemico.sconfitto():  # uso di funzione con return
                print(f"Hai vinto il duello contro {nemico.nome}!")
                nemici_sconfitti += 1
                
                break

            nemico.attacca(giocatore)
            print("Storico danni subiti dal giocatore:", giocatore.storico_danni_subiti)

            if giocatore.sconfitto():  # uso di funzione applicata a due oggetti diversi (nemico e giocatore)
                print("Sei stato sconfitto!")
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")
                
                return

            turno += 1

    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")

def main():
    gioca_torneo()

if __name__ == "__main__":
    main()
```
# V 10.0

## Obiettivi del programma
- Implementare funzionalità di recupero salute tra un nemico e l'altro
- Dopo ogni vittoria il giocatore recupera una percentuale fissa di salute che gli è rimasta (30%)
- Se la salute è maggiore di 100, la riporto a 100
- Dopo ogni nemico sconfitto, il giocatore recupera salute e stampiamo un riepilogo della salute attuale
```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
    def recupera_hp(self, percentuale):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * percentuale)
        nuova_salute = min(self.salute + recupero, 100)  # uso min per non superare 100 selezionando il valore piu basso
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")
        
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")
        
def gioca_torneo():
    mostra_benvenuto()

    # Creazione del giocatore
    giocatore = Personaggio("Personaggio Principale")

    # Creazione dei nemici
    nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
    nemici = [Personaggio(nome) for nome in nomi_nemici]
    random.shuffle(nemici)

    nemici_sconfitti = 0

    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico.nome}")
        turno = 1

        while True:
            print(f"Turno {turno}:")

            giocatore.attacca(nemico)
            print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)

            if nemico.sconfitto():
                print(f"Hai vinto il duello contro {nemico.nome}!")
                
                # Recupero salute del 30%
                giocatore.recupera_hp(0.3)
                
                nemici_sconfitti += 1
                
                break

            nemico.attacca(giocatore)
            print("Storico danni subiti dal giocatore:", giocatore.storico_danni_subiti)

            if giocatore.sconfitto():
                print("Sei stato sconfitto!")
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")
                
                return

            turno += 1

    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")

def main():
    gioca_torneo()

if __name__ == "__main__":
    main()
```
# V 11.0

## Obiettivi del programma
- Usare l override aggiungendo abilità speciali a personaggi specifici
- L override è un comportamento specifico di una classe in una determinata situazione


## Obiettivi didattici

Capire:
- Le classi figlie (ereditarietà)
- Come modificare il comportamento (override dei metodi)
- Come scrivere codice riusabile, espandibile, leggibile
```python
class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 10
        self.attacco_max = 20

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        # bersaglio.salute -= danno
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} danni.")

class Mago(Personaggio):  # sto creando una classe derivata cioè che estende quella originale
    def attacca(self, bersaglio):
        # danno = random.randint(15, 30)
        danno = random.randint(self.attacco_min - 5, self.attacco_max + 10)
        # bersaglio.salute -= danno
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} lancia un incantesimo su {bersaglio.nome} per {danno} danni!")

class Guerriero(Personaggio):
    def attacca(self, bersaglio):
        # danno = random.randint(20, 45)
        danno = random.randint(self.attacco_min + 15, self.attacco_max + 20)
        # bersaglio.salute -= danno
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce con la spada {bersaglio.nome} per {danno} danni!")

# Creazione del giocatore
giocatore = Personaggio("Personaggio Principale")

# uso
# Creazione del giocatore
giocatore = Mago("Nome del Mago")
nemico = Guerriero("Nemico")

giocatore.attacca(nemico)
nemico.attacca(giocatore)
```

## Implementazione
- Creare un terzo personaggio specifico
- Inserire i personaggi all interno della logica di gioco
```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
    def recupera_hp(self, percentuale):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * percentuale)
        nuova_salute = min(self.salute + recupero, 100)
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")

class Mago(Personaggio):
    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min - 5, self.attacco_max + 10)
        # bersaglio.salute -= danno
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} lancia un incantesimo su {bersaglio.nome} per {danno} danni!")

class Guerriero(Personaggio):
    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 15, self.attacco_max + 20)
        # bersaglio.salute -= danno
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce con la spada {bersaglio.nome} per {danno} danni!")
        
class Ladro(Personaggio):
    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 5, self.attacco_max + 5)
        # bersaglio.salute -= danno
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce furtivamente {bersaglio.nome} per {danno} danni!")
        
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")
        
def gioca_torneo():
    mostra_benvenuto()

    # Scelta casuale del giocatore tra le 3 classi
    classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]
    giocatore = random.choice(classi_giocatore)
    print(f"Hai ottenuto il personaggio: {giocatore.nome}\n")

    # Nemici: uno per classe
    nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
    random.shuffle(nemici)

    nemici_sconfitti = 0

    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico.nome}")
        turno = 1

        while True:
            print(f"Turno {turno}:")
            giocatore.attacca(nemico)
            print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)

            if nemico.sconfitto():
                print(f"Hai vinto il duello contro {nemico.nome}!")
                giocatore.recupera_hp(0.3)
                nemici_sconfitti += 1
                break

            nemico.attacca(giocatore)
            print("Storico danni subiti dal giocatore:", giocatore.storico_danni_subiti)

            if giocatore.sconfitto():
                print("Sei stato sconfitto!")
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")
                return

            turno += 1

    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")

def main():
    gioca_torneo()

if __name__ == "__main__":
    main()
```
# V 12.0

## Obiettivi del programma
- personalizzare la salute iniziale in base alla classe
- cioè ridefinire __init__() in ogni sottoclasse

## Suggerimenti
- usare `super` che è una funzione che ti permette di accedere ai metodi della superclasse (cioè la classe madre), direttamente da una classe figlia
- Serve per non riscrivere codice già esistente nella classe base, ma estenderlo o modificarlo in modo chiaro

## Esempio
```python
# Hai questa classe base:
class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
# questa e una classe figlia che usa super in modo da sovrascrivere il valore della salute
class Guerriero(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)  # Chiama l'__init__ di Personaggio
        self.salute = 120       # Sovrascrive il valore della salute
```
__super().__init__(nome)__
- Chiama il costruttore della superclasse Personaggio
- Passa nome come parametro, perché Personaggio.__init__() si aspetta nome
- Inizializza self.nome come nella classe base
## Implementazione
```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
    def recupera_hp(self, percentuale):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * percentuale)
        nuova_salute = min(self.salute + recupero, 100)
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")

class Mago(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 80  # Salute base più bassa per il Mago

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min - 5, self.attacco_max + 10)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} lancia un incantesimo su {bersaglio.nome} per {danno} danni!")

class Guerriero(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 120  # Salute base più alta per il Guerriero

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 15, self.attacco_max + 20)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce con la spada {bersaglio.nome} per {danno} danni!")

class Ladro(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 140  # Salute base molto alta per il Ladro

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 5, self.attacco_max + 5)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce furtivamente {bersaglio.nome} per {danno} danni!")
        
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")
        
def gioca_torneo():
    mostra_benvenuto()

    # Scelta casuale del giocatore tra le 3 classi
    classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]
    giocatore = random.choice(classi_giocatore)
    print(f"Hai ottenuto il personaggio: {giocatore.nome}\n")

    # Nemici: uno per classe
    nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
    random.shuffle(nemici)

    nemici_sconfitti = 0

    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico.nome}")
        turno = 1

        while True:
            print(f"Turno {turno}:")
            giocatore.attacca(nemico)
            print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)

            if nemico.sconfitto():
                print(f"Hai vinto il duello contro {nemico.nome}!")
                giocatore.recupera_hp(0.3)
                nemici_sconfitti += 1
                break

            nemico.attacca(giocatore)
            print("Storico danni subiti dal giocatore:", giocatore.storico_danni_subiti)

            if giocatore.sconfitto():
                print("Sei stato sconfitto!")
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")
                return

            turno += 1

    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")

def main():
    gioca_torneo()

if __name__ == "__main__":
    main()
```
# V 12.0

## Obiettivi del programma
__override__

aggiorniamo recupera_hp() per essere diverso per ogni classe
- Mago -> Recupero più lento (solo 20% della salute attuale)
- Guerriero -> Recupero costante (30 HP fissi)
- Ladro -> Recupero veloce ma casuale (tra 10 e 40 HP)
## Problema
- metodo nella classe base che accetta un parametro (recupera_hp(percentuale)), ma nelle classi derivate (Mago, Guerriero, Ladro) hai fatto override senza quel parametro:
```python
# CLASSE BASE
def recupera_hp(self, percentuale):  # <-- accetta un argomento

# CLASSI DERIVATE
def recupera_hp(self):  # <-- non accetta niente → ERRORE!

# In gioca_torneo
giocatore.recupera_hp(0.3)

# Deve diventare
giocatore.recupera_hp()
```
## Implementazione
```python
class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        # self.salute -= danno
        self.salute = max(0, self.salute - danno)
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
    def recupera_hp(self):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * 0.3)
        nuova_salute = min(self.salute + recupero, 100)
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")

class Mago(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 80

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min - 5, self.attacco_max + 10)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} lancia un incantesimo su {bersaglio.nome} per {danno} danni!")

    def recupera_hp(self):
        # Recupero più lento (solo 20% della salute attuale)
        recupero = int(self.salute * 0.2)
        self.salute = min(self.salute + recupero, 80)
        print(f"\n{self.nome} medita e recupera {recupero} HP. Salute attuale: {self.salute}")

class Guerriero(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 120

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 15, self.attacco_max + 20)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce con la spada {bersaglio.nome} per {danno} danni!")

    def recupera_hp(self):
        # Recupero costante (30 HP fissi)
        recupero = 30
        self.salute = min(self.salute + recupero, 120)
        print(f"\n{self.nome} si fascia le ferite e recupera {recupero} HP. Salute attuale: {self.salute}")

class Ladro(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 140

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 5, self.attacco_max + 5)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce furtivamente {bersaglio.nome} per {danno} danni!")

    def recupera_hp(self):
        # Recupero veloce ma casuale (tra 10 e 40 HP)
        recupero = random.randint(10, 40)
        self.salute = min(self.salute + recupero, 140)
        print(f"\n{self.nome} si cura rapidamente e recupera {recupero} HP. Salute attuale: {self.salute}")
```