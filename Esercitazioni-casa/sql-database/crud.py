from sqlalchemy import insert
from db import SessionLocal, engine
from models import Studente, docenti

def aggiungere_studente(nome: str, classe: str):
    db = SessionLocal()
    try:
        nouvel_eleve = Studente(nom=nome, classe=classe)
        db.add(nouvel_eleve)
        db.commit()
        print(f"Élève {nome} ajouté en {classe}")
    finally:
        db.close()

def aggiungere_docente(nome: str, materie: str):
    with engine.connect() as conn:
        conn.execute(insert(docenti).values(nome=nome, materie=materie))
        conn.commit()
    print(f"Docente {nome} ({materie}) aggiunto")
