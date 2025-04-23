import random

# Legge le parole dal file
with open("parole.txt", "r", encoding="utf-8") as file:
    parole = []
    for linea in file:
        # Rimuove gli spazi bianchi e le righe vuote
        parola = linea.strip()
        if parola:  # Controlla se la parola non è vuota
            parole.append(parola)

# Controllo se il file contiene almeno 5 parole
# Se il file è vuoto o contiene meno di 5 parole, mostra un messaggio di errore
if len(parole) < 5:
    print("Errore: il file 'parole.txt' deve contenere almeno 5 parole.")
else:
    # Inizializza punteggio
    punteggio = 0

    # Benvenuto
    print("Prova a indovinare la parola mescolata. Hai 3 tentativi per parola.\n")

    # Gioco principale (sceglie 5 parole diverse)
    parole_scelte = random.sample(parole, 5)  # gli argomenti sono la lista e il numero di parole da scegliere

    for parola in parole_scelte:
        parola_lista = list(parola)
        random.shuffle(parola_lista)
        parola_mescolata = ''.join(parola_lista)  # mescola la parola usando join in modo da non avere spazi dato che in join non ci sono spazi ''

        print("Parola da indovinare:", parola_mescolata)

        tentativi = 3
        while tentativi > 0:
            risposta = input(f"Tentativi rimasti {tentativi}. La tua risposta: ").strip().lower()

            if risposta == parola:
                print("Corretto!")
                punteggio += 1
                break
            else:
                print("Sbagliato!")
                tentativi -= 1

        if tentativi == 0:
            print(f"La parola corretta era: {parola}\n")
        else:
            print()

    # Risultato finale
    print(f"Hai indovinato {punteggio} parole su 5.")

    # Salvataggio su file
    with open("punteggio_indovina_parola.txt", "a", encoding="utf-8") as file:
        file.write(f"Punteggio: {punteggio}/5\n")

    print("Punteggio salvato nel file 'punteggio_indovina_parola.txt'")