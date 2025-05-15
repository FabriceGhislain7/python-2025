from crud import crea_cliente, lista_prodotti
from db import SessionLocal, engine
from models import Base, Prodotto

# Controllo se tutte le tabelle sono state create
Base.metadata.create_all(bind=engine)

