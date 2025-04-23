import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
    def recupera_hp(self, percentuale):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * percentuale)
        nuova_salute = min(self.salute + recupero, 100)
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")
        
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")
        
def gioca_torneo():
    mostra_benvenuto()

    # Creazione del giocatore
    giocatore = Personaggio("Personaggio Principale")

    # Creazione dei nemici
    nomi_nemici = ["Nemico1", "Nemico2", "Nemico3"]
    nemici = [Personaggio(nome) for nome in nomi_nemici]
    random.shuffle(nemici)

    nemici_sconfitti = 0

    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico.nome}")
        turno = 1

        while True:
            print(f"Turno {turno}:")

            giocatore.attacca(nemico)
            print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)

            if nemico.sconfitto():
                print(f"Hai vinto il duello contro {nemico.nome}!")
                
                # Recupero salute del 30%
                giocatore.recupera_hp(0.3)
                
                nemici_sconfitti += 1
                
                break

            nemico.attacca(giocatore)
            print("Storico danni subiti dal giocatore:", giocatore.storico_danni_subiti)

            if giocatore.sconfitto():
                print("Sei stato sconfitto!")
                print(f"Hai sconfitto {nemici_sconfitti} nemico/i.")
                
                return

            turno += 1

    print("\nHai vinto il torneo! Tutti i nemici sono stati sconfitti!")
    print(f"Nemici sconfitti: {nemici_sconfitti}")

def main():
    gioca_torneo()

if __name__ == "__main__":
    main()