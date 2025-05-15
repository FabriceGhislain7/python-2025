from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

# Tabella di associazione molti-a-molti tra Ordini e Prodotti
ordine_prodotto = Table(
    "ordine_prodotto", Base.metadata,
    Column("ordine_id", Integer, ForeignKey("ordini.id"), primary_key=True),
    Column("prodotto_id", Integer, ForeignKey("prodotti.id"), primary_key=True),
    Column("quantita", Integer, default=1)
)

class Cliente(Base):
    __tablename__ = "clienti"
    id     = Column(Integer, primary_key=True)
    nome   = Column(String, nullable=False)
    email  = Column(String, unique=True, nullable=False)
    ordini = relationship("Ordine", back_populates="cliente")  # Relazione uno-a-molti

class Prodotto(Base):
    __tablename__ = "prodotti"
    id     = Column(Integer, primary_key=True)
    nome   = Column(String, nullable=False)
    prezzo = Column(Float, nullable=False)

class Ordine(Base):
    __tablename__ = "ordini"
    id         = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clienti.id"), nullable=False)
    data_creaz = Column(DateTime, default=datetime.datetime.now)
    cliente    = relationship("Cliente", back_populates="ordini")  # Relazione molti-a-uno
    prodotti   = relationship("Prodotto", secondary=ordine_prodotto, backref="ordini")  # Relazione molti-a-molti
