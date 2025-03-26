
while True:
    inserimento = input("Inserisci un numero intero valido oppure inserici 'esci' per uscire dal programma: ")
    
    if inserimento.lower() == "esci":
        print("Ciao, alla prossima.")
        break
    
    if not inserimento.isdigit:
        print("Per favore inserire un numero intero valido oppure 'esci' per uscire dal programma: " )
        continue # Ricomincia il ciclo for while dall'inizio 
    
    numero = int(inserimento)    # Convertiamo la striga in numer intero.

    if numero % 3 == 0 and numero % 5 == 0: 
        print(f"{numero} -> FizzBuzz")
    elif numero % 3 == 0: 
        print(f"{numero} -> Fizz")
    elif numero % 5 == 0: 
        print(f"{numero} -> Buzz")
    else: 
        print(numero)
