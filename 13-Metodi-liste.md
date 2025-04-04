# METODI LISTE

Le **liste** in Python sono una struttura dati mutabile che consente di memorizzare una sequenza di elementi. Sono una delle collezioni più versatili e utilizzate. Python offre numerosi metodi per manipolare le liste.

---

### **Metodi principali delle liste**

#### **1\. append()**

* **Descrizione**: Aggiunge un elemento alla fine della lista.  
* **Sintassi**: lista.append(elemento)

**Esempio**:  
```python  
lista = [1, 2, 3]

lista.append(4)

print(lista)  # Output: [1, 2, 3, 4]

```

#### **2\. extend()**

* **Descrizione**: Aggiunge tutti gli elementi di un'altra lista (o di un iterabile) alla fine della lista corrente.  
* **Sintassi**: lista.extend(iterabile)

**Esempio**:  
```python  
lista = [1, 2, 3]

lista.extend([4, 5, 6])

print(lista)  # Output: [1, 2, 3, 4, 5, 6]

```

#### **3\. insert()**

* **Descrizione**: Inserisce un elemento in una posizione specifica della lista.  
* **Sintassi**: lista.insert(indice, elemento)

**Esempio**:  
```python  
lista = [1, 2, 4]

lista.insert(2, 3)  # Inserisce 3 alla posizione 2

print(lista)  # Output: [1, 2, 3, 4]

```

#### **4\. remove()**

* **Descrizione**: Rimuove la prima occorrenza di un elemento dalla lista.  
* **Sintassi**: lista.remove(elemento)

**Esempio**:  
```python  
lista = [1, 2, 3, 2]

lista.remove(2)

print(lista)  # Output: [1, 3, 2]

```

#### **5\. pop()**

* **Descrizione**: Rimuove e restituisce l'elemento alla posizione specificata. Se l'indice non è fornito, rimuove e restituisce l'ultimo elemento.  
* **Sintassi**: lista.pop([indice])

**Esempio**:  
```python  
lista = [1, 2, 3]

elemento = lista.pop(1)

print(elemento)  # Output: 2

print(lista)     # Output: [1, 3]

```

#### **6\. clear()**

* **Descrizione**: Rimuove tutti gli elementi dalla lista.  
* **Sintassi**: lista.clear()

**Esempio**:  
```python  
lista = [1, 2, 3]

lista.clear()

print(lista)  # Output: []

```

---

### **Metodi di ricerca**

#### **7\. index()**

* **Descrizione**: Restituisce l'indice della prima occorrenza di un elemento. Solleva un ValueError se l'elemento non è presente.  
* **Sintassi**: lista.index(elemento[, start[, end]])

**Esempio**:  
```python  
lista = [1, 2, 3, 2]

print(lista.index(2))  # Output: 1

```

#### **8\. count()**

* **Descrizione**: Restituisce il numero di volte che un elemento appare nella lista.  
* **Sintassi**: lista.count(elemento)

**Esempio**:  
```python  
lista = [1, 2, 3, 2]

print(lista.count(2))  # Output: 2

```

---

### **Metodi per ordinare e modificare**

#### **9\. sort()**

* **Descrizione**: Ordina la lista in ordine crescente (o decrescente se specificato). Modifica la lista originale.  
* **Sintassi**: lista.sort(key=None, reverse=False)

**Esempio**:  
```python  
lista = [3, 1, 4, 2]

lista.sort()

print(lista)  # Output: [1, 2, 3, 4]

```

#### **10\. sorted()**

* **Descrizione**: Restituisce una nuova lista ordinata senza modificare l'originale.  
* **Sintassi**: sorted(lista, key=None, reverse=False)

**Esempio**:  
```python  
lista = [3, 1, 4, 2]

nuova_lista = sorted(lista)

print(nuova_lista)  # Output: [1, 2, 3, 4]

print(lista)        # Output: [3, 1, 4, 2]

```

#### **11\. reverse()**

* **Descrizione**: Inverte l'ordine degli elementi nella lista. Modifica la lista originale.  
* **Sintassi**: lista.reverse()

**Esempio**:  
```python  
lista = [1, 2, 3]

lista.reverse()

print(lista)  # Output: [3, 2, 1]

```

### **Metodi di copia**

#### **12\. copy()**

* **Descrizione**: Restituisce una copia superficiale della lista.  
* **Sintassi**: lista.copy()

**Esempio**:  
```python  
lista = [1, 2, 3]

copia = lista.copy()

print(copia)  # Output: [1, 2, 3]

```

---

### **Operazioni utili**

#### **13\. len()**

* **Descrizione**: Restituisce il numero di elementi nella lista.  
* **Sintassi**: len(lista)

**Esempio**:  
```python  
lista = [1, 2, 3]

print(len(lista))  # Output: 3

```

#### **14\. in e not in**

* **Descrizione**: Verifica se un elemento è presente o meno nella lista.  
* **Sintassi**:  
  * elemento in lista  
  * elemento not in lista

**Esempio**:  
```python  
lista = [1, 2, 3]

print(2 in lista)  # Output: True

print(4 not in lista)  # Output: True

```

---

### **Esempi combinati**

#### **Aggiunta e ordinamento:**

```python

numeri = [5, 2, 9, 1]

numeri.append(6)

numeri.sort()

print(numeri)  # Output: [1, 2, 5, 6, 9]

```

#### **Rimozione e conteggio:**

```python

frutta = ["mela", "banana", "arancia", "mela"]

frutta.remove("mela")

print(frutta.count("mela"))  # Output: 1

```

Le **liste** in Python sono potenti e flessibili, e i metodi sopra elencati coprono una vasta gamma di operazioni, rendendole adatte per quasi tutte le situazioni.