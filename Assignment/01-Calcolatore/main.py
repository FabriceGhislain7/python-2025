# Definizione delle funzioni per gestire le operazioni
def somma(a, b):
    return a + b
def sottrazione(a, b):
    return a - b
def moltiplicazione(a, b):
    return a * b
def divisione(a, b):
    try:
        resultato = a/b
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Error: {e}")
    return resultato

def calcolatrice():

    while True:
        numero1 = float(input("inserisci il primo numero: "))
        numero2 = float(input("inserisci il secondo numero: "))
        scelta_operazione = input("Inserisci il segno per l'operazione desiderata: +, -, *, / : ")
        operazioni = ["+", "-", "/", "*"]

        while not scelta_operazione in operazioni:
            scelta_operazione = input("Inserisci di nuovo il segno per l'operazione desiderata: +, -, *, / : ")
        while numero2 == 0 and scelta_operazione == "/":
            numero2 = float(input("il secondo valore deve essere diverso da zero. inserisci di nuovo il secondo numero: "))

        if scelta_operazione == "+":
            print(somma(numero1, numero2))
        elif scelta_operazione == "-":
            print(sottrazione(numero1, numero2))
        elif scelta_operazione ==  "*":
            print(moltiplicazione(numero1, numero2))
        else:
            print(divisione(numero1, numero2))

        continua = input("Vuoi continuare? (si/no): ")
        if continua != "si":
            break

print(calcolatrice())



