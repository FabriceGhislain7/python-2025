import argparse
from crud import (
    crea_cliente,
    lista_prodotti,
    crea_ordine,
    aggiungi_prodotto_a_ordine,
    elimina_cliente,
    elimina_ordine,
    lista_ordini
)

# comandi
# python app.py add_cliente "Cliente 1" cliente@dominio.com
# python app.py list_prodotti
# python app.py add_ordine 1
# python app.py add_prod_ordine 1 2 3
# python app.py del_cliente 1
# python app.py del_ordine 1
# python app.py list_ordini

def main():
    parser = argparse.ArgumentParser(description="App CRUD SQLAlchemy") # crea il parser cioè l'oggetto che gestisce gli argomenti della riga di comando
    sub = parser.add_subparsers(dest="cmd", required=True) # crea i sottocomandi sub cioè i comandi che partono da app.py

    # add_cliente
    p = sub.add_parser("add_cliente", help="Crea un nuovo cliente") # crea il parser per il comando add_cliente
    # help serve per mostrare il messaggio di aiuto quando si usa il comando --help
    p.add_argument("nome", help="Nome del cliente") # aggiunge l'argomento nome
    p.add_argument("email", help="Email del cliente") # aggiunge l'argomento email

    # del_cliente
    p = sub.add_parser("del_cliente", help="Elimina un cliente per ID")
    p.add_argument("cliente_id", type=int, help="ID del cliente da eliminare")

    # add_ordine
    p = sub.add_parser("add_ordine", help="Crea un ordine per un cliente")
    p.add_argument("cliente_id", type=int, help="ID del cliente")# add_prod_ordine
    p = sub.add_parser("add_prod_ordine", help="Aggiungi un prodotto a un ordine esistente")
    p.add_argument("ordine_id", type=int, help="ID dell'ordine")
    p.add_argument("prodotto_id", type=int, help="ID del prodotto")
    p.add_argument("quantita", type=int, default=1, nargs="?", help="Quantità (default 1)")

    # list_prodotti
    sub.add_parser("list_prodotti", help="Mostra tutti i prodotti")

    # del_ordine
    p = sub.add_parser("del_ordine", help="Elimina un ordine per ID")
    p.add_argument("ordine_id", type=int, help="ID dell'ordine da eliminare")

    # list_ordini
    sub.add_parser("list_ordini", help="Mostra tutti gli ordini")

    args = parser.parse_args() # analizza gli argomenti della riga di comando cioè li legge e li memorizza in args

    if args.cmd == "add_cliente":
        cliente = crea_cliente(args.nome, args.email)
        print(f"Nuovo cliente: {cliente.id} – {cliente.nome}")

    elif args.cmd == "del_cliente":
        elimina_cliente(args.cliente_id)
        print(f"Cliente eliminato: {args.cliente_id}")

    elif args.cmd == "add_ordine":
        ordine = crea_ordine(args.cliente_id)
        print(f"Nuovo ordine creato: {ordine.id} per cliente {ordine.cliente_id}")

    elif args.cmd == "del_ordine":
        elimina_ordine(args.ordine_id)
        print(f"Ordine eliminato: {args.ordine_id}")

    elif args.cmd == "add_prod_ordine":
        aggiungi_prodotto_a_ordine(args.ordine_id, args.prodotto_id, args.quantita)
        print(f"Aggiunto prodotto {args.prodotto_id} (qty {args.quantita}) all'ordine {args.ordine_id}")

    elif args.cmd == "list_prodotti":
        prodotti = lista_prodotti()
        print("Prodotti disponibili:")
        for p in prodotti:
            print(f"  {p.id}: {p.nome} – {p.prezzo} €")

    elif args.cmd == "del_ordine":
        elimina_ordine(args.ordine_id)
        print(f"Ordine eliminato: {args.ordine_id}")

    elif args.cmd == "list_ordini":
        ordini = lista_ordini()
        if not ordini:
            print("Nessun ordine presente.")
        else:
            for o in ordini:
                print(f"Ordine {o['ordine_id']} | Cliente: {o['cliente']['nome']} ({o['cliente']['id']}) | Data: {o['data']}")
                for it in o["items"]:
                    print(f"  - Prodotto {it['id']}: {it['nome']} x{it['quantita']} @ {it['prezzo']}€")
                print("-" * 40)

if __name__ == "__main__":
    main()