import random

class Inventario:
    def __init__(self):
        self.oggetti = []
    
    def aggiungi(self, oggetto):
        self.oggetti.append(oggetto)

    def usa_oggetto(self, nome_oggetto, utilizzatore, bersaglio=None):
        for oggetto in self.oggetti:
            if oggetto.nome == nome_oggetto:
                oggetto.usa(utilizzatore, bersaglio)
                self.oggetti.remove(oggetto)
                return
        print(f"{utilizzatore.nome} non ha un oggetto chiamato {nome_oggetto}.")

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
        
    def prendi_inventario(self, altro_personaggio):
        if altro_personaggio.inventario:
            print(f"\n{self.nome} ottiene l'inventario di {altro_personaggio.nome}:")
            for oggetto in altro_personaggio.inventario:
                print(f" - {oggetto.nome}")
                self.inventario.append(oggetto)
            altro_personaggio.inventario.clear()  # svuota l'inventario del nemico
        else:
            print(f"{altro_personaggio.nome} non aveva oggetti nell'inventario.")

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

class Turno:
    def __init__(self, giocatore, nemico):
        self.giocatore = giocatore
        self.nemico = nemico
        self.numero_turno = 1

    def esegui(self):
        while True:
            print(f"--- Turno {self.numero_turno} ---")

            # Azioni del giocatore
            self.giocatore.inventario.aggiungi(PozioneCura())
            self.giocatore.inventario.aggiungi(BombaAcida())
            self.giocatore.inventario.aggiungi(Medaglione())

            # Usa bomba acida contro il nemico
            self.giocatore.inventario.usa_oggetto("Bomba Acida", self.giocatore, self.nemico)
            self.giocatore.attacca(self.nemico)
            print("Storico danni subiti dal nemico:", self.nemico.storico_danni_subiti)

            if self.nemico.sconfitto():
                print(f"Hai vinto contro {self.nemico.nome}!")
                self.giocatore.recupera_hp()
                self.giocatore.inventario.usa_oggetto("Pozione Rossa", self.giocatore)
                break

            # Azioni del nemico
            self.nemico.attacca(self.giocatore)
            print("Storico danni subiti dal giocatore:", self.giocatore.storico_danni_subiti)

            if self.giocatore.sconfitto():
                print(f"Sei stato sconfitto da {self.nemico.nome}!")
                break

            self.numero_turno += 1
            
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")

class Torneo:
    def __init__(self):
        self.giocatore = None
        self.nemici = []
        self.nemici_sconfitti = 0

    def setup(self):
        mostra_benvenuto()
        # Configurazioni iniziali del torneo

        # configurazioni personaggio principale
        classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]
        self.giocatore = random.choice(classi_giocatore)
        self.giocatore.inventario = Inventario()  # assegna un inventario
        print(f"Hai ricevuto il personaggio: {self.giocatore.nome}")

        # configurazioni nemici
        self.nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
        random.shuffle(self.nemici)

    def gioca(self):
        self.setup()

        for nemico in self.nemici:
            turno = Turno(self.giocatore, nemico)
            turno.esegui()

            if self.giocatore.sconfitto():
                print(f"Hai sconfitto {self.nemici_sconfitti} nemici")
                return

            # incremento il contatore dei nemici sconfitti
            self.nemici_sconfitti +=1

        print("Hai vinto il torneo")
        print(f"Hai sconfitto {self.nemici_sconfitti} nemici")

def main():
    torneo = Torneo()
    torneo.gioca()

# Firma di avvio
if __name__ == "__main__":
    main()
    