inventario = {
    "mele": [10, 0.20],
    "banane": [5, 0.15],
    "pere": [8, 0.18],
    "ciliegie": [15, 0.25],
    "fragole": [20, 0.22]
}

azione = input("Vuoi [V]edere o [A]ggiornare l'inventario? ").upper()

if azione == "V":
    for prodotto, dati in inventario.items():
        quantita, prezzo = dati  # dati è una lista con [quantità, prezzo]
        print(f"{prodotto}: {quantita} pezzi - €{prezzo:.2f} ciascuno")

elif azione == "A":
    prodotto = input("Nome prodotto: ").lower()
    quantita = int(input("Quantità da aggiungere: "))
    prezzo_unitario = float(input("Prezzo unitario (€): "))

    if prodotto in inventario:
        inventario[prodotto][0] += quantita  # aggiorna la quantità con [prodotto][0] dove 0 è la quantità
        inventario[prodotto][1] = prezzo_unitario  # sovrascrive il prezzo
    else:
        inventario[prodotto] = [quantita, prezzo_unitario]

    print("Inventario aggiornato:")
    for prodotto, dati in inventario.items():
        quantita, prezzo = dati
        print(f"{prodotto}: {quantita} pezzi - €{prezzo:.2f} ciascuno")

else:
    print("Azione non valida.")