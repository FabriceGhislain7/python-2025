# METODI DIZIONARIO

I **dizionari** in Python sono strutture dati che memorizzano coppie chiave-valore, dove le chiavi sono uniche e immutabili. Python fornisce diversi metodi per manipolare i dizionari in modo efficace.

---

### **Metodi principali dei dizionari**

#### **1\. clear()**

* **Descrizione**: Rimuove tutti gli elementi dal dizionario.  
* **Sintassi**: dizionario.clear()

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
d.clear()  
print(d)  # Output: {}
```

#### **2\. copy()**

* **Descrizione**: Restituisce una copia superficiale del dizionario.  
* **Sintassi**: dizionario.copy()

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
d_copy = d.copy()  
print(d_copy)  # Output: {'a': 1, 'b': 2}
```

#### **3\. fromkeys()**

* **Descrizione**: Crea un nuovo dizionario con le chiavi specificate e un valore predefinito.  
* **Sintassi**: dict.fromkeys(iterabile, valore)

**Esempio**:  
```python  
keys = ["a", "b", "c"]  
d = dict.fromkeys(keys, 0)  
print(d)  # Output: {'a': 0, 'b': 0, 'c': 0}
```

#### **4\. get()**

* **Descrizione**: Restituisce il valore associato a una chiave. Se la chiave non esiste, restituisce un valore predefinito (di default None).  
* **Sintassi**: dizionario.get(chiave, valore_default)

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
print(d.get("a"))        # Output: 1  
print(d.get("c", "N/A")) # Output: N/A
```

#### **5\. items()**

* **Descrizione**: Restituisce una vista (view) degli elementi del dizionario come tuple (chiave, valore).  
* **Sintassi**: dizionario.items()

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
print(list(d.items()))  # Output: [('a', 1), ('b', 2)]
```

#### **6\. keys()**

* **Descrizione**: Restituisce una vista delle chiavi del dizionario.  
* **Sintassi**: dizionario.keys()

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
print(list(d.keys()))  # Output: ['a', 'b']
```

#### **7\. values()**

* **Descrizione**: Restituisce una vista dei valori del dizionario.  
* **Sintassi**: dizionario.values()

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
print(list(d.values()))  # Output: [1, 2]
```

#### **8\. pop()**

* **Descrizione**: Rimuove una chiave e restituisce il valore associato. Genera un errore se la chiave non esiste, a meno che non venga fornito un valore di default.  
* **Sintassi**: dizionario.pop(chiave, valore_default)

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
valore = d.pop("a")  
print(valore)  # Output: 1  
print(d)       # Output: {'b': 2}
```

#### **9\. popitem()**

* **Descrizione**: Rimuove e restituisce l'ultima coppia chiave-valore inserita. Solleva un errore se il dizionario è vuoto.  
* **Sintassi**: dizionario.popitem()

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
elemento = d.popitem()  
print(elemento)  # Output: ('b', 2)  
print(d)         # Output: {'a': 1}
```

#### **10\. setdefault()**

* **Descrizione**: Restituisce il valore di una chiave. Se la chiave non esiste, la aggiunge al dizionario con un valore predefinito.  
* **Sintassi**: dizionario.setdefault(chiave, valore_default)

**Esempio**:  
```python  
d = {"a": 1}  
valore = d.setdefault("b", 2)  
print(valore)  # Output: 2  
print(d)       # Output: {'a': 1, 'b': 2}
```

#### **11\. update()**

* **Descrizione**: Aggiorna il dizionario con coppie chiave-valore da un altro dizionario o da un iterabile.  
* **Sintassi**: dizionario.update(altri_dati)

**Esempio**:  
```python  
d = {"a": 1, "b": 2}  
d.update({"c": 3, "d": 4})  
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### **Esempi pratici**

#### **Creazione e modifica:**

```python  
d = {"nome": "Mario", "età": 30}  
d["città"] = "Roma"  # Aggiunge una nuova coppia chiave-valore  
d["età"] = 31       # Modifica il valore di una chiave esistente  
print(d)  # Output: {'nome': 'Mario', 'età': 31, 'città': 'Roma'}
```

#### **Iterazione su chiavi, valori e coppie:**

```python  
d = {"a": 1, "b": 2, "c": 3}  
for chiave in d.keys():  
    print(chiave)  # Output: a b c

for valore in d.values():  
    print(valore)  # Output: 1 2 3

for chiave, valore in d.items():  
    print(f"{chiave}: {valore}")  # Output: a: 1 b: 2 c: 3
```

#### **Unione di dizionari:**

```python  
d1 = {"a": 1, "b": 2}  
d2 = {"c": 3, "d": 4}  
d1.update(d2)  
print(d1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

#### **Accesso sicuro alle chiavi:**

```python  
d = {"a": 1, "b": 2}  
print(d.get("c", "Chiave non trovata"))  # Output: Chiave non trovata
```

I **dizionari** sono strumenti fondamentali in Python per rappresentare dati strutturati e le loro operazioni coprono numerosi scenari utili per l'elaborazione dei dati.