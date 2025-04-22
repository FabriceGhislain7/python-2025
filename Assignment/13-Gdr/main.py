import random

# Funzione senza parametri: stampa un messaggio di benvenuto
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")  # Non prende input, non restituisce nulla. Serve solo a stampare testo

# Funzione con parametri: crea un personaggio
def crea_personaggio(nome):  # restituisce un dizionario
    personaggio = {
        "nome": nome,
        "salute": 100,
        "attacco_min": 5,
        "attacco_max": 20,
        "MAX_SALUTE": 100,
        "Storico_danni_subiti": [] 
    }
    return personaggio

# Funzione con parametri: esegue un attacco
def esegui_attacco(attaccante, difensore):  # prende due personaggi
    danno = random.randint(attaccante["attacco_min"],attaccante["attacco_max"])  # sceglie un numero casuale tra attacco_min ed attacco_max
    difensore["salute"] -= danno  # sottrae il danno alla salute dell altro personaggio
    difensore["Storico_danni_subiti"].append(danno)
    # stampo il messaggio di attacco
    print(f"{attaccante['nome']} attacca {difensore['nome']} e infligge {danno} danni!")  # stampa il messaggio di attacco
    # Se la salute scende sotto 0, la riportiamo a zero
    if difensore["salute"] < 0:
        difensore["salute"] = 0
    # stampo la salute del difensore
    print(f"{difensore['nome']} ha {difensore['salute']} punti salute rimasti.")  # stampa la salute del difensore


# Funzione con parametri: controlla se qualcuno è sconfitto
def personaggio_sconfitto(personaggio):  # prende il personaggio
    # ritorna un valore booleano
    return personaggio["salute"] <= 0  # controlla se la salute è zero

def gioca_duello():
    # stampo il messaggio di benvenuto
    mostra_benvenuto()

    # Creiamo i personaggi
    giocatore = crea_personaggio("Alberto")
    nomi_nemici = ["nemico1", "Nemico2", "Nemico3"]
    nemici = [crea_personaggio(nome) for nome in nomi_nemici]

    # definiamo un contatore per i turni
    turno = 1

    nemici_sconfitti = []

     # Ciclo finché qualcuno perde (quando la salute è zero)
    while True:
        if len(nemici) == 0:
            print("Hai vinto il duello!")
            print(f"numero dei nemici sconfiti:{len(nemici_sconfitti)}, nomi:{','.join(nemici_sconfitti)}")
            break

        if turno != 1:
            salute_agiornata = giocatore["salute"] + giocatore["salute"]*0.3
            giocatore["salute"] = salute_agiornata

            if  giocatore["salute"] > giocatore["MAX_SALUTE"]:
                giocatore["salute"] = giocatore["MAX_SALUTE"]
                print(f"Punteggio attuale riportato a: {giocatore["salute"]}")

            print(f"Punteggio attuale aggionato a: {giocatore["salute"]}")

        while len(nemici)!= 0:
            print(f"Turno {turno}:")
            nemico = random.choice(nemici)

            # Attacco del giocatore
            esegui_attacco(giocatore, nemico)

            print(nemico["Storico_danni_subiti"])

            # controlla se il nemico è sconfitto
            if personaggio_sconfitto(nemico):
                print(f"{nemico["nome"]} è stato sconfitto. Prossimo nemico.")
                nemici_sconfitti.append(nemico["nome"])
                nemici.remove(nemico)
                break

            # Attacco del nemico
            esegui_attacco(nemico, giocatore)
            print(giocatore["Storico_danni_subiti"])


            # controlla se il giocatore è sconfitto
            if personaggio_sconfitto(giocatore):
                print('=' * 40)
                print("Sei stato sconfitto!")
                print(f"numero dei nemici sconfitti:{len(nemici_sconfitti)}, nomi:{','.join(nemici_sconfitti)}")
                break # esci dal ciclo nel caso di sconfitta

            # incremento il contatore dei turni
            turno += 1
            print('-' * 40)

# punto di ingresso 
def main():
    gioca_duello()

# Esegui il gioco
if __name__ == "__main__":
    main()




