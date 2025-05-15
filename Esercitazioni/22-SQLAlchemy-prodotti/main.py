from crud import crea_cliente, lista_prodotti
from db import SessionLocal, engine
from models import Base, Prodotto

# Assicurati di aver creato le tabelle
Base.metadata.create_all(bind=engine)

"""
# crea prodotti d’esempio
db = SessionLocal()
db.add_all([
    Prodotto(nome="Penna", prezzo=1.50),
    Prodotto(nome="Quaderno", prezzo=2.70)
])
db.commit()
db.close()
"""

"""
# usa le funzioni
c = crea_cliente("Cliente 1", "cliente@mail.com")
print("Nuovo cliente:", c.id, c.nome)
print("Prodotti disponibili:", lista_prodotti())
"""

if __name__ == "__main__":
    from db import engine
    print("Engine creato:", engine)