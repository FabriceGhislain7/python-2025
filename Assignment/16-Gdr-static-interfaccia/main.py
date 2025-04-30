# importa la classe principale Torneo
from utils.interfaccia import InterfacciaUtente
from torneo.torneo import Torneo

def main():
    while True:
        print("\n=== MENU PRINCIPALE ===")
        scelta = InterfacciaUtente.chiedi_input(
            "Scegli un'opzione:\n1) Nuova partita\n2) Esci\n> ",
            opzioni=["1", "2"]
        )

        if scelta == "1":
            torneo = Torneo()
            torneo.gioca()
        elif scelta == "2":
            print("Grazie per aver giocato!")
            break

if __name__ == "__main__":
    main()