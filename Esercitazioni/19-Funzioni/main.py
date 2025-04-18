# FUNZIONI

# Una funzione è un blocco di codice che esegue un'azione specifica
# generalmente si usano le funzioni quando:
# Si vuole tenere circoscritto il codice in modo da rendere lo script piu leggibile e manutenibile
# Si vogliono evitare ripetizioni di codice
# Una funzione deve necessariamente risolvere un task specifico
# Una funzione deve necessariamente avere un nome descrittivo

# Una funzione che non restituisce alcun valore
def stampa_messaggio():
    print("funzione void")
stampa_messaggio()  # Utilizzo della funzione

# Funzione con un parametro
def stampa_messaggio_con_parametro(messaggio):  # messaggio è un parametro
    print(messaggio)
stampa_messaggio_con_parametro("funzione void con parametro")  # "funzione void con parametro" è un argomento

# Funzione con più parametri
def stampa_messaggio_con_piu_parametri(messaggio1, messaggio2):
    print(f"{messaggio1} {messaggio2}")
stampa_messaggio_con_piu_parametri("funzione void con", "più parametri")

# Funzione che restituisce un valore
def somma(a, b):
    return a + b  # return indica il valore di ritorno
risultato = somma(5, 10)  # 5 e 10 sono gli argomenti
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
print(risultato_pari)  # True

# Funzione che restituisce più valori
def divisione(dividendo, divisore):
    quoziente = dividendo // divisore
    resto = dividendo % divisore
    return quoziente, resto  # Restituisce una tupla con i valori
q, r = divisione(10, 3)
print(f"Quoziente: {q}, Resto: {r}")

# Funzione che restituisce una lista
# in questo caso stampa i primi n numeri pari
def numeri_pari(n):
    lista_pari = []
    for i in range(n):
        lista_pari.append(2 * i)
    return lista_pari
numeri = numeri_pari(5)
print(numeri)

# Funzione che restituisce una lista di stringhe con lunghezza pari
def parole_pari(parole):
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
    nomi_abbreviati = []
    for nome in nomi:
        nomi_abbreviati.append(f"{nome.split()[0]} {nome.split()[1][0]}.")  # lo split in questo caso serve a separare il nome dal cognome [1][0]
        # con [0] si  prende solo la prima lettera cognome
        # con [2] si prende la terza lettera del cognome
        # con [0:2] si prende il primo ed il secondo carattere del cognome
        # con [0::2] si prende ogni intervallo di 2 caratteri del cognome a partire dal primo
        # con [2::] si prende quello che c e dopo la posizione 2 del cognome
    return nomi_abbreviati
nomi_completi = ["Nome1 Cognome1", "Nome2 Cognome2", "Nome3 Cognome3"]
nomi_abbreviati = nomi_abbreviati(nomi_completi)  # creo una lista di nomi abbreviati con la funzione che ho creato
print(nomi_abbreviati)

# Funzione che restituisce un dizionario filtrato
def valori_specifici(dizionario, chiavi):  
    dizionario_filtrato = {}
    for chiave in chiavi:
        if chiave in dizionario:
            dizionario_filtrato[chiave] = dizionario[chiave]
    return dizionario_filtrato
dizionario = {"a": 1, "b": 2, "c": 3, "d": 4}
chiavi = ["a", "c"]
dizionario_filtrato = valori_specifici(dizionario, chiavi)  # creo un dizionario filtrato con le chiavi specificate
print(dizionario_filtrato)  # {'a': 1, 'c': 3}

# Funzione che trasmette un valore ad un'altra funzione  
def doppio(n):  
    return n * 2  
def quadruplo(n):  
    return doppio(n) * 2  
print(quadruplo(5))  # 20

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
print(risultato)  # 15

# Funzione con parametro inizializzato con valore di default
def saluta(nome="studente"):  # nome ha un valore di default
    return f"Ciao {nome}!"
saluto = saluta()  # non passo alcun argomento, quindi viene usato il valore di default
print(saluto)  # Ciao studente

# Funzione con parametro inizializzato con valore di default
def calcola(a, b, operazione="somma"):  # operazione ha un valore di default
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
risultato = calcola(10, 5)  # non passo l argomento operazione, quindi uso il valore di default
print(risultato)  # 15