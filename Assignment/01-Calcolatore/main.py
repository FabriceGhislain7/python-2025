# calcolatore basico
while True:
    # definisco quali sono gli input che l'utente deve inserire
    primo_numero = float(input("Inserisci il primo numero: "))
    secondo_numero = float(input("Inserisci il secondo numero: "))
    operazione = input("Inserisci l'operazione da eseguire (+, -, *, /): ")

    # definisco le operazioni che il calcolatore deve eseguire
    if operazione == "+":
        print(primo_numero + secondo_numero)
    elif operazione == "-":
        print(primo_numero - secondo_numero)
    elif operazione == "*":
        print(primo_numero * secondo_numero)
    elif operazione == "/":
        if secondo_numero == 0:
            print("Non puoi dividere per 0")
        else:
            print(primo_numero / secondo_numero)
    else:
        print("Operazione non valida")

    # chiedo all'utente se vuole continuare
    continua = input("Vuoi continuare? (s/n): ")
    if continua.lower() != "s":
        break