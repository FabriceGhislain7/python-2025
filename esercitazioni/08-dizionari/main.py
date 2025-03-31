# Dizionario da due liste.
# Obiettivo: Creare un dizionario da due liste.
chiavi = ["nome", "cognome", "eta"]
valori = ["Nome 1", "Cognome 1", 25]

persona = dict(zip(chiavi, valori)) # Crea una lista di tuple con zip e poi crea un dizionario con dict
# Stampa il dizionario
print(persona) # Output: {'nome': 'Nome 1', 'cognome': 'Cognome 1', 'eta': 25}

# Raggruppa elementi in base a una proprietà comune.
# Obiettivo: Raggruppare gli elementi per la loro prima lettura.
nomi = ["Anna", "Alberto", "Marco", "Maria", "Luigi"] 
# Crea un dizionario vuoto
gruppi = {}
for nome in nomi:
    # Prendi la prima lettera del nome
    prima_lettera = nome[0].upper()
    # Aggiungi il dizionario sotto la chiave della prima lettera
    if prima_lettera not in gruppi: # Se non esiste già la chiave, perché deve essere unica.
        gruppi[prima_lettera] = [] # Inizializza una lista vuota per la chiave
    gruppi[prima_lettera].append(nome)

print(gruppi) # Output: {'A': ['Anna', 'Alberto'], 'M': ['Marco', 'Maria'], 'L': ['Luigi']}
# Puoi accedere agli elementi del dizionario usando la chiave.
gruppi["A"] # Output: ['Anna', 'Alberto']
# oppure un nome specifico della lista 
print(gruppi["A"][0]) # Output: Anna

# Trova la chiave con il valore minimo.
dati = {"Partecipante 1": 10, 
        "Partecipante 2": 5, 
        "Partecipante 3": 8}
# Trova la chiave con il valore minimo
minimo = min(dati, key=dati.get) # Restituisce la chiave con il valore minimo
print(minimo) # Output: Partecipante 2

# Rubrica telefonica.
# Obiettivo: Creare una rubrica telefonica.
rubrica = {
    "Partecipante 1": "123456789",
    "Partecipante 2": "987654321",
    "Partecipante 3": "555555555"
}

# Stampa la rubrica
print(rubrica) # Output: {'Partecipante 1': '123456789', 'Partecipante 2': '987654321', 'Partecipante 3': '555555555'}
# Chiede all'utente di inserire un nome.
nome = input("Inserisci il nome del partecipante: ")
# Verifica se il nome è presente nella rubrica.
if nome in rubrica:
    print(f"Il numero di tellefono {nome} è {rubrica[nome]}") 
else:
    print(f"{nome} non è presente nella rubrica.")

# Voti degli studenti 
# Obiettivo: Creare un dizionario per memorizzare i voti degli studenti e calcolare la media.
studenti = {
    "Studente 1": [8, 9, 7],
    "Studente 2": [6, 7, 8],
    "Studente 3": [9, 10, 9]
}

print(studenti) # Output: {'Studente 1': [8, 9, 7], 'Studente 2': [6, 7, 8], 'Studente 3': [9, 10, 9]}

for studente, voti in studenti.items():
    media = sum(voti) / len(voti) # Calcola la media dei voti
    print(f"La media di {studente} è {media:.2f}") # Stampa la media con due decimali
    
