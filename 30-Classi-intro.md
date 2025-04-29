# CLASSI

In Python, una classe è una struttura che consente di creare oggetti che possono contenere dati (proprietà o attributi) e funzionalità (metodi). Le classi rappresentano un concetto fondamentale nella programmazione orientata agli oggetti (OOP) e permettono di modellare entità del mondo reale.

Ecco una descrizione dettagliata di come sono strutturate le classi in Python:

## **1\. Definizione di una classe**

Per definire una classe in Python si utilizza la parola chiave class seguita dal nome della classe. È una convenzione usare la **notazione PascalCase** per i nomi delle classi.

```python  
class NomeClasse:  
    pass  # Corpo della classe (vuoto per ora)  si usa pass in modo da non avere errori di sintassi
```

Esempio:  
```python

class Prodotto:  
    pass  
```

---

## **2\. Costruttore e Metodi**

Il costruttore è un metodo speciale usato per inizializzare gli oggetti della classe. In Python, il costruttore è definito come __init__.

### **Costruttore __init__:**

* Viene automaticamente chiamato quando si crea un'istanza della classe.  
* Riceve i parametri per inizializzare gli attributi dell'oggetto.

### **Metodi:**

* Funzioni definite all'interno della classe per rappresentare il comportamento degli oggetti.  
* Il primo parametro di ogni metodo è self, che rappresenta l'istanza corrente della classe.

Esempio:

```python  
class Prodotto:  
    def __init__(self, nome, prezzo):  
        self.nome = nome  # Attributo di istanza  
        self.prezzo = prezzo

    def mostra_info(self):  
        print(f"Nome: {self.nome}, Prezzo: {self.prezzo}")  
```

---

## **3\. Attributi di Istanza e di Classe**

### **Attributi di istanza:**

* Associati a una specifica istanza di una classe.  
* Definiti con self.

Esempio:

```python  
class Prodotto:  
    def __init__(self, nome, prezzo):  
        self.nome = nome  
        self.prezzo = prezzo  
```

### **Attributi di classe:**

* Condivisi tra tutte le istanze della classe.  
* Definiti all'interno della classe ma fuori dai metodi.

Esempio:

```python  
class Prodotto:  
    sconto_generale = 0.10  # Attributo di classe

    def __init__(self, nome, prezzo):  
        self.nome = nome  
        self.prezzo = prezzo  
```

---

## **4\. Ereditarietà**

In Python, una classe può ereditare attributi e metodi da un'altra classe. La classe derivata è definita includendo la classe base tra parentesi.

Esempio:

```python  
class Prodotto:  
    def __init__(self, nome, prezzo):  
        self.nome = nome  
        self.prezzo = prezzo

class ProdottoAlimentare(Prodotto):  
    def __init__(self, nome, prezzo, data_scadenza):  
        super().__init__(nome, prezzo)  # Chiama il costruttore della classe base  
        self.data_scadenza = data_scadenza  
```

---

## **5\. Encapsulation (Incapsulamento)**

Python consente di definire attributi e metodi con diversi livelli di accessibilità:

* **Pubblici:** Accessibili ovunque.  
* **Privati:** Accessibili solo all'interno della classe (indicati con __ come prefisso).

Esempio:

```python  
class Prodotto:  
    def __init__(self, nome, prezzo):  
        self.nome = nome          # Pubblico  
        self.__prezzo = prezzo    # Privato

    def mostra_prezzo(self):  
        return self.__prezzo  # Accesso al membro privato  
```

---

## **6\. Metodi Speciali**

Python ha diversi metodi speciali (detti "magic methods") che iniziano e finiscono con __.

### **Esempi comuni:**

* __init__: Costruttore.  
* __str__: Rappresentazione in formato stringa dell'oggetto.  
* __repr__: Rappresentazione "ufficiale" per debugging.  
* __eq__, __lt__: Confronto tra oggetti.

Esempio:

```python  
class Prodotto:  
    def __init__(self, nome, prezzo):  
        self.nome = nome  
        self.prezzo = prezzo

    def __str__(self):  
        return f"{self.nome}: {self.prezzo}€"

prodotto = Prodotto("Pane", 2.50)  
print(prodotto)  # Output: Pane: 2.5€  
```

---

## **7\. Proprietà (Properties)**

Le proprietà permettono di definire getter, setter e deleter per un attributo.

Esempio:

```python  
class Prodotto:  
    def __init__(self, nome, prezzo):  
        self.nome = nome  
        self.__prezzo = prezzo

    @property  
    def prezzo(self):  # Getter  
        return self.__prezzo

    @prezzo.setter  
    def prezzo(self, valore):  # Setter  
        if valore <= 0:  
            raise ValueError("Il prezzo deve essere maggiore di zero.")  
        self.__prezzo = valore  
```

---

## **8\. Static e Class Methods**

* **Static Methods (@staticmethod):**  
  * Non dipendono dall'istanza né dalla classe.  
  * Utile per funzionalità generiche.

```python  
class Calcolatrice:  
    @staticmethod  
    def somma(a, b):  
        return a + b  
```

* **Class Methods (@classmethod):**  
  * Operano sulla classe e non sull'istanza.  
  * Ricevono cls come primo parametro.

```python  
class Prodotto:  
    sconto_generale = 0.10

    @classmethod  
    def imposta_sconto(cls, valore):  
        cls.sconto_generale = valore  
```

---

## **9\. Esempio Completo**

```python  
class Prodotto:  
    def __init__(self, nome, prezzo):  
        self.nome = nome  
        self.prezzo = prezzo

    def mostra_info(self):  
        print(f"Nome: {self.nome}, Prezzo: {self.prezzo}€")

class ProdottoAlimentare(Prodotto):  
    def __init__(self, nome, prezzo, data_scadenza):  
        super().__init__(nome, prezzo)  
        self.data_scadenza = data_scadenza

    def mostra_info(self):  
        super().mostra_info()  
        print(f"Data di scadenza: {self.data_scadenza}")

pane = ProdottoAlimentare("Pane", 1.50, "2025-01-30")  
pane.mostra_info()  
```

**Output:**

```bash  
Nome: Pane, Prezzo: 1.5€  
Data di scadenza: 2025-01-30  
```

Con questa base, puoi modellare e gestire facilmente oggetti complessi in Python\!