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