
contatore_Fizz = 0
contatore_Buzz = 0
contatore_FizzBuzz = 0
contatore_nessuno = 0

while True:
    
    inserimento = input("Inserisci un numero intero valido oppure inserici 'esci' per uscire dal programma: ")
    
    if inserimento.lower() == "esci":
        print("Ciao, alla prossima.")
        break
    
    if not inserimento.isdigit():
        print("Per favore inserire un numero intero valido oppure 'esci' per uscire dal programma: " )
        continue # Ricomincia il ciclo for while dall'inizio 
    
    numero = int(inserimento)    # Convertiamo la striga in numer intero.

    if numero % 3 == 0 and numero % 5 == 0: 
        print(f"{numero} -> FizzBuzz")
        contatore_FizzBuzz += 1

    elif numero % 3 == 0: 
        print(f"{numero} -> Fizz")
        contatore_Fizz += 1

    elif numero % 5 == 0: 
        print(f"{numero} -> Buzz")
        contatore_Buzz += 1
    else: 
        print(numero)
        contatore_nessuno += 1

print(f"contatore Fizz -> {contatore_Fizz}")
print(f"contatore Buzz -> {contatore_Buzz}")
print(f"contatore FizzBuzz -> {contatore_FizzBuzz}")
print(f"contatore nessuno -> {contatore_nessuno}")




