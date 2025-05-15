from sqlalchemy import select, insert, update, delete
from db import SessionLocal
from models import Cliente, Prodotto, Ordine, ordine_prodotto

def crea_cliente(nome: str, email: str) -> Cliente:
    # Creo e salvo un nuovo cliente
    db = SessionLocal()
    cliente = Cliente(nome=nome, email=email)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    db.close()
    return cliente

def lista_prodotti() -> list[Prodotto]:
    # Restituisco tutti i prodotti
    db = SessionLocal()
    prodotti = db.query(Prodotto).all()
    db.close()
    return prodotti

def crea_ordine(cliente_id: int) -> Ordine:
    # Creo un nuovo ordine per un cliente
    db = SessionLocal()
    ordine = Ordine(cliente_id=cliente_id)
    db.add(ordine)
    db.commit()
    db.refresh(ordine)
    db.close()
    return ordine

def aggiungi_prodotto_a_ordine(ordine_id: int, prodotto_id: int, qty: int = 1) -> None:
    # Aggiungo un prodotto a un ordine (aggiorno quantità se già presente)
    db = SessionLocal()
    ordine = db.get(Ordine, ordine_id)
    prod = db.get(Prodotto, prodotto_id)
    if ordine is None or prod is None:
        db.close()
        raise ValueError("Ordine o prodotto non trovato.")

    prodotto_exists = select(ordine_prodotto).where(
        ordine_prodotto.c.ordine_id == ordine_id,
        ordine_prodotto.c.prodotto_id == prodotto_id
    )
    existing = db.execute(prodotto_exists).first()
    if existing:
        upd = (
            update(ordine_prodotto)
            .where(
                ordine_prodotto.c.ordine_id == ordine_id,
                ordine_prodotto.c.prodotto_id == prodotto_id
            )
            .values(quantita=qty)
        )
        db.execute(upd)
    else:
        ins = insert(ordine_prodotto).values(
            ordine_id=ordine_id,
            prodotto_id=prodotto_id,
            quantita=qty
        )
        db.execute(ins)

    db.commit()
    db.close()

def elimina_cliente(cliente_id: int) -> None:
    # Elimino un cliente e i suoi ordini
    db = SessionLocal()
    c = db.get(Cliente, cliente_id)
    if c:
        db.execute(delete(Ordine).where(Ordine.cliente_id == cliente_id))
        db.delete(c)
        db.commit()
    db.close()
    raise ValueError("Cliente non trovato.")

def elimina_ordine(ordine_id: int) -> None:
    # Elimino un ordine e le sue associazioni
    db = SessionLocal()
    db.execute(delete(ordine_prodotto).where(ordine_prodotto.c.ordine_id == ordine_id))
    db.execute(delete(Ordine).where(Ordine.id == ordine_id))
    db.commit()
    db.close()

def lista_clienti() -> list[dict]:
    # Restituisco tutti i clienti come dizionari
    db = SessionLocal()
    all_clienti = select(Cliente)
    clienti = db.execute(all_clienti).scalars().all()
    result = []
    for c in clienti:
        result.append({"id": c.id, "nome": c.nome, "email": c.email})
    db.close()
    return result

def lista_ordini() -> list[dict]:
    # Restituisco tutti gli ordini con dettagli cliente e prodotti
    db = SessionLocal()
    all_ordini = select(Ordine)
    ordini = db.execute(all_ordini).scalars().all()
    result = []
    for o in ordini:
        items = []
        rows = db.execute(
            select(
                ordine_prodotto.c.prodotto_id,
                ordine_prodotto.c.quantita
            ).where(ordine_prodotto.c.ordine_id == o.id)
        ).all()
        for prod_id, qty in rows:
            p = db.get(Prodotto, prod_id)
            items.append({"id": p.id, "nome": p.nome, "prezzo": p.prezzo, "quantita": qty})
        c = db.get(Cliente, o.cliente_id)
        result.append({
            "ordine_id": o.id,
            "cliente": {"id": c.id, "nome": c.nome},
            "data": o.data_creaz,
            "items": items
        })
    db.close()
    return result

def crea_prodotto(nome: str, prezzo: float) -> Prodotto:
    # Crea un nuovo prodotto
    db = SessionLocal()
    prodotto = Prodotto(nome=nome, prezzo=prezzo)
    db.add(prodotto)
    db.commit()
    db.refresh(prodotto)
    db.close()
    return prodotto

def elimina_prodotto(prodotto_id: int) -> None:
    # Elimino un prodotto e le sue associazioni
    db = SessionLocal()
    prodotto = db.get(Prodotto, prodotto_id)
    if prodotto:
        db.execute(delete(ordine_prodotto).where(ordine_prodotto.c.prodotto_id == prodotto_id))
        db.delete(prodotto)
        db.commit()
    db.close()
