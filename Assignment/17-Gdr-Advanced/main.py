# importa la classe principale Torneo

from utils.interfaccia import InterfacciaUtente
from torneo.torneo import Torneo
from missioni.missione import Missione
from ambiente.ambiente import ambienti_standard
from oggetti.oggetto import Medaglione

import os

def main():
    ambienti = ambienti_standard()
    missione = Missione(
        nome="Il Cammino del Campione",
        ambienti=ambienti,
        premio=Medaglione(),
        descrizione="Vinci 3 tornei per ottenere il leggendario Medaglione."
    )

    while True:
        print("\n=== MENU PRINCIPALE ===")
        scelta = InterfacciaUtente.chiedi_input(
            "Scegli un'opzione:\n1) Nuova partita\n2) Esci\n> ",
            opzioni=["1", "2"]
        )

        if scelta == "1":
            # pulisci lo schermo
            os.system('cls' if os.name == 'nt' else 'clear')
            torneo = Torneo(missione=missione)
            torneo.gioca()
        elif scelta == "2":
            print("Grazie per aver giocato!")
            break

if __name__ == "__main__":
    main()