# OOP
## 1. Modularità: da funzioni pure a oggetti

Funzionale:
Scrivi funzioni pure che trasformano dati:

```python
def calcola_area(rettangolo):
    return rettangolo["larghezza"] * rettangolo["altezza"]
```
OOP:
Raggruppi dati e comportamenti in oggetti:

```python
class Rettangolo:
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
    
    def area(self):
        return self.larghezza * self.altezza
```
## 2. Concetto base: la Classe
Una classe è uno stampo per creare oggetti (istanze):

```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        print(f"Ciao, sono {self.nome}")

p = Persona("Persona")
p.saluta()
```
## 3. Stato vs. Immutabilità
Nella FP, lo stato è immutabile. In OOP, gli oggetti hanno stato interno modificabile:

```python
class Contatore:
    def __init__(self):
        self.valore = 0
    
    def incrementa(self):
        self.valore += 1
```
> In OOP è normale avere mutazioni di stato, mentre in FP usi copie aggiornate.

## 4. Self vs Parametri espliciti
Le funzioni FP ricevono tutti i dati come parametri.

I metodi OOP ricevono implicitamente l’oggetto stesso come primo parametro: self.

## 5. Ereditarietà
Le classi possono estendere altre classi:

```python
class Animale:
    def parla(self):
        print("Suono generico")

class Cane(Animale):
    def parla(self):
        print("Bau")
```
> In FP useresti composizione di funzioni, qui puoi anche usare ereditarietà e overriding.

## 6. Encapsulation (Incapsulamento)
In OOP puoi nascondere dettagli interni:

```python
class Banca:
    def __init__(self):
        self.__saldo = 0  # "privato"
    
    def deposita(self, importo):
        self.__saldo += importo
```
## Nella FP questo si fa con closure o moduli separati.

## 7. Design orientato agli oggetti
In FP pensi a trasformazioni di dati.

In OOP pensi a:

Chi sono i "protagonisti" del tuo sistema?

Cosa sanno fare?

Come interagiscono?

## Riepilogo rapido

Concetto Funzionale OOP
Struttura | Funzioni + dati | Classi + oggetti
---|---|---
Stato | Immutabile | Mutabile
Modello | Transformazioni | Attori con comportamento
Estensione | Composizione | Ereditarietà e overriding
Incapsulamento | Closure, moduli | self, attributi privati
Principio di progettazione | Funzioni pure, pipe | Responsabilità e collaborazione
