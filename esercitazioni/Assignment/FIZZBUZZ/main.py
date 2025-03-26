

for numero in range(1, 101): # Per ogin numero da 1 a 100
    if numero % 3 == 0 and numero % 5 == 0: # Se è divisibile per entrambi, stampa "FizzBuzz".
        print("FizzBuzz")
    elif numero % 3 == 0: # Se è divisibile per 5, stampa "Buzz"
        print("Fizz")
    elif numero % 5 == 0: # Se è divisibile per entrambi, stampa "FizzBuzz".
        print("Buzz")
    else: # Altrimenti, stampa il numero
        print(numero)
