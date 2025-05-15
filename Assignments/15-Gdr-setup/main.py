from torneo.torneo import Torneo
from personaggi.classi import Guerriero, Mago, Ladro
from utils.utils import mostra_benvenuto
from inventario.inventario import Inventario

def main():
    mostra_benvenuto()
    torneo = Torneo()
    torneo.setup()

    # Stampa il personaggio del giocatore
    print(f"Hai ricevuto il personaggio: {torneo.giocatore.nome}")

    # Stampa i nemici
    print("I tuoi nemici sono:")
    for nemico in torneo.nemici:
        print(f"- {nemico.nome}")

    # Inizia il torneo
    torneo.gioca()
    print("Torneo concluso!")
    print(f"Hai sconfitto {torneo.nemici_sconfitti} nemici")
    print("Grazie per aver giocato!")
if __name__ == "__main__":
    main()