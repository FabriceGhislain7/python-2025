# FONDAMENTI DI PROGRAMMAZIONE

## **Fondamenti della programmazione in Python**

### **Obiettivo: Familiarizzare con i concetti di base della programmazione utilizzando Python, adattandoli alle sue peculiarità.**

---

### **Concetti di base**

#### **Tipi di dati**

In Python, i tipi di dati si dividono in:

**Tipi semplici**:

**Numeri interi**: int

**Numeri reali**: float

**Stringhe**: str

**Booleani**: bool

**Nessun valore**: NoneType

Esempi:  
```python  
numero_intero = 10  
numero_reale = 3.14  
stringa = "Ciao"  
booleano = True  
nulla = None  
```

**Strutture dati**:

**Liste** (list): Raccolta ordinata e modificabile.

**Tuple** (tuple): Raccolta ordinata e immutabile.

**Dizionari** (dict): Coppie chiave-valore.

**Insiemi** (set): Raccolta non ordinata di elementi unici.

Esempi:  
```python  
lista = [1, 2, 3, 4]  
tupla = (1, 2, 3, 4)  
dizionario = {"chiave": "valore", "età": 30}  
insieme = {1, 2, 3, 3}  # Elementi duplicati non vengono inclusi  
```

#### **Array (con libreria array)**

Gli array in Python sono simili alle liste, ma utilizzano meno memoria e possono contenere solo elementi di un unico tipo:

```python  
import array  
numeri = array.array('i', [1, 2, 3, 4])  # 'i' indica numeri interi  
# gli altri tipi di dati sono 'f' per i float e 'd' per i double  
```

---

### **Variabili e costanti**

In Python:

* **Variabili**: Sono dichiarate assegnando un valore. Non hanno bisogno di specificare un tipo.  
* **Costanti**: Python non ha un meccanismo nativo per le costanti, ma si utilizzano convenzioni (nomi in maiuscolo).

Esempi:

```python  
variabile = 10  # Variabile  
COSTANTE = 3.14  # Convenzione per le costanti  
```

---

### **Operatori**

#### **Aritmetici**

```python  
a, b = 10, 3  
somma = a + b  # 13  
differenza = a - b  # 7  
prodotto = a * b  # 30  
quoziente = a / b  # 3.333...  
modulo = a % b  # 1  
esponenziale = a ** b  # 1000  
```

#### **Confronto**

```python  
a, b = 10, 20  
print(a == b)  # False  
print(a != b)  # True  
print(a > b)  # False  
```

#### **Logici**

```python  
print(True and False)  # False  
print(True or False)  # True  
print(not True)  # False  
```

#### **Assegnazione**

```python  
a = 10  
a += 5  # 15  
a *= 2  # 30  
```

---

### **Condizioni**

#### **if**

```python  
numero = 10  
if numero == 10:  
    print("Il numero è 10")  
```

#### **if-else**

```python  
if numero > 10:  
    print("Maggiore di 10")  
else:  
    print("Minore o uguale a 10")  
```

#### **if-elif-else**

```python  
if numero > 10:  
    print("Maggiore di 10")  
elif numero == 10:  
    print("È 10")  
else:  
    print("Minore di 10")  
```

#### **Switch (simulato con un dizionario)**

Python non ha un'istruzione switch nativa, ma si può usare un dizionario:

```python  
opzioni = {  
    1: "Opzione 1",  
    2: "Opzione 2"  
}  
numero = 2  
print(opzioni.get(numero, "Default"))  
```

---

### **Cicli**

#### **while**

```python  
n = 5  
while n > 0:  
    print(n)  
    n -= 1  
```

#### **for**

```python  
for i in range(5):  # Da 0 a 4  
    print(i)  
```

#### **foreach (applicato con for)**

```python  
lista = ["a", "b", "c"]  
for elemento in lista:  
    print(elemento)  
```

---

### **Funzioni**

#### **Senza parametri**

```python  
def saluta():  
    print("Ciao mondo!")  
saluta()  
```

#### **Con parametri**

```python  
def saluta(nome):  
    print(f"Ciao, {nome}!")  
saluta("Alice")  
```

#### **Con valore di ritorno**

```python  
def somma(a, b):  
    return a + b  
risultato = somma(10, 5)  
print(risultato)  # 15  
```

#### **Funzioni anonime (lambda)**

Una funzione anonima è una funzione senza nome definita con una sintassi più compatta, il vantaggio è la brevità:
```python  
somma = lambda a, b: a + b  
print(somma(2, 3))  # 5  
```

---

### **Best practices per Python**

**Formattazione**: Segui PEP 8 (usa strumenti come black o flake8).

**Commenti**: Usa docstring per documentare funzioni e classi.  
```python  
def somma(a, b):  
    """Calcola la somma di due numeri."""  
    return a + b  
```

**Gestione delle eccezioni**:  
```python  
try:  
    numero = int(input("Inserisci un numero: "))  
except ValueError:  
    print("Errore: Inserisci un numero valido.")  
```