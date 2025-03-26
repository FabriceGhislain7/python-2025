# RANDOM
Python offre un modulo per la generazione di numeri casuali, chiamato random.
```python
import random
```
Per generare un numero casuale tra 1 e 100 si può usare il metodo randint:
```python
random.randint(1, 100)
```
Per scegliere una stringa casuale tra quelle fornite si può usare il metodo choice:
```python
random.choice(["ciao", "hello", "hola"])
```
Per mescolare una lista si può usare il metodo shuffle:
```python
random.shuffle([1, 2, 3, 4, 5])
```
Per scegliere n elementi casuali da una lista si può usare il metodo sample:
```python
random.sample([1, 2, 3, 4, 5], 3)
```

### Il seed è un valore che inizializza il generatore di numeri casuali.

Ad esempio, se si fissa il seed a 42, la sequenza di numeri casuali generata sarà sempre la stessa.

Per fissare il seed si può usare il metodo seed:

```python
random.seed(42)
```

### Esempio di utilizzo del modulo random

```python
import time  # importa il modulo time
import random # importa il modulo random
# fisso il numero random tra 3 ed 8
time.sleep(random.randint(3, 8))
print("Ciao!")
```