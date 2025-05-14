# SQLalchemy

In sintesi
models.py → definisce le tabelle e le relazioni.
db.py → crea l’engine e la sessione, inizializza il database.
crud.py → implementa le operazioni su tabelle e associazioni.
app.py → espone tutti questi metodi tramite comandi da terminale.
Così hai un’architettura modulare, chiara e facilmente estendibile

1. models.py

Definisce la struttura dati del database tramite classi ORM di SQLAlchemy:

Base = declarative_base()
punto di partenza per tutte le classi “mappate” sul DB.
ordine_prodotto
tabella di associazione many‐to‐many tra ordini e prodotti, con campo aggiuntivo quantita.
class Cliente
mappa la tabella clienti con colonne id, nome, email e la relazione uno-a-molti verso Ordine.
class Prodotto
mappa la tabella prodotti con colonne id, nome, prezzo.
class Ordine
mappa la tabella ordini con colonne id, cliente_id, data_creaz e la relazione many-to-many verso Prodotto tramite ordine_prodotto.
2. db.py

Configura la connessione e la sessione verso il database:

engine = create_engine("sqlite:///app.db", echo=False)
crea il “motore” che parla con SQLite e, con echo=False, disabilita il log delle query in console.
SessionLocal = sessionmaker(...)
fabbrica oggetti sessione per interagire col DB (CRUD, transazioni, ecc.).
Base.metadata.create_all(bind=engine)
controlla che tutte le tabelle definite in models.py esistano nel file app.db, e le crea se mancano.
3. crud.py

Raccoglie tutte le funzioni di accesso al database (Create, Read, Update e Delete):

crea_cliente(nome, email)
aggiunge un nuovo record in clienti.
lista_prodotti()
restituisce tutti i prodotti dalla tabella prodotti.
crea_ordine(cliente_id)
crea un nuovo ordine collegato a un cliente esistente.
aggiungi_prodotto_a_ordine(ordine_id, prodotto_id, qty)
gestisce la tabella di associazione ordine_prodotto:
se l’accoppiata esiste già, ne aggiorna la quantita
altrimenti ne inserisce una nuova riga.
elimina_cliente(cliente_id)
cancella un cliente (e, grazie alle impostazioni di relazione, i suoi ordini associati se configurato con cascade).
elimina_ordine(ordine_id)
rimuove prima le righe in ordine_prodotto per quell’ordine e poi il record in ordini.
lista_ordini()
restituisce una lista di dict che per ciascun ordine include:
ID, data, dati del cliente
lista di prodotti con id, nome, prezzo e quantità.
4. app.py

Fornisce un’interfaccia da linea di comando (CLI) per usare le funzioni di crud.py:

argparse definisce i comandi disponibili:
add_cliente <nome> <email>
del_cliente <cliente_id>
add_ordine <cliente_id>
del_ordine <ordine_id>
add_prod_ordine <ordine_id> <prodotto_id> [quantita]
list_prodotti
list_ordini
In base al comando (args.cmd), chiama la corrispondente funzione di crud.py e stampa il risultato o un messaggio di conferma.

# Esercitazione 1 – Installazione e setup di base

Obiettivo: installare SQLAlchemy, creare l’engine e una sessione.

Crea un nuovo virtualenv e attiva:
python3 -m venv venv
source venv/bin/activate
Installa SQLAlchemy:
pip install SQLAlchemy
In un file db.py, configura l’engine SQLite e la session factory:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1) crea engine
engine = create_engine("sqlite:///app.db", echo=True)

# 2) crea Session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Testa l’import:
if __name__ == "__main__":
    from db import engine
    print("Engine creato:", engine)
Verifica: lancia python db.py e controlla che non dia errori.

# Esercitazione 2 – Definizione dei modelli ORM

Obiettivo: creare le classi Python per Prodotto, Cliente, Ordine con SQLAlchemy ORM.

In models.py:
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clienti"
    id      = Column(Integer, primary_key=True)
    nome    = Column(String, nullable=False)
    email   = Column(String, unique=True, nullable=False)
    ordini  = relationship("Ordine", back_populates="cliente")

class Prodotto(Base):
    __tablename__ = "prodotti"
    id      = Column(Integer, primary_key=True)
    nome    = Column(String, nullable=False)
    prezzo  = Column(Float, nullable=False)

class Ordine(Base):
    __tablename__ = "ordini"
    id           = Column(Integer, primary_key=True)
    cliente_id   = Column(Integer, ForeignKey("clienti.id"), nullable=False)
    data_creaz   = Column(DateTime, default=datetime.datetime.utcnow)
    cliente      = relationship("Cliente", back_populates="ordini")
    # relazione molti‐a‐molti con prodotti verrà aggiunta in seguito
In db.py, importa e crea tutte le tabelle:
from models import Base
Base.metadata.create_all(bind=engine)
Esegui:
python db.py
e verifica che nascano i file/tabelle SQLite.
Esercitazione 3 – Operazioni di Create e Read

Obiettivo: inserire e leggere record da DB.

In crud.py scrivi funzioni:
from db import SessionLocal
from models import Cliente, Prodotto, Ordine

def crea_cliente(nome: str, email: str):
    db = SessionLocal()
    cliente = Cliente(nome=nome, email=email)
    db.add(cliente); db.commit(); db.refresh(cliente)
    db.close()
    return cliente

def lista_prodotti():
    db = SessionLocal()
    prodotti = db.query(Prodotto).all()
    db.close()
    return prodotti
Nel main.py prova:
from crud import crea_cliente, lista_prodotti
from db import engine
from models import Base, Prodotto

# Assicurati di aver creato le tabelle
Base.metadata.create_all(bind=engine)

# crea prodotti d’esempio
db = SessionLocal()
db.add_all([
    Prodotto(nome="Penna", prezzo=1.50),
    Prodotto(nome="Quaderno", prezzo=2.70)
])
db.commit()
db.close()

# usa le funzioni
c = crea_cliente("Mario Rossi", "mario@example.com")
print("Nuovo cliente:", c.id, c.nome)
print("Prodotti disponibili:", lista_prodotti())
Verifica: il terminale mostra i prodotti e il cliente creati.
Esercitazione 4 – Update e Delete + Relazioni Ordine-Prodotto

Obiettivo: aggiornare, cancellare e modellare la relazione molti-a-molti Ordine↔Prodotto.

Aggiungi una tabella di associazione in models.py:
from sqlalchemy import Table

ordine_prodotto = Table(
    "ordine_prodotto", Base.metadata,
    Column("ordine_id", Integer, ForeignKey("ordini.id"), primary_key=True),
    Column("prodotto_id", Integer, ForeignKey("prodotti.id"), primary_key=True),
    Column("quantita", Integer, default=1)
)

# modifica in Ordine:
class Ordine(Base):
    # ...
    prodotti = relationship("Prodotto", secondary=ordine_prodotto, backref="ordini")
In crud.py aggiungi:
def aggiungi_prodotto_a_ordine(ordine_id: int, prodotto_id: int, qty: int=1):
    db = SessionLocal()
    ordine = db.get(Ordine, ordine_id)
    prod   = db.get(Prodotto, prodotto_id)
    ordine.prodotti.append(prod)
    # poi aggiorna qty manualmente:
    db.execute(
        ordine_prodotto.update()
        .where(ordine_prodotto.c.ordine_id==ordine_id)
        .where(ordine_prodotto.c.prodotto_id==prodotto_id)
        .values(quantita=qty)
    )
    db.commit()
    db.close()

def elimina_cliente(cliente_id: int):
    db = SessionLocal()
    c = db.get(Cliente, cliente_id)
    db.delete(c); db.commit(); db.close()
Scrivi uno script di test: crea un ordine, aggiungi prodotti, poi cancella un cliente e osserva la cascata (configura cascata in relazione se necessario).
Esercitazione 5 – Semplice interfaccia CRUD (CLI o Flask)

Obiettivo: metti tutto insieme in un piccolo tool da linea di comando o in una mini-app Flask.

Opzione A: CLI con argparse
Crea app.py con:
import argparse
from crud import (
    crea_cliente, lista_prodotti, aggiungi_prodotto_a_ordine,
    # ...
)

parser = argparse.ArgumentParser(description="App CRUD SQLAlchemy")
sub = parser.add_subparsers(dest="cmd")

# comando: add_cliente
p1 = sub.add_parser("add_cliente")
p1.add_argument("nome"); p1.add_argument("email")

# comando: list_prodotti
sub.add_parser("list_prodotti")

# altro: add_ordine, add_prod_ordine, upd, del

args = parser.parse_args()
if args.cmd == "add_cliente":
    c = crea_cliente(args.nome, args.email)
    print("Creato:", c.id)
elif args.cmd == "list_prodotti":
    for p in lista_prodotti():
        print(p.id, p.nome, p.prezzo)
Esegui in terminale, es.:
python app.py add_cliente "Luigi Bianchi" luigi@dominio.com
python app.py list_prodotti
Opzione B: Mini-app Flask
Installa Flask: pip install Flask
In app.py:
from flask import Flask, request, jsonify
from crud import crea_cliente, lista_prodotti, aggiungi_prodotto_a_ordine

app = Flask(__name__)

@app.route("/clienti", methods=["POST"])
def api_crea_cliente():
    data = request.json
    c = crea_cliente(data["nome"], data["email"])
    return jsonify({"id": c.id, "nome": c.nome})

@app.route("/prodotti", methods=["GET"])
def api_lista_prodotti():
    prodotti = lista_prodotti()
    return jsonify([{"id": p.id, "nome": p.nome, "prezzo": p.prezzo} for p in prodotti])

# rotte per ordini, update, delete
if __name__ == "__main__":
    app.run(debug=True)
Lancia python app.py, accedi a http://127.0.0.1:5000/prodotti via browser o curl.
Con queste 5 esercitazioni ti sarai fatto le ossa con:

Setup di engine e session.
Modelli e migrazioni basic.
CRUD create/read.
Update/Delete e relazioni molti-a-molti.
Interfaccia (CLI o web)