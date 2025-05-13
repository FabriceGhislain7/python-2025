from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente, Prodotto, Ordine

# Crea l'engine e connette al DB SQLite
engine = create_engine('sqlite:///prodotti.db', echo=True)

# Crea le tabelle
Base.metadata.create_all(bind=engine)

# Crea la sessione
SessionLocal = sessionmaker(bind=engine)

# Esempio: inserimento cliente
nuovo_cliente = Cliente(nome='Mario Rossi', email='mario@example.com')
session.add(nuovo_cliente)
session.commit()

print("Cliente aggiunto con successo.")
