from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

ordini_prodotto = Table(
    'ordini_prodotti', Base.metadata,
    Column('ordine_id', Integer, ForeignKey('ordini.id'), primary_key=True),
    Column('prodotto_id', Integer, ForeignKey('prodotti.id'), primary_key=True),
    Column('quantita', Integer, default=1)
)

class Cliente(Base):
    __tablename__ = 'clienti'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    # back populates è usato per definire la relazione inversa
    ordini = relationship("Ordine", back_populates="cliente")

class Prodotto(Base):
    __tablename__ = 'prodotti'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    prezzo = Column(Float)

class Ordine(Base):
    __tablename__ = 'ordini'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clienti.id'), nullable=False)
    data_creaz = Column(DateTime, default=datetime.datetime.now) 
    cliente = relationship("Cliente")   # relazione molti a molti con clienti
