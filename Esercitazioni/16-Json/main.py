import json

# LETTURA

path = "test.json"  # File JSON nella stessa directory
with open(path, "r") as file:   # r = read
    obj = json.load(file)  # Deserializza il file JSON
print(f"nome: {obj['nome']} cognome: {obj['cognome']} eta: {obj['eta']}")  # obj indica il file JSON

path2 = "test-multilevel.json"
with open(path2, "r") as file:
    obj2 = json.load(file)
print(f"nome: {obj2['nome']} cognome: {obj2['cognome']} eta: {obj2['eta']} via: {obj2['indirizzo']['via']} citta: {obj2['indirizzo']['citta']}")    

path3 = "test-complex.json"
with open(path3, "r") as file:  
    obj3 = json.load(file)
    
# 1 livello (dizionario)
print(f"nome: {obj3['nome']} eta: {obj3['eta']} impiegato: {obj3['impiegato']}")  
# 2 livello (dizionario)
print(f"via: {obj3['indirizzo']['via']} citta: {obj3['indirizzo']['citta']} CAP: {obj3['indirizzo']['CAP']}")  
# 3 livello (lista di dizionari)
print(f"tipo: {obj3['numeriditelefono'][0]['tipo']} numero: {obj3['numeriditelefono'][0]['numero']}")  
# 3 livello (lista)
print(f"lingua: {obj3['lingueparlate'][0]}")  
# 1 livello (booleani e null)
print(f"sposato: {obj3['sposato']} patente: {obj3['patente']}")

# SCRITTURA

with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)  # Serializza con formattazione leggibile dump permette di scrivere su file indent =4 indica il numero di spazi per la formattazione
    
# Aggiunta di un nuovo numero di telefono (aggiungere un dizionario alla lista)
obj3["numeriditelefono"].append({"tipo": "cellulare", "numero": "1234567890"})
# scrivo il file
with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)
    
# rimuovere un elemento (lista)
# obj3["lingueparlate"].remove("inglese")  
# scrivo il file
with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)
# provare a rimuovere un elemento che non esiste da errore ValueError: list.remove(x): x not in list
# quindi posso usare il try except
try:
    obj3["lingueparlate"].remove("inglese")
except ValueError:
    print("Elemento non trovato nella lista", obj3["lingueparlate"])
# scrivo il file
with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)
    
# modificare un elemento (dizionario)
obj3["eta"] = 30
# scrivo il file
with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)

# modificare un elemento (dizionario)
obj3["indirizzo"]["via"] = "Via Roma"
# scrivo il file
with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)

# modificare un elemento (dizionario nella lista)
obj3["numeriditelefono"][0]["numero"] = "0987654321"
# scrivo il file
with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)
    
# modificare un elemento (lista)
obj3["lingueparlate"][0] = "italiano"
# scrivo il file
with open("test-complex.json", "w") as file:  
    json.dump(obj3, file, indent=4)
    
# CREARE UN JSON PARTENDO DA UN DIZIONARIO
# creo un dizionario
dizionario = {
    "nome": "Nome1",
    "cognome": "Cognome1",
    "eta": 30,
    "indirizzo": {
        "via": "Via Roma",
        "citta": "Roma",
        "CAP": "00100"
    }
}
with open("test-creato.json", "w") as file:
    json.dump(dizionario, file, indent=4)  # Serializza il dizionario in un file JSON
    
# LETTURA DI UNA LISTA DI DIZIONARI
path4 = "test-struttura.json"
with open(path4, "r") as file:  
    obj4 = json.load(file)
for elemento in obj4:
    print(f"nome: {elemento['nome']} cognome: {elemento['cognome']}")  # obj4 è una lista di dizionari