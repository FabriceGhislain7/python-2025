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
        "attacco_max": 80,
        "storico_danni_subiti": []
    }
    return personaggio

# Funzione con parametri: esegue un attacco
def esegui_attacco(attaccante, difensore):  # prende due personaggi
    danno = random.randint(attaccante["attacco_min"],attaccante["attacco_max"])  # sceglie un numero casuale tra attacco_min ed attacco_max
    difensore["salute"] -= danno  # sottrae il danno alla salute dell altro personaggio
    difensore["storico_danni_subiti"].append(danno)  # <--- salviamo il danno
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

# loop principale di gioco
def gioca_duello():
    # stampo il messaggio di benvenuto
    mostra_benvenuto()

    # Creazione del giocatore
    giocatore = crea_personaggio("Personaggio Principale")

    # Creazione di più nemici
    nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
    nemici = [crea_personaggio(nome) for nome in nomi_nemici]

    # Faccio lo shuffle dei nemici
    random.shuffle(nemici)
    
    # Statistiche torneo
    nemici_sconfitti = 0
    
    # Loop sul torneo: un nemico alla volta
    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico['nome']}")
        
        # definiamo un contatore per i turni
        turno = 1

        # Ciclo finché qualcuno perde (quando la salute è zero)
        while True:
            print(f"Turno {turno}:")

            # Attacco del giocatore
            esegui_attacco(giocatore, nemico)
            
            # stampo lo storico dei danni subiti dal nemico
            print("Storico danni subiti dal nemico:", nemico["storico_danni_subiti"])

            # controlla se il nemico è sconfitto
            if personaggio_sconfitto(nemico):
                print(f"Hai vinto il duello contro {nemico['nome']}!")
                
                # Recupero salute tra scontri (30)
                percentuale_recupero = 0.3
                salute_recuperata = int(giocatore["salute"] * percentuale_recupero)
                
                # Limitiamo il recupero della salute a 100
                if giocatore["salute"] + salute_recuperata > 100:
                    salute_recuperata = 100
                    
                else:
                    # recupero salute
                    giocatore["salute"] += salute_recuperata
                
                # stampo la salute del giocatore
                print(f"\nHai recuperato {salute_recuperata} punti salute! Salute attuale: {giocatore['salute']}")
                
                # incrementa il contatore dei nemici sconfitti
                nemici_sconfitti += 1
                
                break  # Passa al prossimo nemico

            # Attacco del nemico
            esegui_attacco(nemico, giocatore)
            
            # stampo lo storico dei danni subiti dal giocatore
            print("Storico danni subiti dal giocatore:", giocatore["storico_danni_subiti"])

            # controlla se il giocatore è sconfitto
            if personaggio_sconfitto(giocatore):
                print("Sei stato sconfitto!") 
                
                # stampa quanti nemici hai sconfitto
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")
                
                # break → il ciclo continua dopo la sconfitta
                return # esci dalla funzione nel caso di sconfitta

            # incremento il contatore dei turni
            turno += 1
            
    # Se il giocatore ha sconfitto tutti
    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")
        
# punto di ingresso
def main():
    gioca_duello()

# Esegui il gioco
if __name__ == "__main__":
    main()
