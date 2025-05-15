from sqlalchemy import Column, Integer, String, ForeignKey, Table
from db import Base, metadata, engine

# ---- Version ORM (comme en cours) ----
class Eleve(Base):
    __tablename__ = 'eleves'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50))
    classe = Column(String(30))

# ---- Version Table pure (comme vous l'avez fait) ----
professeurs = Table(
    'professeurs', metadata,
    Column('id', Integer, primary_key=True),
    Column('nom', String(50)),
    Column('matiere', String(30))
)

# Création des tables
Base.metadata.create_all(engine)
metadata.create_all(engine)