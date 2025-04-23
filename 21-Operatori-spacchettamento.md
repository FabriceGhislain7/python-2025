# OPERATORI DI SPACCHETTAMENTO

Gli operatori di spacchettamento in Python sono
- `*` (asterisco singolo)
- `**` (asterisco doppio), e servono per "spacchettare" o "espandere" contenitori come liste, tuple e dizionari.

## * (per liste e tuple)

Serve per spacchettare sequenze come liste o tuple.

```python
numeri = [1, 2, 3]
print(*numeri)
```

Output:

- 1 2 3

*numeri prende gli elementi della lista e li passa uno per uno alla funzione print.

## ** (per dizionari)

Serve per spacchettare dizionari, cioè coppie chiave-valore.

```python
dati = {"nome": "Nome", "eta": 30}
print(*dati)  # Stampa la chiave
print(*dati.values())  # Stampa i valori
```

```python
dati = {"nome": "Nome", "eta": 30}
def saluta(nome, età):
    print(f"Ciao {nome}, hai {età} anni!")

saluta(**dati)
```

Output:

- Ciao Nome, hai 30 anni!

Simbolo | Cosa fa | Dove si usa
--------|---------|----------------
`*` |  Spacchetta liste o tuple | In chiamate o definizioni
`**` | Spacchetta dizionari | In chiamate o definizioni

## Spacchettamento in assegnazione

Puoi usare * per "catturare" più valori in una lista durante l’assegnazione.

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```
Qui:

- a prende il primo valore
- c prende l’ultimo
- *b prende tutto quello in mezzo

## Unire liste o tuple con *

Puoi combinare più liste in una nuova usando *.

```python
lista1 = [1, 2]
lista2 = [3, 4]
unita = [*lista1, *lista2]
print(unita)  # [1, 2, 3, 4]
```

Niente cicli: lo spacchettamento le unisce in modo semplice!

## Unire dizionari con **

Con ** puoi unire dizionari. Se ci sono chiavi duplicate, vince l’ultimo cioe quello che viene dopo.

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {**d1, **d2}
print(d3)  # {'a': 1, 'b': 3, 'c': 4}
```
La chiave "b" viene sovrascritta con il valore di d2

# Creare nuove liste o tuple miste

Puoi mischiare valori normali e spacchettati:

```python
valori = [2, 3, 4]
nuova = [1, *valori, 5]
print(nuova)  # [1, 2, 3, 4, 5]
```

# Convertire stringhe o range in liste
```python
print([*'ciao'])        # ['c', 'i', 'a', 'o']
print([*range(3, 6)])   # [3, 4, 5]
```

Uso | Operatore | Risultato
-----|-----------|----------------
Spacchettamento in assegnazione | `*` | Raccoglie più valori in una lista
Unione di liste/tuple | `*` | Aggiunge elementi singoli
Unione di dizionari | `**` | Aggiunge coppie chiave-valore
Misto | `*, **` | Valori fissi + variabili