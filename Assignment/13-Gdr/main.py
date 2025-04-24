import random

# Definiamo la classe Personaggio ----------------------------------------------
class Personaggio:
    def __init__(self, nome):  # Costruttore
        self.nome = nome  # Attributo
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 20
        self.MAX_SALUTE = 100
        self.storico_dani_subiti = []
        self.storico_aiuto_ricevuto = []
        self.inventario = []

    def attacca(self, bersaglio): # Metodo
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti.")

    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_dani_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}")
    
    def recupera_hp(self):
        bonus = 30
        self.salute += bonus
        self.salute = min(self.salute, 100)
        print(f"{self.nome} riceve {bonus} di salute in più.")
    
    def sconfitto(self):
        return self.salute <= 0
    
    # Aggiungiamo un attributo alla nostra classe Personaggio
    def usa_oggetto(self, nome_oggetto):
        for oggetto in self.inventario:
            if oggetto.nome == oggetto:
                oggetto.usa(self)
                self.inventario.remove(oggetto)
                return # per uscire dal ciclo
        print(f"{self.nome} non ha un oggetto chiamato {nome_oggetto}")

# Definiamo la classe Mago------------------------------------------------------
class Mago(Personaggio):
    def __init__(self, nome):
        super().__init__(nome)

    def recupera_hp(self):
        bonus = 0.3 * self.salute
        self.salute += bonus
        print(f"{self.nome} ha recuperato {bonus} si salute")

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 15, self.attacco_max + 20)
        bersaglio.salute -= danno
        print(f"{self.nome} lancia un incatesimo su {bersaglio.nome} per {danno} danni.")


# Definiamo la classe Guerriero ------------------------------------------------
class Guerriero(Personaggio):
    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min + 15, self.attacco_max + 20)
        bersaglio.salute -= danno
        print(f"{self.nome} colpisce con una spada {bersaglio.nome} per {danno} danni.")

# Definiamo la classe Prontosoccorso -------------------------------------------
class Prontosoccorso(Personaggio):
    def aiuta(self, bersaglio): # Metodo
        if random.randint(1, 0) == 1:
            aiuto = 0.5 * random.randint(self.attacco_min, self.attacco_max)
            bersaglio.riceve_aiuto(aiuto)
            print(f"{self.nome} riceve {bersaglio.nome} per {aiuto} punti.")

    def recive_aiuto(self, aiuto):
        aiuto = 0.5 * random.randint(self.attacco_min, self.attacco_max)
        self.salute += aiuto
        self.storico_aiuto_ricevuto.append(aiuto)
        print(f"Salute di {self.nome}: {self.salute}")

# Definiamo la classe oggetto
class Oggetto:
    def __init__(self, nome, effetto, valore):
        self.nome = nome
        self.effetto = effetto
        self.valore = valore
        self.usato = False

    def usa(self, personaggio):
        if  self.effetto == "cura":
            personaggio.salute += self.valore
            print(f"{personaggio.nome} usa {self.nome} e recupera {self.valore} salute.")
            personaggio.salute = min(personaggio.salute, personaggio.salute_max)
            self.usato = True
            print(f"Salute attuale: {personaggio.salute}\n")

            # ricordiamoci di implementare gli hp mx diversi a secondo del personaggio


# PARTENZA DEL TORNEO ==========================================================
def gioca_torneo():
    giocatore = Personaggio("Personaggio Pincipale")
    soccorso = Prontosoccorso("Pronto Soccorso")
    pozione = Oggetto("Pozione gialla", "cura", 20)
    num_nemici = 5
    nemici = [Mago(f"nemico{n}") for n in range(1, num_nemici + 1)]
    random.shuffle(nemici)

    for nemico in nemici:
        print(nemico.nome)

    for nemico in nemici:
        while True:
            print("-" * 40)
            giocatore.attacca(nemico)
            if nemico.sconfitto:
                print(f"{nemico.nome} sconfitto. Next step.")
                break
            soccorso.aiuta(nemico)
            nemico.attacca(giocatore)
            if giocatore.sconfitto:
                print("Sei stato sconfitto. Fine della partita.")
                return
            giocatore.recupera_hp()
            nemico.recupera_hp()
            giocatore.usa_oggetto()

    print(f"Hai sconfitto tutti i nemici.")

def main():
    gioca_torneo()

if __name__ == "__main__":
    main()