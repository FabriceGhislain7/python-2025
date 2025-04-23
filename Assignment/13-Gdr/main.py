import random

class Personaggio:
    def __init__(self, nome):  # Costruttore
        self.nome = nome  # Attributo
        self.salute = 100
        self.attacco_min = 5
        self.attacco_max = 20
        self.MAX_SALUTE = 100
        self.storico_dani_subiti = []

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

    def sconfitto(self):
        return self.salute <= 0

def gioca_torneo(): 

    # Definiamo i personaggi del torneo
    giocatore = Personaggio("Personaggio Pincipale")
    num_nemici = 5 
    nemici = [Personaggio(f"nemico{n}") for n in range(1, num_nemici + 1)]
    random.shuffle(nemici)

    for nemico in nemici:  # Solo per verificare la presenza 
        print(nemico.nome)

    for nemico in nemici:
        while True:
            print("--------------------")
            giocatore.attacca(nemico)
            if nemico.sconfitto:
                print(f"{nemico.nome} sconfitto. Next step.")
                break
            nemico.attacca(giocatore)
            if giocatore.sconfitto:
                print("Sei stato sconfitto. Fine della partita.")
                return

    print(f"Hai sconfitto tutti i nemici.")

def main():
    gioca_torneo()

if __name__ == "__main__":
    main()