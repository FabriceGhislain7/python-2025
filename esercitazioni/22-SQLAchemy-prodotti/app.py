import argparse
from crud import (create_product, elimina_cliente, crea_ordine, elimina_ordine, lista_prodotti, lista_clienti)

# Lo scopo del metodo di lavoro 

def main():
    parser = argparse.ArgumentParser(description="App CRUD SQLAlchemy")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("add_cliente", help="Crea un nuovo cliente")
    p.add_argument("nome", help="Nome del cliente")
    p.add_argument("email", help="Email del cliente")

    if args.cmd == "add_cliente":
        cliente = create_cliente(args.nome, args.email)
        print(f"Nuovo cliente: {cliente.id} - {cliente.nome}")

if __name__ == "__main__":
    main()
