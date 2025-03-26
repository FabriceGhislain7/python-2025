numero = int(input("Inserisci un numero: "))  # effettuo la conversione in intero del valore inserito dall'utente in modo da poter effettuare i controlli successivi
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print(numero)