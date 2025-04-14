import json

# 01 LETTURA DI UN FILE JSON  
"""  
{  
    "nome": "nome1",  
    "cognome": "cognome1",  
    "eta": 20  
}  
"""  
path = "test.json"  # File JSON nella stessa directory  
with open(path, "r") as file:   # r = read
    obj = json.load(file)  # Deserializza il file JSON  
print(f"nome: {obj['nome']} cognome: {obj['cognome']} eta: {obj['eta']}")  # obj indica il file JSON

# 02 LETTURA DI UN FILE JSON CON PIÙ LIVELLI  
"""  
{  
    "nome": "nome1",  
    "cognome": "cognome1",  
    "eta": 20,  
    "indirizzo": {  
        "via": "via roma",  
        "citta": "roma"  
    }  
}  
"""  
path2 = "test2.json"  
with open(path2, "r") as file:  
    obj2 = json.load(file)  
print(f"nome: {obj2['nome']} cognome: {obj2['cognome']} eta: {obj2['eta']} via: {obj2['indirizzo']['via']} citta: {obj2['indirizzo']['citta']}")

# 03 LETTURA DI UN FILE JSON COMPLESSO  
"""  
{  
    "nome": "Nome1 Cognome1",  
    "eta": 30,  
    "impiegato": true,  
    "indirizzo": {  
      "via": "Via Roma 10",  
      "citta": "Roma",  
      "CAP": "00100"  
    },  
    "numeriditelefono": [  
      {"tipo": "casa", "numero": "1234-5678"},  
      {"tipo": "ufficio", "numero": "8765-4321"}  
    ],  
    "lingueparlate": ["italiano", "inglese", "spagnolo"],  
    "sposato": false,  
    "patente": null  
}  
"""  
path3 = "test3.json"  
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

# 04 SCRITTURA DI UN OGGETTO JSON  
obj4 = {  
    "nome": "Mario Rossi",  
    "eta": 30,  
    "impiegato": True,  
    "indirizzo": {  
        "via": "Via Roma 10",  
        "citta": "Roma",  
        "CAP": "00100"  
    },  
    "numeriditelefono": [  
        {"tipo": "casa", "numero": "1234-5678"},  
        {"tipo": "ufficio", "numero": "8765-4321"}  
    ],  
    "lingueparlate": ["italiano", "inglese", "spagnolo"],  
    "sposato": False,  
    "patente": None  
}  
with open("test4.json", "w") as file:  
    json.dump(obj4, file, indent=4)  # Serializza con formattazione leggibile dump permette di scrivere su file indent =4 indica il numero di spazi per la formattazione

# 05 AGGIUNTA DI UN OGGETTO A UN FILE JSON  
path5 = "test4.json"  
with open(path5, "r") as file:  
    obj5 = json.load(file)

# Aggiunta di un nuovo numero di telefono  
obj5["numeriditelefono"].append({"tipo": "mobile", "numero": "555-6789"})  
with open(path5, "w") as file:  
    json.dump(obj5, file, indent=4)

# 06 CANCELLAZIONE DI UN ELEMENTO DA UN FILE JSON  
path6 = "test4.json"  
with open(path6, "r") as file:  
    obj6 = json.load(file)

# Rimozione di una lingua parlata  
obj6["lingueparlate"].remove("inglese")  
with open(path6, "w") as file:  
    json.dump(obj6, file, indent=4)

# 07 MODIFICA DI UN ELEMENTO IN UN FILE JSON  
path7 = "test4.json"  
with open(path7, "r") as file:  
    obj7 = json.load(file)

# Modifica del nome  
obj7["nome"] = "Giovanni Rossi"  
with open(path7, "w") as file:  
    json.dump(obj7, file, indent=4)

# 08 CREAZIONE DI UN FILE JSON DA UN DIZIONARIO  
dizionario = {  
    "nome": "Mario",  
    "cognome": "Rossi"  
}  
with open("test8.json", "w") as file:  
    json.dump(dizionario, file, indent=4)  

# 09 LETTURA DI UNA LISTA JSON  
"""  
[  
    {
    "nome": "Nome1",
    "cognome": "Cognome1"
    },  
    {
    "nome": "Nome2",
    "cognome": "Cognome2"
    },  
    {
    "nome": "Nome3",
    "cognome": "Cognome3"
    }  
]  
"""
path9 = "test9.json"
with open(path9, "r") as file:  
    lista = json.load(file)  # Deserializza la lista JSON
for elemento in lista:
    print(f"nome: {elemento['nome']} cognome: {elemento['cognome']}")  # Stampa ogni elemento della lista

# 10 CREAZIONE DI UNA LISTA JSON
lista2 = [  
    {"nome": "Mario", "cognome": "Rossi"},  
    {"nome": "Giovanni", "cognome": "Bianchi"},  
    {"nome": "Luca", "cognome": "Verdi"}  
]
with open("test10.json", "w") as file:  
    json.dump(lista2, file, indent=4)  # Serializza la lista JSON
# 11 AGGIUNTA DI UN ELEMENTO A UNA LISTA JSON
path11 = "test10.json"
with open(path11, "r") as file:  
    lista3 = json.load(file)  # Deserializza la lista JSON
# Aggiunta di un nuovo elemento alla lista
lista3.append({"nome": "Marco", "cognome": "Neri"})
with open(path11, "w") as file:  
    json.dump(lista3, file, indent=4)  # Serializza la lista JSON
# 12 RIMOZIONE DI UN ELEMENTO DA UNA LISTA JSON
path12 = "test10.json"
with open(path12, "r") as file:  
    lista4 = json.load(file)  # Deserializza la lista JSON
# Rimozione di un elemento dalla lista
lista4.remove({"nome": "Giovanni", "cognome": "Bianchi"})
with open(path12, "w") as file:  
    json.dump(lista4, file, indent=4)  # Serializza la lista JSON
# 13 MODIFICA DI UN ELEMENTO IN UNA LISTA JSON
path13 = "test10.json"
with open(path13, "r") as file:  
    lista5 = json.load(file)  # Deserializza la lista JSON
# Modifica di un elemento nella lista
for elemento in lista5:
    if elemento["nome"] == "Mario":
        elemento["cognome"] = "Verdi"
with open(path13, "w") as file:
    json.dump(lista5, file, indent=4)  # Serializza la lista JSON