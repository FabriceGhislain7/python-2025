# Comprensioni
Le comprensioni in Python permettono di scrivere codice più compatto, leggibile e performante per creare liste, dizionari o insiemi.

## Cosa sono le comprensioni?
Sono una forma compatta per creare strutture dati come:

- liste (list comprehension)
- dizionari (dict comprehension)
-set (set comprehension)

> Si usano quando vuoi trasformare o filtrare elementi in un ciclo

## Sintassi:
```python
[espressione for elemento in iterabile if condizione]
```
## 1. List Comprehension
Esempio 1: lista di quadrati
```python
quadrati = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
```
Esempio 2: solo numeri pari
```python
pari = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```
Esempio 3: trasformare stringhe
```python
nomi = ["alice", "BOB", "ClAra"]
puliti = [n.lower() for n in nomi]
# ['alice', 'bob', 'clara']
```
## 2. Dict Comprehension
Utile per creare o trasformare dizionari in una sola riga.

```python
nomi = ["alice", "bob", "carla"]
lunghezze = {nome: len(nome) for nome in nomi}
# {'alice': 5, 'bob': 3, 'carla': 5}
```
## 3. Set Comprehension
Come la list comprehension, ma con {} e senza duplicati.

```python
caratteri = {c for c in "banana"}
# {'b', 'a', 'n'}
```
## 4. Con if...else dentro
```python
numeri = [1, 2, 3, 4, 5]
parita = ["pari" if x % 2 == 0 else "dispari" for x in numeri]
# ['dispari', 'pari', 'dispari', 'pari', 'dispari']
```
## Vantaggi delle comprensioni

Vantaggio | Spiegazione
---|---
Più leggibile | Una riga invece di 4-5 righe di for + append()
Più performante | In genere più veloce dei cicli standard
Ideale per trasformazioni | Perfetto per filtrare o mappare elementi
Combinabile facilmente | Puoi annidare o creare strutture complesse in modo chiaro
