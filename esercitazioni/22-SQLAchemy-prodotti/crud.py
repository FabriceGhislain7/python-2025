from sqlalchemy import select, insert, update, delete
from db import SessionLocal
from models import Cliente, Prodotto, Ordine,ordini_prodotto

def crea_cliente(nome:int, eamil:str) -> Cliente:
    # -> Cliente significa che la funzione restituisce un oggetto di tipo Cliente
    db = SessionLocal()
    cliente = Cliente(nome=nome, email=email)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    db.close()
    return cliente

def elimina_cliente(cliente_id:int) -> None:
    # -> None significa che la funzione non restituisce nulla
    db = SessionLocal()
    c = db.get(Cliente, cliente_id)  
    if c:
        db.execute(
            delete(ordini_prodotto)
            .where(ordini_prodotto.c.cliente_id == cliente_id)
        )
        # Poi eliminiamo il cliente
        db.execute(
            delete(Cliente)
            .where(Cliente.id == cliente_id)
        )
        db.commit()
    db.close()
    
def crea_ordine(cliente_id:int) -> Ordine:
    # -> Ordine significa che la funzione restituisce un oggetto di tipo Ordine
    db = SessionLocal()
    ordine = Ordine(cliente_id=cliente_id) # crea un nuovo ordine dove l'id cliente corrisponde a quello passato come argomento
    db.add(ordine)
    db.commit()
    db.refresh(ordine)
    db.close()
    return ordine

def lista_prodotti() -> list[Prodotto]:
    # -> list[Prodotto] significa che la funzione restituisce una lista di oggetti di tipo Prodotto
    db = SessionLocal()
    prodotti = db.query(Prodotto).all() # restituisce una lista di tutti i prodotti
    db.close()
    return prodotti

def lista_clienti() -> list[dict]:
    # -> list[dict] significa che la funzione restituisce una lista di dizionari
    db = SessionLocal()
    # Recupera tutti i clienti
    all_clienti = select(Cliente)
    clienti = db.execute(all_clienti).scalars().all()
    result = []
    for cliente in clienti:
        result.append({"id": cliente.id, "nome": cliente.nome, "email": cliente.email})
    db.close()
    return result

def aggiungi_prodotto_a_ordine(ordine_id:int, prodotto_id:int, quantita:int) -> None:
    pass


