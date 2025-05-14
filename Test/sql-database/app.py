from db import engine
from models import Eleve, professeurs
from crud import ajouter_eleve, ajouter_professeur

def peupler_base():
    """Fonction pour insérer des données comme en cours"""
    # Insertion via ORM
    ajouter_eleve("Marie Dupont", "CM2")
    ajouter_eleve("Jean Martin", "6ème")
    
    # Insertion via Table (commande comme en cours)
    ajouter_professeur("M. Legrand", "Maths")
    ajouter_professeur("Mme Leroi", "Français")

    print("Peuplement terminé !")

if __name__ == "__main__":
    peupler_base()