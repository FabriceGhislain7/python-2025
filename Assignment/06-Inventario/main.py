def vedi_inventario(inventario):
    for prodotto, dati in inventario.items():
        quantita, prezzo = dati
        print(f"{prodotto}: {quantita} pezzi - €{prezzo:.2f} ciascuno")

def aggiorna_inventario(inventario, prodotto, quantita, prezzo_unitario):
    if prodotto in inventario:
        inventario[prodotto][0] += quantita
        inventario[prodotto][1] = prezzo_unitario
    else:
        inventario[prodotto] = [quantita, prezzo_unitario]

# Inventario iniziale
inventario = {
    "mele": [10, 0.20],
    "banane": [5, 0.15],
    "pere": [8, 0.18],
    "fragole": [20, 0.22]
}

# Menù principale
azione = input("Vuoi [V]edere o [A]ggiornare l'inventario? ").upper()

if azione == "V":
    print("\n--- Inventario Attuale ---")
    vedi_inventario(inventario)

elif azione == "A":
    prodotto = input("Nome prodotto: ").lower()
    quantita = int(input("Quantità da aggiungere: "))
    prezzo_unitario = float(input("Prezzo unitario (€): "))
    
    aggiorna_inventario(inventario, prodotto, quantita, prezzo_unitario)
    
    print("\nInventario aggiornato:")
    vedi_inventario(inventario)

else:
    print("Azione non valida.")
