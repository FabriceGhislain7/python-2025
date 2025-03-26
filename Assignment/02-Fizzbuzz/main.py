# Inizializzazione dei contatori
count_fizz = 0
count_buzz = 0
count_fizzbuzz = 0
count_nessuno = 0

while True:
    inserimento = input("Inserisci un numero: ")
    
    # se l'utente inserisce "esci" termina il programma e mostra i risultati
    if inserimento.lower() == "esci":
        print("\n--- Risultati ---")
        print(f"Fizz: {count_fizz}")
        print(f"Buzz: {count_buzz}")
        print(f"FizzBuzz: {count_fizzbuzz}")
        print(f"Nessuno: {count_nessuno}")
        break

    if not inserimento.isdigit():
        print("Per favore inserisci un numero valido oppure 'esci'.\n")
        continue

    numero = int(inserimento)

    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz\n")
        count_fizzbuzz += 1  # incremento il contatore di FizzBuzz
    elif numero % 3 == 0:
        print("Fizz\n")
        count_fizz += 1  # incremento il contatore di Fizz
    elif numero % 5 == 0:
        print("Buzz\n")
        count_buzz += 1  # incremento il contatore di Buzz
    else:
        print("Nessuno\n")
        count_nessuno += 1