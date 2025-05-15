
class InterfacciaUtente:
    @staticmethod
    def chiedi_input(messaggio, opzioni=None):
        while True:
            risposta = input(messaggio).strip()
            if opzioni:
                if risposta.lower() in [o.lower() for o in opzioni]:
                    return risposta
                else:
                    print(f"input non valido. Scelte valide: {', '.join(opzioni)}")
            else:
                return risposta

    @staticmethod
    def chiedi_numero(messaggio, minimo=None, massimo=None):
        while True:
            try:
                numero = int(input(messaggio).strip())
                if minimo is not None and numero <= minimo:
                    print(f"Il numero deve essere maggiore o uguale a {minimo}.")
                    continue
                if massimo is not None and numero >= massimo:
                    print(f"Il numero deve essere minore o uguale a {massimo}.")
                    continue
                return numero

            except ValueError:
                print("Input non valido. Inserisci un numero intero.")

    @staticmethod
    def conferma(messaggio):
        while True:
            risposta = input (messaggio + " (s/n): ").strip().lower()
            if risposta == 's':
                return True
            elif risposta == 'n':
                return False
            else:
                print("Input non valido. Rispondi con 's' o 'n'.")


