# CLASSI - DESERIALIZZAZIONE

Le classi possono essere utilizzate per la serializzazione e deserializzazione di oggetti in Python.

```python  
import json

# Classe Prodotto per rappresentare ogni prodotto  
class Prodotto:  
    def __init__(self, id, nome_prodotto, prezzo_prodotto, giacenza_prodotto):  
        self.id = id  
        self.nome_prodotto = nome_prodotto  
        self.prezzo_prodotto = prezzo_prodotto  
        self.giacenza_prodotto = giacenza_prodotto

    # Metodo per rappresentare l'oggetto come dizionario (utile per la serializzazione)  
    def to_dict(self):  
        return {  
            "id": self.id,  
            "nome_prodotto": self.nome_prodotto,  
            "prezzo_prodotto": self.prezzo_prodotto,  
            "giacenza_prodotto": self.giacenza_prodotto  
        }

    # Metodo per creare un oggetto Prodotto da un dizionario (utile per la deserializzazione)  
    @staticmethod  
    def from_dict(data):  
        return Prodotto(  
            id=data["id"],  
            nome_prodotto=data["nome_prodotto"],  
            prezzo_prodotto=data["prezzo_prodotto"],  
            giacenza_prodotto=data["giacenza_prodotto"]  
        )

# Funzione principale  
def main():  
    # Creare una lista di prodotti  
    prodotti = [  
        Prodotto(1, "Prodotto A", 10.50, 100),  
        Prodotto(2, "Prodotto B", 20.75, 50)  
    ]

    # Serializzare i dati in un file JSON  
    file_path = "prodotti.json"  
    prodotti_dict = [prodotto.to_dict() for prodotto in prodotti]  
    with open(file_path, "w") as file:  
        json.dump(prodotti_dict, file, indent=4)  
    print(f"Dati serializzati e salvati in {file_path}:\n{json.dumps(prodotti_dict, indent=4)}\n")

    # Deserializzare i dati dal file JSON  
    with open(file_path, "r") as file:  
        read_json_data = json.load(file)

    prodotti_deserializzati = [Prodotto.from_dict(data) for data in read_json_data]  
    print("Dati deserializzati:")  
    for prodotto in prodotti_deserializzati:  
        print(f"ID: {prodotto.id}, Nome: {prodotto.nome_prodotto}, Prezzo: {prodotto.prezzo_prodotto}, Giacenza: {prodotto.giacenza_prodotto}")

# Esecuzione della funzione principale  
if __name__ == "__main__":   # Questo controlla se il file è eseguito come script principale (entry point)
    main()   # Esegue la funzione principale in modo da poter essere importato in altri script
```

### **Adattamenti specifici:**

1. **Classe Prodotto**:  
   * Utilizza il costruttore __init__ per definire le proprietà.  
   * Metodo to_dict() per convertire un oggetto in un dizionario, necessario per la serializzazione.  
   * Metodo statico from_dict() per creare un oggetto Prodotto da un dizionario durante la deserializzazione.  
2. **Serializzazione**:  
   * Usa json.dump() per scrivere i dati su file e json.dumps() per visualizzare i dati in formato leggibile in console.  
3. **Deserializzazione**:  
   * Usa json.load() per leggere i dati JSON e trasforma ogni dizionario in un oggetto Prodotto con from_dict().  
4. **Output**:  
   * I dati serializzati e deserializzati sono mostrati in console per verifica