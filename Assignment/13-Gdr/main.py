import random

class Personaggio:
    def __init__(self, nome):
        self.nome = nome
        self.salute = 100
        self.salute_max = 200
        self.attacco_min = 5
        self.attacco_max = 80
        self.storico_danni_subiti = []
        # aggiungo la proprieta inventario al costruttore
        self.inventario = []  # Lista di oggetti

    def attacca(self, bersaglio):
        danno = random.randint(self.attacco_min, self.attacco_max)
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!")
        # questo metodo esegue un azione o stampa quindi non deve dare un risultato da usare in un if quindi non serve il return

    def subisci_danno(self, danno):
        self.salute = max(0, self.salute - danno)
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome}: {self.salute}\n")
        # questo metodo modifica lo stato di un oggetto quindi non deve dare un risultato da usare in un if quindi non serve il return

    def sconfitto(self):
        return self.salute <= 0
        # in questo caso abbiamo il return perchè chiediamo una risposta e deve darci True o False
        
    def recupera_hp(self):
        if self.salute == 100:
            print(f"{self.nome} ha già la salute piena.")
            return
        recupero = int(self.salute * 0.3)
        nuova_salute = min(self.salute + recupero, 100)
        effettivo = nuova_salute - self.salute
        self.salute = nuova_salute
        print(f"\n{self.nome} recupera {effettivo} HP. Salute attuale: {self.salute}")
        
    def usa_oggetto(self, nome_oggetto):
        for oggetto in self.inventario:
            if oggetto.nome == nome_oggetto:
                oggetto.usa(self)  # applico l'effetto dell oggetto al personaggio
                self.inventario.remove(oggetto)
                return  # uso return per uscire dal ciclo for
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
        # Recupero più lento (solo 20% della salute attuale)
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
        # Recupero costante (30 HP fissi)
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
        # Recupero veloce ma casuale (tra 10 e 40 HP)
        recupero = random.randint(10, 40)
        self.salute = min(self.salute + recupero, 140)
        print(f"\n{self.nome} si cura rapidamente e recupera {recupero} HP. Salute attuale: {self.salute}")
        
class Oggetto:
    def __init__(self, nome, effetto, valore):
        self.nome = nome  # Es: "Pozione"
        self.effetto = effetto  # Es: "cura"
        self.valore = valore  # Es: 20
        self.usato = False  # Es: torcia consumata

    def usa(self, personaggio):
        if self.effetto == "cura":
            personaggio.salute += self.valore
            print(f"{personaggio.nome} usa {self.nome} e recupera {self.valore} salute!")
            personaggio.salute = min(personaggio.salute, personaggio.salute_max)  # Limita la salute al max del personaggio
            self.usato = True  # Indica che l'oggetto è stato usato
            print("-" * 80)
            print(f"Salute attuale: {personaggio.salute}\n")

            # ricordarsi di implementare gli hp mx diversi a seconda del personaggio
        
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")
        
def gioca_torneo():
    mostra_benvenuto()

    # Scelta casuale del giocatore tra le 3 classi
    classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]
    giocatore = random.choice(classi_giocatore)
    print(f"Hai ottenuto il personaggio: {giocatore.nome}\n")

    # Nemici: uno per classe
    nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
    random.shuffle(nemici)
    
    # creazione di un oggetto
    pozione = Oggetto("Pozione gialla", "cura", 20)

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
                giocatore.recupera_hp()
                nemici_sconfitti += 1
                
                # aggiunta all inventario
                giocatore.inventario.append(pozione)
                
                # in gioca_duello il giocatore si cura usando la pozione
                giocatore.usa_oggetto("Pozione gialla")
                
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