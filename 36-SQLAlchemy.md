# SQLAlchemy

SqlAlchemy è un ORM (Object Relational Mapper) per Python, che permette di interagire con i database in modo più semplice e intuitivo rispetto all'uso diretto di SQL. Con SqlAlchemy, puoi definire le tue classi Python come modelli di dati e utilizzare queste classi per eseguire operazioni CRUD (Create, Read, Update, Delete) sui dati nel database.

## Vantaggi

- **Astrazione**: SqlAlchemy fornisce un livello di astrazione sopra SQL, permettendo di lavorare con oggetti Python invece di scrivere query SQL a mano.
- **Portabilità**: SqlAlchemy supporta diversi database (MySQL, PostgreSQL, SQLite, ecc.), quindi puoi cambiare il database senza modificare il tuo codice.
- **Facilità d'uso**: La sintassi di SqlAlchemy è più semplice e intuitiva rispetto a SQL, rendendo più facile per i programmatori Python lavorare con i database.
- **Supporto per le transazioni**: SqlAlchemy gestisce automaticamente le transazioni, garantendo che le operazioni sul database siano atomiche e sicure.

## Svantaggi

- **Prestazioni**: In alcuni casi, SqlAlchemy può essere più lento rispetto all'esecuzione diretta di query SQL, specialmente per operazioni complesse o su grandi quantità di dati.
- **Curva di apprendimento**: Anche se SqlAlchemy è più semplice rispetto a SQL, può comunque richiedere del tempo per imparare a usarlo correttamente, specialmente per le funzionalità avanzate.
- **Overhead**: SqlAlchemy introduce un certo overhead rispetto all'uso diretto di SQL, il che può influire sulle prestazioni in alcune situazioni. (l hoverhead è il tempo e le risorse aggiuntive necessarie per eseguire un'operazione rispetto a un'operazione diretta)
- **Configurazione**: La configurazione iniziale di SqlAlchemy può essere complessa, specialmente per i principianti.
- **Debugging**: Il debugging delle query generate da SqlAlchemy può essere più difficile rispetto a SQL, poiché le query sono generate automaticamente e potrebbero non essere immediatamente visibili.

## Installazione e setup di base

Crea un nuovo virtualenv e attiva:
```bash
python -m venv venv
# MacOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

Installa SQLAlchemy:
```bash
pip install SQLAlchemy
```
In un file db.py, configura l’engine SQLite e la session factory:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
```

## 1) crea engine

engine = create_engine("sqlite:///app.db", echo=True)

## 2) crea Session

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Testa l’import:
```python
if __name__ == "__main__":
    from db import engine
    print("Engine creato:", engine)
```

Verifica: lancia python db.py e controlla che non dia errori

# Definizione dei modelli ORM
> models.py
```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()  # Base è la classe base per i modelli ORM che uso in modo da definire le mie classi come modelli di dati

class Cliente(Base):
    __tablename__ = "clienti" # indica il nome della tabella nel database creato
    id      = Column(Integer, primary_key=True)
    nome    = Column(String, nullable=False)  # nullable indica che il dato è richiesto in modo esplicito
    email   = Column(String, unique=True, nullable=False) # unique indica che la colonna non puo contenere dati ripetuti
    ordini  = relationship("Ordine", back_populates="cliente") # back_populate indica 

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
    # relazione molti‐a‐molti con prodotti verrà aggiunta dopo
```
db.py, importa e crea tutte le tabelle
```
from models import Base
Base.metadata.create_all(bind=engine)
```
Esegui
```bash
python db.py
```
Controlla che siano state create le tabelle nel database SQLite

# Operazioni di Create e Read

In crud.py scrivi funzioni:

```python
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
```

Nel main.py prova:

```python
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
c = crea_cliente("Cliente1", "cliente1@example.com")
print("Nuovo cliente:", c.id, c.nome)
print("Prodotti disponibili:", lista_prodotti())
Verifica: il terminale mostra i prodotti e il cliente creati
```

# Update e Delete ed Relazioni Ordine-Prodotto
Aggiungi una tabella di associazione in models.py:
```python
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

python
Copia
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
Scrivi uno script di test: crea un ordine, aggiungi prodotti, poi cancella un cliente e osserva la cascata (configura cascata in relazione se necessario)
```

# Semplice interfaccia CRUD (argparse)

Gli argparse sono un modo per gestire gli argomenti della riga di comando in Python. Puoi usarli per creare un'interfaccia semplice per il tuo CRUD.

Il vantaggio di usare argparse è che puoi eseguire il tuo script da riga di comando e passare gli argomenti direttamente, senza dover modificare il codice ogni volta.

In pratica quando avviamo l applicazione con un comando come:
```bash
python app.py add_cliente "Nome Cliente" "email_cliente@dominio.com"
```
L'applicazione eseguirà l'azione specificata (in questo caso, `crea_cliente`) e utilizzerà i parametri forniti per eseguire l'operazione desiderata.

app.py
```python
import argparse
from crud import (
    crea_cliente, lista_prodotti, aggiungi_prodotto_a_ordine,
    elimina_cliente, crea_ordine, lista_ordini
)

parser = argparse.ArgumentParser(description="App CRUD SQLAlchemy")  # parser è il parser principale per gli argomenti della riga di comando
sub = parser.add_subparsers(dest="cmd")  # sub è il parser secondario per i comandi specifici che vogliamo eseguire

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
```

Esegui:
```bash
python app.py add_cliente "Nome Cliente" "email_cliente@dominio.com"
python app.py list_prodotti
```

Aggiungi gli altri metodi ed argomenti
```bash
# comandi
# Aggiungi Cliente -> python app.py add_cliente "Cliente 1" "cliente@dominio.com"
# Elenco di prodotti -> python app.py list_prodotti
# Aggiungi Ordine -> python app.py add_ordine 1
# Aggiungi Prodotto a Ordine -> python app.py add_prod_ordine 1 2 3
# Elimina Cliente -> python app.py del_cliente 1
# Elimina Ordine -> python app.py del_ordine 1
# Elenco di Ordini -> python app.py list_ordini
```