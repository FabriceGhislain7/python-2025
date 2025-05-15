# Definizione delle funzioni per gestire le operazioni
def somma(a, b):
    try: 
        return a + b
    except ValueError as e:
        print(f"Errore: {e}")

def sottrazione(a, b):
    try: 
        return a - b
    except ValueError as e:
        print(f"Errore: {e}")

def moltiplicazione(a, b):
    try:
        return a * b
    except ValueError as e:
        print(f"Errore: {e}")

def divisione(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Il secondo valore non può essere 0 per l'operazione divisione")
        else:
            return a/b
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Error: {e}")

def calcolatrice(a, b, operazione):
    if operazione == somma:
        return somma(a, b)
    elif operazione == sottrazione:
        return sottrazione(a, b)
    elif operazione ==  moltiplicazione:
        return moltiplicazione(a, b)
    elif operazione == divisione:
        return divisione(a, b)
    else:
        print("Operazione non valida")

print(calcolatrice(4, 0, divisione))



