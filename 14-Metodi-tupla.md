# METODI TUPLE

Le tuple in Python sono strutture di dati immutabili che possono contenere una sequenza ordinata di elementi. Nonostante la loro semplicità, le tuple dispongono di diversi metodi utili e proprietà integrate.

### **Metodi delle tuple**

1. **count()**  
   * **Descrizione**: Restituisce il numero di volte che un elemento specifico appare nella tupla.  
   * **Sintassi**: tupla.count(elemento)

**Esempio**:  
```python
tupla = (1, 2, 3, 1, 4, 1)  
print(tupla.count(1))  # Output: 3  
print(tupla.count(5))  # Output: 0
```

2. **index()**  
   * **Descrizione**: Restituisce l'indice della prima occorrenza di un elemento specifico nella tupla. Solleva un'eccezione (ValueError) se l'elemento non è presente.  
   * **Sintassi**: tupla.index(elemento[, start[, stop]])  
     * start e stop sono opzionali e limitano la ricerca a un intervallo specifico.

**Esempio**:  
```python
tupla = (1, 2, 3, 1, 4)  
print(tupla.index(1))       # Output: 0  
print(tupla.index(1, 1))    # Output: 3  
# print(tupla.index(5))     # Solleverà un ValueError
```

### **Operazioni utili con le tuple**

Le tuple non hanno molti metodi perché sono **immutabili**, ma ci sono operazioni integrate che puoi utilizzare:

1. **Accesso agli elementi**:

Usa gli indici per accedere agli elementi della tupla:  
```python
tupla = (1, 2, 3, 4)  
print(tupla[0])  # Output: 1  
print(tupla[-1]) # Output: 4
```

2. **Unpacking**:

Puoi "spacchettare" i valori di una tupla in variabili separate:  
```python
tupla = (1, 2, 3)  
a, b, c = tupla  
print(a, b, c)  # Output: 1 2 3
```

3. **Concatenazione**:

Puoi concatenare tuple usando +:  
```python
tupla1 = (1, 2)  
tupla2 = (3, 4)  
nuova_tupla = tupla1 + tupla2  
print(nuova_tupla)  # Output: (1, 2, 3, 4)
```

4. **Ripetizione**:

Usa * per ripetere una tupla:  
```python
tupla = (1, 2)  
print(tupla * 3)  # Output: (1, 2, 1, 2, 1, 2)
```

5. **Verifica di appartenenza**:

Usa l'operatore in per controllare se un elemento è nella tupla:  
```python
tupla = (1, 2, 3)  
print(2 in tupla)  # Output: True  
print(5 in tupla)  # Output: False
```

6. **Lunghezza della tupla**:

Usa len() per calcolare la lunghezza della tupla:  
```python
tupla = (1, 2, 3)  
print(len(tupla))  # Output: 3
```

7. **Iterazione**:

Puoi iterare attraverso una tupla usando un ciclo for:  
```python
tupla = (1, 2, 3)  
for elemento in tupla:  
    print(elemento)
```

8. **Conversione ad altri tipi**:

Converte una lista in una tupla:  
```python
lista = [1, 2, 3]  
tupla = tuple(lista)  
print(tupla)  # Output: (1, 2, 3)
```

Converte una tupla in una lista:  
```python
tupla = (1, 2, 3)  
lista = list(tupla)  
print(lista)  # Output: [1, 2, 3]
```

### **Proprietà delle tuple**

**Immutabilità**: Una volta creata, una tupla non può essere modificata. Gli elementi non possono essere aggiunti, rimossi o sostituiti.  
```python
tupla = (1, 2, 3)  
# tupla[0] = 10  # Solleverà un TypeError
```

**Eterogeneità**: Puoi memorizzare tipi di dati diversi in una tupla.  
```python
tupla = (1, "Python", True, 3.14)  
print(tupla)  # Output: (1, 'Python', True, 3.14)
```

Seguire queste linee guida ti permetterà di sfruttare al meglio le tuple in Python\!