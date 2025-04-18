# FUNZIONI

Una funzione è un blocco di codice che esegue un'azione specifica. In Python, le funzioni sono definite con la parola chiave def, seguita dal nome della funzione e da parentesi tonde. Le funzioni possono accettare parametri e restituire valori.

```python  
# FUNZIONI

# Una funzione che non restituisce alcun valore  
def stampa_messaggio():  
    print("funzione void")  
stampa_messaggio()  # Utilizzo della funzione

# Funzione con un parametro  
def stampa_messaggio_con_parametro(messaggio):  
    print(messaggio)  
stampa_messaggio_con_parametro("funzione void con parametro")

# Funzione con più parametri  
def stampa_messaggio_con_piu_parametri(messaggio1, messaggio2):  
    print(f"{messaggio1} {messaggio2}")  
stampa_messaggio_con_piu_parametri("funzione void con", "più parametri")

# Funzione che restituisce un valore  
def somma(a, b):  
    return a + b  # return indica il valore di ritorno
risultato = somma(2, 3)  
print(risultato)

# Funzione che restituisce una stringa  
def saluta(nome):  
    return f"Ciao {nome}!"  
saluto = saluta("studente")  
print(saluto)

# Funzione che restituisce un booleano  
def parola_pari(parola):  
    return len(parola) % 2 == 0  
risultato_pari = parola_pari("cane")  
print(risultato_pari)

# Funzione che restituisce più valori  
def divisione(dividendo, divisore):  
    quoziente = dividendo // divisore  
    resto = dividendo % divisore  
    return quoziente, resto  
q, r = divisione(10, 3)  
print(f"Quoziente: {q}, Resto: {r}")

# Funzione che restituisce una lista  
def numeri_pari(n):
    lista_pari = []
    for i in range(n):
        lista_pari.append(2 * i)
    return lista_pari
numeri = numeri_pari(5)
print(numeri)

# Funzione che restituisce una lista di stringhe con lunghezza pari  
def parole_pari(parole):  
    # return [parola for parola in parole if len(parola) % 2 == 0]
    parole_pari = []
    for parola in parole:  
        if len(parola) % 2 == 0:  
            parole_pari.append(parola)
    return parole_pari
parole = ["cane", "gatto", "elefante", "topo"]
parole_pari = parole_pari(parole)
print(parole_pari)

# Funzione che restituisce una lista di nomi abbreviati  
def nomi_abbreviati(nomi):  
    # return [f"{nome.split()[0]} {nome.split()[1][0]}." for nome in nomi]  
    nomi_abbreviati = []
    for nome in nomi:  
        nomi_abbreviati.append(f"{nome.split()[0]} {nome.split()[1][0]}.")  # lo split in questo caso serve a separare il nome dal cognome [1][0] serve a prendere solo la prima lettera del cognome
    return nomi_abbreviati
nomi_completi = ["Nome1 Cognome1", "Nome2 Cognome2", "Nome3 Cognome3"]
nomi_abbreviati = nomi_abbreviati(nomi_completi)
print(nomi_abbreviati)

# Funzione che restituisce un dizionario filtrato  
def valori_specifici(dizionario, chiavi):  
    # return {chiave: dizionario[chiave] for chiave in chiavi if chiave in dizionario}  
    dizionario_filtrato = {}
    for chiave in chiavi:  
        if chiave in dizionario:  
            dizionario_filtrato[chiave] = dizionario[chiave]
    return dizionario_filtrato
dizionario = {"a": 1, "b": 2, "c": 3, "d": 4}
chiavi = ["a", "c"]
dizionario_filtrato = valori_specifici(dizionario, chiavi)
print(dizionario_filtrato)

# Funzione che trasmette un valore ad un'altra funzione  
def doppio(n):  
    return n * 2  
def quadruplo(n):  
    return doppio(n) * 2  
print(quadruplo(5))

# Funzione che trasmette un valore a se stessa
def fattoriale(n):  
    if n == 0:  
        return 1  
    else:  
        return n * fattoriale(n - 1)
print(fattoriale(5))  # Output: 120  

# Funzione che viene usata da un 'altra funzione
def somma(a, b):  
    return a + b

def sottrazione(a, b):  
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Non puoi dividere per 0"
    else:
        return a / b
        
def calcola(a, b, operazione):
    if operazione == "somma":
        return somma(a, b)
    elif operazione == "sottrazione":
        return sottrazione(a, b)
    elif operazione == "moltiplicazione":
        return moltiplicazione(a, b)
    elif operazione == "divisione":
        return divisione(a, b)    
    else:
        return "Operazione non valida"
# Esempio di utilizzo
risultato = calcola(10, 5, "somma")
print(risultato)  # Output: 15
```

# Dati mutabili ed immutabili
I dizionari e le altre strutture in Python sono oggetti `mutabili`:
 - Quando passi un dizionario (o una lista) a una funzione, non viene copiato, ma viene passato per riferimento
 - Le modifiche fatte dentro la funzione agiscono sullo stesso oggetto in memoria, cioè sull'inventario originale
 - Quindi non serve return perché il dizionario inventario viene modificato all'interno della funzione stessa
 
> se il dizionario fosse immutabile (come un int, float, str, tuple), allora sarebbe diverso

```python
def incrementa(x):
    x += 1  # crea una nuova variabile x
numero = 5
incrementa(numero)
print(numero)  # Rimane 5, perché x è una copia
```
> in modo da incrementarlo si deve fare
```python
def incrementa(x):
    return x + 1  # restituisce il nuovo valore
numero = 5
numero = incrementa(numero)
print(numero)  # Ora è 6
```

### Differenza tra parametri e argomenti

Spesso vengono confusi, ma sono due cose diverse.

- Parametro -> Il nome usato nella definizione della funzione
- Argomento -> Il valore che passi quando chiami la funzione

```python
def saluta(nome):  # 'nome' è un parametro
    print(f"Ciao, {nome}!")
saluta("Marco")    # "Marco" è un argomento
```


### **Adattamenti per Python**

1. **Nessun void**: In Python, tutte le funzioni restituiscono None per default se non viene specificato un return.  
2. **Passaggio di parametri**: Non esiste il concetto di ref o out. I parametri sono passati per riferimento per oggetti mutabili, e per valore per oggetti immutabili.  
3. **Liste e comprensioni**: Le comprensioni di lista sono state utilizzate per creare array in modo più conciso.  
4. **Multipli valori di ritorno**: In Python puoi restituire più valori come una tupla, senza bisogno di out o ref

# SUGGERIMENTI

- 1. Dai nomi chiari e descrittivi

```python
# giusto
def calcola_sconto(prezzo, percentuale):
# sbagliato
def cs(p, x):
```

- 2. Una funzione = una responsabilità

```python
# giusto
def aggiungi_contatto():
def mostra_contatti():
def cerca_contatto():
# sbagliato
def gestisci_contatti():
```

- 3. Usa return per restituire dati, non print

```python
def somma(a, b):
    return a + b

risultato = somma(5, 3)
print(risultato)  # stampi fuori dalla funzione
```

- 4. Documenta con docstring

```python
def area_rettangolo(base, altezza):
    """Calcola l'area di un rettangolo dato base e altezza."""
    return base * altezza
```

- 5. Parametri con valori predefiniti (default)

```python
def saluta(nome="amico"):
    print(f"Ciao, {nome}!")
```

- 6. Mantieni la funzione breve (max 15-20 righe)

> Se una funzione è troppo lunga, probabilmente fa troppe cose

- 7. Evita che la funzione usi o modifichi variabili definite fuori di essa (evita variabili globali)

```python
def calcola_iva(prezzo, iva=22):
    return prezzo * (iva / 100)
```

- 8. Rendi il codice piu modulare possibile

> se ti accorgi che stai riscrivendo la stessa cosa, crea una funzione