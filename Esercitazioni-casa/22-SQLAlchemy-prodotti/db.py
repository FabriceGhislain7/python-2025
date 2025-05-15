from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Impostao le tabelle
from models import Base

# Creo engine
engine = create_engine("sqlite:///app.db", echo=True)

# Crea sessione
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Creo tutte le tabelle se non esisstono
Base.metadata.create_all(bind=engine)
