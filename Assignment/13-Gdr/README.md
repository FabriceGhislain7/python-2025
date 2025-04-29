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
# V 13.0

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
# V 14.0

## Obiettivi del programma
- implementazione di oggetti curativi usando le classi
- usare oggetti all’interno di altri oggetti, un concetto chiave della programmazione a oggetti (OOP)

## Obiettivi didattici
- Classi che rappresentano oggetti diversi
- Come usare una lista di oggetti (inventario)
- Come un oggetto (pozione) può interagire con un altro oggetto (personaggio)

Implementare nella Classe personaggio
```python
self.salute_max = 200
```
```python
class Oggetto:
    def __init__(self, nome, effetto, valore):
        self.nome = nome  # Es: "Pozione"
        self.effetto = effetto  # Es: "cura"
        self.valore = valore  # Es: 20
        self.usato = False  # Es: torcia consumata

    def usa(self, personaggio):
        if self.effetto == "cura":
            personaggio.salute += self.valore
            print(f"{personaggio.nome} usa {self.nome} e recupera {self.valore} salute!")
            # personaggio.salute = min(personaggio.salute, 100)  # Limita la salute a 100
            personaggio.salute = min(personaggio.salute, personaggio.salute_max)  # Limita la salute al max del personaggio
            self.usato = True  # Indica che l'oggetto è stato usato
            print(f"Salute attuale: {personaggio.salute}\n")

class Personaggio:
    # aggiungo la proprieta inventario al costruttore
    self.inventario = []  # Lista di oggetti

    def usa_oggetto(self, nome_oggetto):
        for oggetto in self.inventario:
            if oggetto.nome == nome_oggetto:
                oggetto.usa(self)  # applico l'effetto dell oggetto al personaggio
                self.inventario.remove(oggetto)
                return  # uso return per uscire dal ciclo for
        print(f"{self.nome} non ha un oggetto chiamato {nome_oggetto}.")
```
Uso dell oggetto
```python
# creazione del personaggio
giocatore = Personaggio("Personaggio Principale")
# creazione di un oggetto
pozione = Oggetto("Pozione gialla", "cura", 20)
# aggiunta all inventario
giocatore.inventario.append(pozione)
# in gioca_duello il giocatore si cura usando la pozione
giocatore.usa_oggetto("Pozione gialla")
```

## Codice completo
```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.salute_max = 200
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []
        # aggiungo la proprieta inventario al costruttore
        self.inventario = []  # Lista di oggetti

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
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
        
    def usa_oggetto(self, nome_oggetto):
        for oggetto in self.inventario:
            if oggetto.nome == nome_oggetto:
                oggetto.usa(self)  # applico l'effetto dell oggetto al personaggio
                self.inventario.remove(oggetto)
                return  # uso return per uscire dal ciclo for
        print(f"{self.nome} non ha un oggetto chiamato {nome_oggetto}.")

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
        
class Oggetto:
    def __init__(self, nome, effetto, valore):
        self.nome = nome  # Es: "Pozione"
        self.effetto = effetto  # Es: "cura"
        self.valore = valore  # Es: 20
        self.usato = False  # Es: torcia consumata

    def usa(self, personaggio):
        if self.effetto == "cura":
            personaggio.salute += self.valore
            print(f"{personaggio.nome} usa {self.nome} e recupera {self.valore} salute!")
            personaggio.salute = min(personaggio.salute, personaggio.salute_max)  # Limita la salute al max del personaggio
            self.usato = True  # Indica che l'oggetto è stato usato
            print("-" * 80)
            print(f"Salute attuale: {personaggio.salute}\n")
        
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
    
    # creazione di un oggetto
    pozione = Oggetto("Pozione gialla", "cura", 20)

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
                giocatore.recupera_hp()
                nemici_sconfitti += 1
                
                # aggiunta all inventario
                giocatore.inventario.append(pozione)
                
                # in gioca_duello il giocatore si cura usando la pozione
                giocatore.usa_oggetto("Pozione gialla")
                
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
# V 15.0

## Obiettivi del programma
- modifica Oggetto in una classe base astratta
- creare sottoclassi ad ogni tipo di oggetto
- implementare un parametro che permetta di applicare il metodo al giocatore oppure al nemico in usa_oggetto

## Modificare Oggetto in una classe atratta
```python
class Oggetto:
    def __init__(self, nome):
        self.nome = nome
        self.usato = False
    
    # voglio che se un oggetto non e definito il programma si fermi mostrando l errore
    def usa(self, utilizzatore, bersaglio=None):
        raise NotImplementedError("Questo oggetto non ha effetto definito.")
        # se qualcuno chiama usa senza che sia stato implementato, il programma deve sollevare un ecceziione
        # senza usare il try except quando raise viene eseguito il programma si ferma mostrando l errore
```
Se invece voglio che il programma continui stampando l eccezione devo usare il try except cosi:
```python
try:
    oggetto = Oggetto("Pozione")
    oggetto.usa(personaggio)
except NotImplementedError as e:
    print("Errore catturato:", e)  # uso notimplementederror quando un oggetto non ha un effetto definito
```
Classi specifiche
```python
class PozioneCura(Oggetto):
    def __init__(self, nome="Pozione Rossa", valore=30):
        super().__init__(nome)
        self.valore = valore

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.salute = min(target.salute + self.valore, target.salute_max)
        print(f"{target.nome} usa {self.nome} e recupera {self.valore} salute!")
        self.usato = True
```
In modo da creare degli oggetti che abbiano effetto su un altro personaggio (che non sia l utilizzatore) devo
> modificare usa_oggetto() in Personaggio aggiungendo la proprieta `bersaglio`
```python
def usa_oggetto(self, nome_oggetto, bersaglio=None):
        for oggetto in self.inventario:
            if oggetto.nome == nome_oggetto:
                risultato = oggetto.usa(self, bersaglio)
                self.inventario.remove(oggetto)
                return risultato
        print(f"{self.nome} non ha un oggetto chiamato {nome_oggetto}.")
```
Adesso posso creare le classi di oggetti che hanno effetto su altri personaggi
```python
class BombaAcida(Oggetto):
    def __init__(self, nome="Bomba Acida", danno=30):
        super().__init__(nome)
        self.danno = danno

    def usa(self, utilizzatore, bersaglio=None):
        if bersaglio is None:
            print(f"{utilizzatore.nome} cerca di usare {self.nome}, ma non ha un bersaglio!")
            return
        bersaglio.subisci_danno(self.danno)
        print(f"{utilizzatore.nome} lancia {self.nome} su {bersaglio.nome}, infliggendo {self.danno} danni!")
        self.usato = True
```
```python
class Medaglione(Oggetto):
    def __init__(self):
        super().__init__("Medaglione")

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.attacco_max += 10
        print(f"{target.nome} indossa {self.nome}, aumentando il suo attacco massimo!")
        self.usato = True
```
Adesso posso usare gli oggetti su altri personaggi cosi:
```python
# creazione dell oggetto
pozione = PozioneCura()
bomba = BombaAcida()
medaglione = Medaglione()

# Al momento della vittoria contro un nemico del torneo
giocatore.inventario.append(PozioneCura())
giocatore.inventario.append(BombaAcida())

# uso degli oggetti sul giocatore
giocatore.usa_oggetto("Pozione Rossa", bersaglio=giocatore)  # posso omettere il bersaglio

# uso di un oggetto su un nemico
giocatore.usa_oggetto("Bomba Acida", bersaglio=nemico)
```
## Codice completo
```python
import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.salute_max = 200
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []
        self.inventario = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")

    def subisci_danno(self, danno):
        self.salute = max(0, self.salute - danno)
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")

    def sconfitto(self):
        return self.salute <= 0

    def recupera_hp(self):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * 0.3)
        nuova_salute = min(self.salute + recupero, 100)
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")

    def usa_oggetto(self, nome_oggetto, bersaglio=None):
        for oggetto in self.inventario:
            if oggetto.nome == nome_oggetto:
                risultato = oggetto.usa(self, bersaglio)
                self.inventario.remove(oggetto)
                return risultato
        print(f"{self.nome} non ha un oggetto chiamato {nome_oggetto}.")

class Mago(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 80

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min - 5, self.attacco_max + 10)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} lancia un incantesimo su {bersaglio.nome} per {danno} danni!")

    def recupera_hp(self):
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
        recupero = random.randint(10, 40)
        self.salute = min(self.salute + recupero, 140)
        print(f"\n{self.nome} si cura rapidamente e recupera {recupero} HP. Salute attuale: {self.salute}")
        
class Oggetto:
    def __init__(self, nome):
        self.nome = nome
        self.usato = False

    def usa(self, utilizzatore, bersaglio=None):
        raise NotImplementedError("Questo oggetto non ha effetto definito.")

class PozioneCura(Oggetto):
    def __init__(self, nome="Pozione Rossa", valore=30):
        super().__init__(nome)
        self.valore = valore

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.salute = min(target.salute + self.valore, target.salute_max)
        print(f"{target.nome} usa {self.nome} e recupera {self.valore} salute!")
        self.usato = True

class BombaAcida(Oggetto):
    def __init__(self, nome="Bomba Acida", danno=30):
        super().__init__(nome)
        self.danno = danno

    def usa(self, utilizzatore, bersaglio=None):
        if bersaglio is None:
            print(f"{utilizzatore.nome} cerca di usare {self.nome}, ma non ha un bersaglio!")
            return
        bersaglio.subisci_danno(self.danno)
        print(f"{utilizzatore.nome} lancia {self.nome} su {bersaglio.nome}, infliggendo {self.danno} danni!")
        self.usato = True

class Medaglione(Oggetto):
    def __init__(self):
        super().__init__("Medaglione")

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.attacco_max += 10
        print(f"{target.nome} indossa {self.nome}, aumentando il suo attacco massimo!")
        self.usato = True

def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")

def gioca_torneo():
    mostra_benvenuto()

    classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]
    giocatore = random.choice(classi_giocatore)
    print(f"Hai ottenuto il personaggio: {giocatore.nome}\n")

    nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
    random.shuffle(nemici)
    
    nemici_sconfitti = 0

    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico.nome}")
        turno = 1

        while True:
            print(f"Turno {turno}:")

            # aggiunta oggetti ogni turno (esempio semplice)
            giocatore.inventario.append(PozioneCura())
            giocatore.inventario.append(BombaAcida())
            giocatore.inventario.append(Medaglione())

            # uso BombaAcida contro il nemico
            giocatore.usa_oggetto("Bomba Acida", bersaglio=nemico)

            giocatore.attacca(nemico)
            print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)

            if nemico.sconfitto():
                print(f"Hai vinto il duello contro {nemico.nome}!")
                giocatore.recupera_hp()
                nemici_sconfitti += 1

                # usa la pozione per curarsi
                giocatore.usa_oggetto("Pozione Rossa")
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
# V 16.0

## Obiettivi del programma
- Implementare la logica del torneo che quando un nemico perde il duello il personaggio vince il suo inventario
```python
nemico.inventario = [PozioneCura(), BombaAcida(), Medaglione()]
```
```python
def prendi_inventario(self, altro_personaggio):
    if altro_personaggio.inventario:
        print(f"\n{self.nome} ottiene l'inventario di {altro_personaggio.nome}:")
        for oggetto in altro_personaggio.inventario:
            print(f" - {oggetto.nome}")
            self.inventario.append(oggetto)
        altro_personaggio.inventario.clear()  # svuota l'inventario del nemico
    else:
        print(f"{altro_personaggio.nome} non aveva oggetti nell'inventario.")
```
```python
giocatore.prendi_inventario(nemico)
```
# V 17.0

## Obiettivi del programma
- passare a una struttura più modulare e pulita con classi dedicate a:

Classe | Responsabilità
---|---
Personaggio | Gestire le proprietà e i metodi di un personaggio
Oggetto | Gestire le proprietà e i metodi di un oggetto
Inventario | Gestire oggetti di un personaggio (aggiunta, rimozione, uso)
Turno | Gestire un singolo turno (azioni di attacco, uso oggetti)
Torneo | Gestire tutto il ciclo dei combattimenti, gestione dei nemici, vincite/sconfitte

Creo la classe Inventario in modo da:
- alleggerire il carico di lavoro della classe Personaggio
- delegare le funzionalita relative agli array alla classe Inventario
```python
class Inventario:
    def __init__(self):
        self.oggetti = []
    
    def aggiungi(self, oggetto):
        self.oggetti.append(oggetto)

    def usa_oggetto(self, nome_oggetto, utilizzatore, bersaglio=None):
        for oggetto in self.oggetti:
            if oggetto.nome == nome_oggetto:
                oggetto.usa(utilizzatore, bersaglio)
                self.oggetti.remove(oggetto)
                return
        print(f"{utilizzatore.nome} non ha un oggetto chiamato {nome_oggetto}.")

class Turno:
    def __init__(self, giocatore, nemico):
        self.giocatore = giocatore
        self.nemico = nemico
        self.numero_turno = 1

    def esegui(self):
        while True:
            print(f"--- Turno {self.numero_turno} ---")

            # Azioni del giocatore
            self.giocatore.inventario.aggiungi(PozioneCura())
            self.giocatore.inventario.aggiungi(BombaAcida())
            self.giocatore.inventario.aggiungi(Medaglione())

            # Usa bomba acida contro il nemico
            self.giocatore.inventario.usa_oggetto("Bomba Acida", self.giocatore, self.nemico)
            self.giocatore.attacca(self.nemico)
            print("Storico danni subiti dal nemico:", self.nemico.storico_danni_subiti)

            if self.nemico.sconfitto():
                print(f"Hai vinto contro {self.nemico.nome}!")
                self.giocatore.recupera_hp()
                self.giocatore.inventario.usa_oggetto("Pozione Rossa", self.giocatore)
                break

            # Azioni del nemico
            self.nemico.attacca(self.giocatore)
            print("Storico danni subiti dal giocatore:", self.giocatore.storico_danni_subiti)

            if self.giocatore.sconfitto():
                print(f"Sei stato sconfitto da {self.nemico.nome}!")
                break

            self.numero_turno += 1

class Torneo:
    def __init__(self):
        self.giocatore = None
        self.nemici = []
        self.nemici_sconfitti = 0

    def setup(self):
        mostra_benvenuto()
        # Configurazioni iniziali del torneo

        # configurazioni personaggio principale
        classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]
        self.giocatore = random.choice(classi_giocatore)
        self.giocatore.inventario = Inventario()  # assegna un inventario
        print(f"Hai ricevuto il personaggio: {self.giocatore.nome}")

        # configurazioni nemici
        self.nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
        random.shuffle(self.nemici)

    def gioca(self):
        self.setup()

        for nemico in self.nemici:
            turno = Turno(self.giocatore, self.nemico)\
            turno.esegui()

            if self.giocatore.sconfitto():
                print(f"Hai sconfitto {self.nemici_sconfitti} nemici")
                return

            # incremento il contatore dei nemici sconfitti
            self.nemici_sconfitti +=1

        print("Hai vinto il torneo")
        print(f"Hai sconfitto {self.nemici_sconfitti} nemici")

def main():
    torneo = Torneo()
    toRneo.gioca()

# Firma di avvio
if __name__ == "__main__":
    main()
