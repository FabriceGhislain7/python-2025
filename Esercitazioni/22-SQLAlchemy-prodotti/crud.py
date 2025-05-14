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

def lista_prodotti() -> list[Prodotto]:
    # -> list[Prodotto] indica che la funzione restituisce una lista di oggetti di tipo Prodotto
    db = SessionLocal() # crea una sessione
    prodotti = db.query(Prodotto).all() # recupera tutti i prodotti

    db.close() # chiude la sessione
    return prodotti

def crea_ordine(cliente_id: int) -> Ordine:
    db = SessionLocal()
    ordine = Ordine(cliente_id=cliente_id) # crea un oggetto Ordine dove l id cliente corrisponde a quello passato
    db.add(ordine)
    db.commit()
    db.refresh(ordine)
    db.close()
    return ordine

def aggiungi_prodotto_a_ordine(ordine_id: int, prodotto_id: int, qty: int = 1) -> None:
    db = SessionLocal()

    # Verifica che ordine e prodotto esistano
    ordine = db.get(Ordine, ordine_id)
    prod   = db.get(Prodotto, prodotto_id)
    if ordine is None or prod is None:
        db.close()
        raise ValueError("Ordine o prodotto non trovato.")

    # Controlla se c'è già una riga in ordine_prodotto
    prodotto_exists = select(ordine_prodotto).where(
        ordine_prodotto.c.ordine_id == ordine_id,
        ordine_prodotto.c.prodotto_id == prodotto_id
    )
    existing = db.execute(prodotto_exists).first() # il metodo first() serve per recuperare solo la prima riga

    if existing:
        # Già presente aggiorna la quantita
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
        # Non presente inserisci nuova riga
        ins = insert(ordine_prodotto).values(
            ordine_id=ordine_id,
            prodotto_id=prodotto_id,
            quantita=qty
        )
        db.execute(ins)

    db.commit()
    db.close()

def elimina_cliente(cliente_id: int) -> None:
    # -> None indica che la funzione non restituisce nulla
    # dobbiamo eliminare prima gliordini associati al cliente
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

def lista_ordini() -> list[dict]:
    # -> list[dict] indica che la funzione restituisce una lista di dizionari
    db = SessionLocal()
    # recupera tutti gli ordini con cliente e prodotti
    stmt = select(Ordine)
    ordini = db.execute(stmt).scalars().all() # scalars() serve per recuperare solo gli oggetti altrimenti recupererebbe una lista di tuple
    result = []
    for o in ordini:
        items = []
        # accedi alla tabella di associazione
        rows = db.execute(
            select(
                ordine_prodotto.c.prodotto_id,
                ordine_prodotto.c.quantita
            ).where(ordine_prodotto.c.ordine_id == o.id)
        ).all()
        for prod_id, qty in rows: # prod_id e qty sono le colonne della tabella di associazione
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
    db = SessionLocal()
    prodotto = Prodotto(nome=nome, prezzo=prezzo)
    db.add(prodotto)
    db.commit()
    db.refresh(prodotto)
    db.close()
    return prodotto

def elimina_prodotto(prodotto_id: int) -> None:
    db = SessionLocal()
    prodotto = db.get(Prodotto, prodotto_id)
    # prima di eliminare il prodotto, dobbiamo rimuovere le associazioni nella tabella di associazione
    db.execute(
        delete(ordine_prodotto)
        .where(ordine_prodotto.c.prodotto_id == prodotto_id)
    )
    # ora possiamo eliminare il prodotto
    if prodotto:
        db.delete(prodotto)
        db.commit()
    db.close()