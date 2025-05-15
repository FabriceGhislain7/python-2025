from sqlalchemy import Column, Integer, String, Table
from db import Base, metadata, engine

# Versione con ORM 
class Studente(Base):
    __tablename__ = 'studenti'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50))
    classe = Column(String(30))

# Versione con Table 
docenti = Table(
    'docenti', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50)),
    Column('materie', String(30))
)

# Creazione delle tabelle
Base.metadata.create_all(engine)
metadata.create_all(engine)
