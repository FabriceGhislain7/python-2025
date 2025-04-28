import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.salute_max = 200
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []
        self.inventario = []

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")

    def subisci_danno(self, danno):
        self.salute = max(0, self.salute - danno)
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")

    def sconfitto(self):
        return self.salute <= 0

    def recupera_hp(self):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * 0.3)
        nuova_salute = min(self.salute + recupero, 100)
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")

    def usa_oggetto(self, nome_oggetto, bersaglio=None):
        for oggetto in self.inventario:
            if oggetto.nome == nome_oggetto:
                risultato = oggetto.usa(self, bersaglio)
                self.inventario.remove(oggetto)
                return risultato
        print(f"{self.nome} non ha un oggetto chiamato {nome_oggetto}.")

class Mago(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 80

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min - 5, self.attacco_max + 10)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} lancia un incantesimo su {bersaglio.nome} per {danno} danni!")

    def recupera_hp(self):
        recupero = int(self.salute * 0.2)
        self.salute = min(self.salute + recupero, 80)
        print(f"\n{self.nome} medita e recupera {recupero} HP. Salute attuale: {self.salute}")

class Guerriero(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 120

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 15, self.attacco_max + 20)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce con la spada {bersaglio.nome} per {danno} danni!")

    def recupera_hp(self):
        recupero = 30
        self.salute = min(self.salute + recupero, 120)
        print(f"\n{self.nome} si fascia le ferite e recupera {recupero} HP. Salute attuale: {self.salute}")

class Ladro(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)
        self.salute = 140

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 5, self.attacco_max + 5)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} colpisce furtivamente {bersaglio.nome} per {danno} danni!")

    def recupera_hp(self):
        recupero = random.randint(10, 40)
        self.salute = min(self.salute + recupero, 140)
        print(f"\n{self.nome} si cura rapidamente e recupera {recupero} HP. Salute attuale: {self.salute}")
        
class Oggetto:
    def __init__(self, nome):
        self.nome = nome
        self.usato = False

    def usa(self, utilizzatore, bersaglio=None):
        raise NotImplementedError("Questo oggetto non ha effetto definito.")

class PozioneCura(Oggetto):
    def __init__(self, nome="Pozione Rossa", valore=30):
        super().__init__(nome)
        self.valore = valore

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.salute = min(target.salute + self.valore, target.salute_max)
        print(f"{target.nome} usa {self.nome} e recupera {self.valore} salute!")
        self.usato = True

class BombaAcida(Oggetto):
    def __init__(self, nome="Bomba Acida", danno=30):
        super().__init__(nome)
        self.danno = danno

    def usa(self, utilizzatore, bersaglio=None):
        if bersaglio is None:
            print(f"{utilizzatore.nome} cerca di usare {self.nome}, ma non ha un bersaglio!")
            return
        bersaglio.subisci_danno(self.danno)
        print(f"{utilizzatore.nome} lancia {self.nome} su {bersaglio.nome}, infliggendo {self.danno} danni!")
        self.usato = True

class Medaglione(Oggetto):
    def __init__(self):
        super().__init__("Medaglione")

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.attacco_max += 10
        print(f"{target.nome} indossa {self.nome}, aumentando il suo attacco massimo!")
        self.usato = True

def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")

def gioca_torneo():
    mostra_benvenuto()

    classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]
    giocatore = random.choice(classi_giocatore)
    print(f"Hai ottenuto il personaggio: {giocatore.nome}\n")

    nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
    random.shuffle(nemici)
    
    nemici_sconfitti = 0

    for nemico in nemici:
        print(f"\nNuovo avversario: {nemico.nome}")
        turno = 1

        while True:
            print(f"Turno {turno}:")

            # aggiunta oggetti ogni turno (esempio semplice)
            giocatore.inventario.append(PozioneCura())
            giocatore.inventario.append(BombaAcida())
            giocatore.inventario.append(Medaglione())

            # uso BombaAcida contro il nemico
            giocatore.usa_oggetto("Bomba Acida", bersaglio=nemico)

            giocatore.attacca(nemico)
            print("Storico danni subiti dal nemico:", nemico.storico_danni_subiti)

            if nemico.sconfitto():
                print(f"Hai vinto il duello contro {nemico.nome}!")
                giocatore.recupera_hp()
                nemici_sconfitti += 1

                # usa la pozione per curarsi
                giocatore.usa_oggetto("Pozione Rossa")
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
