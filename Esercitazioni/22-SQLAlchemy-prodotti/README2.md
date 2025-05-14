# SQLAlchemy

db.py
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# CONFIGURAZIONE DELL ENGINE SQLite E DELLA SESSION FACTORY

# importa le tabelle
from models import Base

# crea engine
engine = create_engine("sqlite:///app.db", echo=True)

# crea Session
# bind è l'engine della connessione
# autoflush è per fare il flush automatico delle modifiche cioè per scrivere in memoria
# autocommit è per fare il commit automatico delle modifiche
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# crea tutte le tabelle se non esistono
Base.metadata.create_all(bind=engine)
```
models.py
```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

ordine_prodotto = Table(
    "ordine_prodotto", Base.metadata,
    Column("ordine_id", Integer, ForeignKey("ordini.id"), primary_key=True),
    Column("prodotto_id", Integer, ForeignKey("prodotti.id"), primary_key=True),
    Column("quantita", Integer, default=1)
)

class Cliente(Base):
    __tablename__ = "clienti"
    id      = Column(Integer, primary_key=True)
    nome    = Column(String, nullable=False)
    email   = Column(String, unique=True, nullable=False)
    # back_populates serve per definire la relazione inversa cioè da ordini a cliente
    ordini  = relationship("Ordine", back_populates="cliente") # relazione uno‐a‐molti con ordini

class Prodotto(Base):
    __tablename__ = "prodotti"
    id      = Column(Integer, primary_key=True)
    nome    = Column(String, nullable=False)
    prezzo  = Column(Float, nullable=False)

class Ordine(Base):
    __tablename__ = "ordini"
    id           = Column(Integer, primary_key=True)
    cliente_id   = Column(Integer, ForeignKey("clienti.id"), nullable=False)
    data_creaz   = Column(DateTime, default=datetime.datetime.now)
    cliente      = relationship("Cliente", back_populates="ordini") # relazione molti‐a‐uno con clienti
    # relazione molti‐a‐molti con prodotti
    # bisogna definire una tabella intermedia per la relazione molti‐a‐molti
    # la tabella intermedia è definita sopra come ordine_prodotto
    # secondary serve per definire la tabella intermedia
    # backref serve per definire la relazione inversa cioè da prodotti a ordini
    prodotti    = relationship("Prodotto", secondary=ordine_prodotto, backref="ordini")
```
crud.py
```python
from sqlalchemy import select, insert, update, delete
from db import SessionLocal
from models import Cliente, Prodotto, Ordine, ordine_prodotto

def crea_cliente(nome: str, email: str) -> Cliente:
    # -> Cliente indica che la funzione restituisce un oggetto di tipo Cliente
    # in pratica specifichiamo il tipo di ritorno della funzione
    # bisogna farlo perche se no non viene riconosciuto il tipo di ritorno dato che e un oggetto
    db = SessionLocal() # crea una sessione
    cliente = Cliente(nome=nome, email=email) # crea un oggetto Cliente
    db.add(cliente) # aggiunge il cliente alla sessione
    db.commit() # salva le modifiche nel database
    db.refresh(cliente) # aggiorna l'oggetto cliente con i dati del database
    db.close() # chiude la sessione
    return cliente

def elimina_cliente(cliente_id: int) -> None:
    # -> None indica che la funzione non restituisce nulla
    db = SessionLocal()
    c = db.get(Cliente, cliente_id) # recupera il cliente
    if c: # se il cliente esiste
        # elimina gli ordini associati al cliente
         db.execute(
            delete(Ordine)
            .where(Ordine.cliente_id == cliente_id)
        )
        db.delete(c) # elimina il cliente
        db.commit()
    db.close()
    raise ValueError("Cliente non trovato.")

def crea_ordine(cliente_id: int) -> Ordine:
    # -> Ordine indica che la funzione restituisce un oggetto di tipo Ordine
    db = SessionLocal()
    ordine = Ordine(cliente_id=cliente_id) # crea un oggetto Ordine dove l id cliente corrisponde a quello passato
    db.add(ordine)
    db.commit()
    db.refresh(ordine)
    db.close()
    return ordine

def elimina_ordine(ordine_id: int) -> None:
    db = SessionLocal()
    # prima rimuoviamo le righe di associazione dei prodotti
    db.execute(
        delete(ordine_prodotto)
        .where(ordine_prodotto.c.ordine_id == ordine_id)
    )
     # poi eliminiamo l'ordine
    db.execute(
        delete(Ordine)
        .where(Ordine.id == ordine_id)
    )
    db.commit()
    db.close()

def lista_prodotti() -> list[Prodotto]:
    # -> list[Prodotto] indica che la funzione restituisce una lista di oggetti di tipo Prodotto
    db = SessionLocal()
    prodotti = db.query(Prodotto).all() # recupera tutti i prodotti (SELECT * FROM Prodotti)
    db.close()
    return prodotti

def lista_clienti() -> list[dict]:
    # -> list[dict] indica che la funzione restituisce una lista di dizionari
    db = SessionLocal()
    # recupera tutti i clienti
    all_clienti = select(Cliente)
    # creo una lista di dizionari con i dati dei clienti
    clienti = db.execute(all_clienti).scalars().all() # scalars() serve per recuperare solo gli oggetti altrimenti recupererebbe una lista di tuple
    result = [] # creo una lista vuota che serve a contenere i dizionari
    for c in clienti:
        result.append({"id": c.id, "nome": c.nome, "email": c.email})
    db.close()
    return result

def aggiungi_prodotto_a_ordine(ordine_id: int, prodotto_id: int, qty: int = 1) -> None:
    pass
```
app.py
```python
import argparse
from crud import (crea_cliente, elimina_cliente, crea_ordine, elimina_ordine, lista_prodotti, lista_clienti)

# lo scopo del metodo di lavoro argparse e quello di creare dei comandi che contengano gli argomenti da passare ai parametri delle funzioni
def main():
    parser = argparse.ArgumentParser(description="App CRUD SQLAlchemy") # crea il parser cioè l'oggetto che gestisce gli argomenti della riga di comando
    sub = parser.add_subparsers(dest="cmd", required=True) # crea i sottocomandi sub cioè i comandi che partono da app.py

    # add_cliente -> python app.py add_cliente "Cliente 1" cliente@dominio.com
    p = sub.add_parser("add_cliente", help="Crea un nuovo cliente") # crea il parser per il comando add_cliente
    p.add_argument("nome", help="Nome del cliente") # aggiunge l'argomento nome
    p.add_argument("email", help="Email del cliente") # aggiunge l'argomento email
    args = parser.parse_args() # analizza gli argomenti della riga di comando cioè li legge e li memorizza in args

    if args.cmd == "add_cliente":
        cliente = crea_cliente(args.nome, args.email)
        print(f"Nuovo cliente: {cliente.id} – {cliente.nome}")

if __name__ == "__main__":
    main()
```