from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importa le tabelle
from models import Base

# crea engine mettere true o false in modo da guardare le query
# ci vogliono tre /// perchè è un path relativo
engine = create_engine("sqlite:///app.db", echo=False)

# crea Session
# bind è l'engine della connessione
# autoflush è per fare il flush automatico delle modifiche cioè per scrivere in memoria
# autocommit è per fare il commit automatico delle modifiche
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# crea tutte le tabelle se non esistono
Base.metadata.create_all(bind=engine)