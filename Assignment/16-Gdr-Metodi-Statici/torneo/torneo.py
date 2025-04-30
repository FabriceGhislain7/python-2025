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
# InterfacciaUtente serve per chiedere input all'utente
from utils.interfaccia import InterfacciaUtente as IU



class Torneo:

    def __init__(self):
        self.giocatore = None
        self.nemici = []
        self.nemici_sconfitti = 0
    

    def setup(self):
        if  self.nemici_sconfitti == 0:
            se_gioca = IU.conferma("Vuoi iniziare il torneo?")
            if se_gioca:
                print("Iniziamo il torneo!")
            else:
                print("Torneo annullato.")
                exit()

        mostra_benvenuto()
        # Configurazioni iniziali del torneo

        # configurazioni personaggio principale
        classi_giocatore = [Mago("Tu (Mago)"), Guerriero("Tu (Guerriero)"), Ladro("Tu (Ladro)")]

        scelta_classe_giocatore = IU.chiedi_input("Scegli il personaggio (Guerriero/Mago/Ladro): ",
                                 opzioni=["Guerriero", "Mago", "Ladro"])
        print(f"Hai scelto la classe: {scelta_classe_giocatore}")

        self.giocatore = scelta_classe_giocatore
        if scelta_classe_giocatore == "Guerriero":
            self.giocatore = Guerriero("Tu (Guerriero)")
        elif scelta_classe_giocatore == "Mago":
            self.giocatore = Mago("Tu (Mago)")
        elif scelta_classe_giocatore == "Ladro":
            self.giocatore = Ladro("Tu (Ladro)")
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