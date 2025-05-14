class InterfacciaUtente:
    @staticmethod
    def chiedi_input(messaggio, opzioni=None):
        while True:
            risposta = input(messaggio).strip()
            if opzioni:
                if risposta.lower() in [o.lower() for o in opzioni]:
                    return risposta
                else:
                    print(f"Input non valido! Scelte valide: {', '.join(opzioni)}")
            else:
                return risposta

    @staticmethod
    def chiedi_numero(messaggio, minimo=None, massimo=None):
        while True:
            try:
                numero = int(input(messaggio))
                if minimo is not None and numero <= minimo:
                    print(f"Devi inserire un numero maggiore o uguale a {minimo}.")
                    continue  # uso continue in modo da tornare all inizio del ciclo
                if massimo is not None and numero >= massimo:
                    print(f"Devi inserire un numero minore o uguale a {massimo}.")
                    continue
                return numero

            except ValueError:
                print("Input non valido! Devi inserire un numero intero.")

    @staticmethod
    def conferma(messaggio):
        while True:
            risposta = input(messaggio + " (s/n): ").strip().lower()
            if risposta == 's':
                return True
            elif risposta == 'n':
                return False
            else:
                print("Rispondi con 's' o 'n'.")