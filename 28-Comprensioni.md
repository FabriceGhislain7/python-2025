# Comprensioni
Le comprensioni in Python permettono di scrivere codice più compatto, leggibile e performante per creare liste, dizionari o insiemi.

## Cosa sono le comprensioni?
Sono una forma compatta per creare strutture dati come:

- liste (list comprehension)
- dizionari (dict comprehension)
-set (set comprehension)

> Si usano quando vuoi trasformare o filtrare elementi in un ciclo

# 1. List Comprehension
Sintassi:
```python
[espressione for elemento in iterabile if condizione]
```
## Esempi base
Esempio 1: lista di quadrati
```python
quadrati = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
```
✅ Esempio 2: solo numeri pari
python
Copia
Modifica
pari = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
✅ Esempio 3: trasformare stringhe
python
Copia
Modifica
nomi = ["alice", "BOB", "ClAra"]
puliti = [n.lower() for n in nomi]
# ['alice', 'bob', 'clara']
🔹 2. Dict Comprehension
Utile per creare o trasformare dizionari in una sola riga.

python
Copia
Modifica
nomi = ["alice", "bob", "carla"]
lunghezze = {nome: len(nome) for nome in nomi}
# {'alice': 5, 'bob': 3, 'carla': 5}
🔹 3. Set Comprehension
Come la list comprehension, ma con {} e senza duplicati.

python
Copia
Modifica
caratteri = {c for c in "banana"}
# {'b', 'a', 'n'}
🔹 4. Con if...else dentro
python
Copia
Modifica
numeri = [1, 2, 3, 4, 5]
parita = ["pari" if x % 2 == 0 else "dispari" for x in numeri]
# ['dispari', 'pari', 'dispari', 'pari', 'dispari']
🎯 Vantaggi delle comprensioni

Vantaggio	Spiegazione
✅ Più leggibile	Una riga invece di 4-5 righe di for + append()
⚡ Più performante	In genere più veloce dei cicli standard
🎯 Ideale per trasformazioni	Perfetto per filtrare o mappare elementi
📦 Combinabile facilmente	Puoi annidare o creare strutture complesse in modo chiaro
🛑 Quando non usarle
Se la logica è troppo complessa: meglio usare un ciclo for classico per chiarezza.

Se hai bisogno di debug passo-passo o commenti dentro.

🤯 Bonus: Comprehension annidate
python
Copia
Modifica
matrice = [[i * j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
