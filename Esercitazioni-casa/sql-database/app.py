from db import engine
from models import Studente, docenti
from crud import aggiungere_studente, aggiungere_docente

def popolare_base():
    # Inserimento via ORM
    aggiungere_studente("Marie Dupont", "CM2")
    aggiungere_studente("Jean Martin", "6ème")
    
    # Inserimento usando il metodo Table
    aggiungere_docente("M. Legrand", "Maths")
    aggiungere_docente("Mme Leroi", "Français")

    print("Peuplement terminé !")

if __name__ == "__main__":
    popolare_base()