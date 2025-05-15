# random serve per scegliere il personaggio
import random
# mostra_benvenuto stampa il messaggio iniziale
from utils.utils import mostra_benvenuto
# Turno viene usato
from torneo.turno import Turno
# Classi Mago, Guerriero, Ladro servono in modo da creare i personaggi
from personaggi.classi import Mago, Guerriero, Ladro
# Inventario assegnato al giocatore
from inventario.inventario import Inventario

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