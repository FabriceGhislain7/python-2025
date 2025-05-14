from sqlalchemy import insert, select
from db import SessionLocal, engine
from models import Eleve, professeurs

def ajouter_eleve(nom: str, classe: str):
    """Version ORM comme en cours"""
    db = SessionLocal()
    try:
        nouvel_eleve = Eleve(nom=nom, classe=classe)
        db.add(nouvel_eleve)
        db.commit()
        print(f"Élève {nom} ajouté en {classe}")
    finally:
        db.close()

def ajouter_professeur(nom: str, matiere: str):
    """Version Table pure comme vous l'avez fait"""
    with engine.connect() as conn:
        conn.execute(insert(professeurs).values(nom=nom, matiere=matiere))
        conn.commit()
    print(f"Professeur {nom} ({matiere}) ajouté")