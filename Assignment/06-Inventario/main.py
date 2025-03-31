inventario = { 
    "mele": 10,
    "banane": 5,
    "pere": 8,
    "ciliegie": 15,
    "fragole": 20
}
azione = input("Vuoi [V]edere o [A]ggiornare l'inventario? ")

if azione == "V":
    for prodotto, quantita in inventario.items():
        print(f"{prodotto}: {quantita}")
elif azione == "A":
    prodotto = input("Nome prodotto: ")
    quantita = int(input("Quantità da aggiungere: "))
    if prodotto in inventario:
        inventario[prodotto] += quantita
    else:
        inventario[prodotto] = quantita  # oppure posso fare # inventario.setdefault(prodotto, 0) # inventario[prodotto] += quantita
    # stampa l inventario aggiornato
    print("Inventario aggiornato")
    for prodotto, quantita in inventario.items():
        print(f"{prodotto}: {quantita}")
else:
    print("Azione non valida.")