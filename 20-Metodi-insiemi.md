# METODI DI INSIEMI

Gli **insiemi** in Python (set) sono collezioni non ordinate di elementi unici. Offrono una varietà di metodi per la manipolazione e l'intersezione di dati. Ecco un elenco dettagliato dei metodi disponibili per i set in Python.

### **Metodi principali degli insiemi**

#### **1\. add()**

* **Descrizione**: Aggiunge un elemento all'insieme.  
* **Sintassi**: set.add(elemento)

**Esempio**:  
```python
s = {1, 2, 3}  
s.add(4)  
print(s)  # Output: {1, 2, 3, 4}
```

#### **2\. remove()**

* **Descrizione**: Rimuove un elemento specifico dall'insieme. Solleva un KeyError se l'elemento non è presente.  
* **Sintassi**: set.remove(elemento)

**Esempio**:  
```python
s = {1, 2, 3}  
s.remove(2)  
print(s)  # Output: {1, 3}
```

#### **3\. discard()**

* **Descrizione**: Rimuove un elemento specifico dall'insieme senza sollevare un errore se l'elemento non è presente.  
* **Sintassi**: set.discard(elemento)

**Esempio**:  
```python
s = {1, 2, 3}  
s.discard(4)  # Non solleva un errore  
print(s)  # Output: {1, 2, 3}
```

#### **4\. pop()**

* **Descrizione**: Rimuove e restituisce un elemento arbitrario dall'insieme. Solleva un KeyError se l'insieme è vuoto.  
* **Sintassi**: set.pop()

**Esempio**:  
```python
s = {1, 2, 3}  
elem = s.pop()  
print(elem)  # Output: (un elemento arbitrario, ad esempio 1)  
print(s)     # Output: {2, 3}
```

#### **5\. clear()**

* **Descrizione**: Rimuove tutti gli elementi dall'insieme.  
* **Sintassi**: set.clear()

**Esempio**:  
```python
s = {1, 2, 3}  
s.clear()  
print(s)  # Output: set()
```

### **Metodi per le operazioni insiemistiche**

#### **6\. union()**

* **Descrizione**: Restituisce un nuovo insieme che contiene tutti gli elementi di due o più insiemi.  
* **Sintassi**: set.union(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}
```

#### **7\. intersection()**

* **Descrizione**: Restituisce un nuovo insieme con gli elementi comuni a due o più insiemi.  
* **Sintassi**: set.intersection(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
print(s1.intersection(s2))  # Output: {3}
```

#### **8\. difference()**

* **Descrizione**: Restituisce un nuovo insieme con gli elementi presenti nell'insieme di origine ma non in un altro.  
* **Sintassi**: set.difference(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
print(s1.difference(s2))  # Output: {1, 2}
```

#### **9\. symmetric_difference()**

* **Descrizione**: Restituisce un nuovo insieme con gli elementi presenti in uno dei due insiemi ma non in entrambi.  
* **Sintassi**: set.symmetric_difference(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
print(s1.symmetric_difference(s2))  # Output: {1, 2, 4, 5}
```

### **Metodi per aggiornare gli insiemi**

#### **10\. update()**

* **Descrizione**: Aggiunge tutti gli elementi di un altro insieme all'insieme di origine.  
* **Sintassi**: set.update(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
s1.update(s2)  
print(s1)  # Output: {1, 2, 3, 4, 5}
```

#### **11\. intersection_update()**

* **Descrizione**: Aggiorna l'insieme di origine mantenendo solo gli elementi comuni a entrambi gli insiemi.  
* **Sintassi**: set.intersection_update(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
s1.intersection_update(s2)  
print(s1)  # Output: {3}
```

#### **12\. difference_update()**

* **Descrizione**: Aggiorna l'insieme di origine rimuovendo gli elementi presenti in un altro insieme.  
* **Sintassi**: set.difference_update(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
s1.difference_update(s2)  
print(s1)  # Output: {1, 2}
```

#### **13\. symmetric_difference_update()**

* **Descrizione**: Aggiorna l'insieme di origine con gli elementi presenti in uno dei due insiemi ma non in entrambi.  
* **Sintassi**: set.symmetric_difference_update(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {3, 4, 5}  
s1.symmetric_difference_update(s2)  
print(s1)  # Output: {1, 2, 4, 5}
```

### **Metodi per il confronto degli insiemi**

#### **14\. issubset()**

* **Descrizione**: Restituisce True se tutti gli elementi dell'insieme di origine sono contenuti in un altro insieme.  
* **Sintassi**: set.issubset(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2}  
s2 = {1, 2, 3}  
print(s1.issubset(s2))  # Output: True
```

#### **15\. issuperset()**

* **Descrizione**: Restituisce True se l'insieme di origine contiene tutti gli elementi di un altro insieme.  
* **Sintassi**: set.issuperset(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {1, 2}  
print(s1.issuperset(s2))  # Output: True
```

#### **16\. isdisjoint()**

* **Descrizione**: Restituisce True se gli insiemi non hanno elementi in comune.  
* **Sintassi**: set.isdisjoint(altro_insieme)

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = {4, 5, 6}  
print(s1.isdisjoint(s2))  # Output: True
```

### **Altri metodi utili**

#### **17\. copy()**

* **Descrizione**: Restituisce una copia dell'insieme.  
* **Sintassi**: set.copy()

**Esempio**:  
```python
s1 = {1, 2, 3}  
s2 = s1.copy()  
print(s2)  # Output: {1, 2, 3}
```

Questi metodi offrono una vasta gamma di funzionalità per gestire e manipolare gli insiemi in Python in modo efficiente\!