# Una funzione è un blocco di codice che esegue un'azione specifica.  

# Una funzione che non restituisce alcun valore
def stampa_messaggio():
    print("funzione void")
stampa_messaggio()

# la funzione con un parametro.
print("-" * 40)
def stampa_messaggio_con_argomento(messaggio):
    print(messaggio)
message = "Buongionom come va?"
stampa_messaggio_con_argomento(message)

# Funzione con più parametri
print("-" * 40)
def stampa_piu_parametri(messaggio1, messaggio2):
    print(f"{messaggio1}{messaggio2}")
stampa_piu_parametri("Buongiorno", "Antonio")

# Funzione che restituisce un valore
print("-" * 40)
def somma(a, b):
    return a + b
risultato = somma(5, 10)
print(risultato)

# Funzione che restituisce una striga
print("-" * 40)
def saluta(nome):
    return f"Ciao {nome}"
saluto = saluta("studente")
print(saluto)

# Funzione che restituisce un booleano
print("-" * 40)
def parola_pari(parola):
    return len(parola) % 2 == 0 
risultato_pari = parola_pari("Cane")
print(risultato_pari)

# Funzione che restituisce più valori
print("-" * 40)
def divisione(dividendo, divisore):
    quotiente = dividendo // divisore
    resto = dividendo % divisore
    return quotiente, resto
q, r = divisione(10, 3)
print(f"Quotiente: {q}, resto:{r}")

# Funzioni che restituisce una lista 
print("-" * 40)
def numeri_pari(n):
    lista_pari = []
    for i in range(n):
        lista_pari.append(2 * i)
    return lista_pari
numeri = numeri_pari(5)
print(numeri)
