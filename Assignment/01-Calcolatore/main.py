# versione con try except in ogni funzione
def somma(a, b):
    try:
        return a + b
    except TypeError:
        return "Errore: i valori devono essere numeri"
    
def sottrazione(a, b):
    try:
        return a - b
    except TypeError:
        return "Errore: i valori devono essere numeri"
    
def moltiplicazione(a, b):
    try:
        return a * b
    except TypeError:
        return "Errore: i valori devono essere numeri"
    
def divisione(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return (f"Errore: divisione per zero: {e}")

def calcolatore():
    while True:
        try:
            primo_numero = float(input("Inserisci il primo numero: "))
            secondo_numero = float(input("Inserisci il secondo numero: "))
            operazione = input("Inserisci l'operazione da eseguire (+, -, *, /): ")

            if operazione == "+":
                print(somma(primo_numero, secondo_numero))
            elif operazione == "-":
                print(sottrazione(primo_numero, secondo_numero))
            elif operazione == "*":
                print(moltiplicazione(primo_numero, secondo_numero))
            elif operazione == "/":
                print(divisione(primo_numero, secondo_numero))
            else:
                print("Operazione non valida")
        except ValueError:
            print("Errore: inserisci un numero valido")

        continua = input("Vuoi continuare? (s/n): ")
        if continua.lower() != "s":
            break
# Chiamo la funzione calcolatore
calcolatore()