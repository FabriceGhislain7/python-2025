# random serve per scegliere il personaggio
import random
from utils.utils import mostra_benvenuto
from utils.interfaccia import InterfacciaUtente  # <--- nuovo import
from torneo.turno import Turno
from personaggi.classi import Mago, Guerriero, Ladro
from oggetti.oggetto import PozioneCura, BombaAcida, Medaglione
from inventario.inventario import Inventario

class Torneo:
    def __init__(self):
        self.giocatore = None
        self.nemici = []
        self.nemici_sconfitti = 0

    def setup(self):
        mostra_benvenuto()
        
        # Interattività: scelta manuale del personaggio
        scelta = InterfacciaUtente.chiedi_input(
            "Scegli il tuo personaggio (mago/guerriero/ladro): ",
            opzioni=["mago", "guerriero", "ladro"]
        ).lower()

        if scelta == "mago":
            self.giocatore = Mago("Tu (Mago)")
        elif scelta == "guerriero":
            self.giocatore = Guerriero("Tu (Guerriero)")
        elif scelta == "ladro":
            self.giocatore = Ladro("Tu (Ladro)")

        self.giocatore.inventario = Inventario()  # Assegna inventario
        print(f"\nHai scelto: {self.giocatore.nome}\n")

        # Configurazione nemici
        self.nemici = [Mago("Nemico Mago"), Guerriero("Nemico Guerriero"), Ladro("Nemico Ladro")]
        
       # Randomizzazione dei nemici
        random.shuffle(self.nemici)

    def gioca(self):
        self.setup()
        
        # Aggiungi una pozione iniziale al giocatore
        self.giocatore.inventario.aggiungi(PozioneCura("Pozione Rossa"))
    
        for nemico in self.nemici:
            
            # Aggiungi un oggetto random all'inventario di ogni nemico
            oggetto_random = random.choice([
                PozioneCura("Pozione Rossa"),
                PozioneCura("Pozione Blu", valore=50),
                BombaAcida(),
                Medaglione()
            ])
            nemico.inventario = Inventario()  # Assicuriamoci che ogni nemico abbia un inventario
            nemico.inventario.aggiungi(oggetto_random)
            
            print(f"\nSta per iniziare uno scontro contro {nemico.nome}!")

            # Conferma opzionale prima di ogni combattimento
            if not InterfacciaUtente.conferma("Sei pronto ad affrontarlo?"):
                print("Hai deciso di ritirarti dal torneo.")
                return

            turno = Turno(self.giocatore, nemico)
            turno.esegui()

            if self.giocatore.sconfitto():
                print(f"Hai sconfitto {self.nemici_sconfitti} nemici")
                return

            self.nemici_sconfitti += 1

        print("\nHai vinto il torneo!")
        print(f"Hai sconfitto {self.nemici_sconfitti} nemici.")