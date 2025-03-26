while True:
    inserimento = input("Inserisci un numero valido oppure 'esci': ")
    
    if inserimento.lower() == "esci":
        print("Ciao! Alla prossima.")
        break  # uso break in modo da uscire dal ciclo while
    
    if not inserimento.isdigit():  # uso isdigit per controllare se la stringa è un numero
        print("Per favore inserisci un numero valido oppure 'esci'.\n")
        continue  # uso continue in modo da ripartire dal ciclo while

    numero = int(inserimento) # converto la stringa inserimento in un intero

    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} -> fizzBuzz!\n")
    elif numero % 3 == 0:
        print(f"{numero} -> fizz\n")
    elif numero % 5 == 0:
        print(f"{numero} -> buzz\n")
    else:
        print("Nessuno\n")