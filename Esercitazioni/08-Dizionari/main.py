# Dizionario da due liste
# Obiettivo: Crea un dizionario da due liste
chiavi = ["nome", "cognome", "eta"]
valori = ["Nome 1", "Cognome 1", 25]
persona = dict(zip(chiavi, valori))  # zip() crea una lista di tuple, dict() converte in dizionario mentre dict crea un dizionario
# Stampa il dizionario
print(persona)  # Output: {'nome': 'Nome 1', 'cognome': 'Cognome 1', 'eta': 25} 

# Raggruppa elementi in base a una proprietà
# Obiettivo: Raggruppare elementi per la loro prima lettera
nomi = ["Anna", "Alberto", "Marco", "Maria", "luigi"]
# Crea un dizionario vuoto
gruppi = {}
for nome in nomi:
    # Ottieni la prima lettera del nome
    prima_lettera = nome[0].upper()
    # Aggiungi il nome al dizionario sotto la chiave della prima lettera
    if prima_lettera not in gruppi: # se non esiste la chiave perche deve essere unica
        gruppi[prima_lettera] = [] # crea una lista vuota dato che non esiste
    gruppi[prima_lettera].append(nome) # aggiungi il nome alla lista
# Stampa il dizionario
print(gruppi)  # Output: {'A': ['Anna', 'Alberto'], 'M': ['Marco', 'Maria'], 'L': ['luigi']}
# posso accedere ad un valore del dizionario tramite la chiave
print(gruppi["A"])  # Output: ['Anna', 'Alberto']
# oppure ad un elemento specifico della lista
print(gruppi["A"][0])  # Output: 'Anna'

# Trova la chiave con il valore minimo
dati = {
    "Partecipante 1": 10,
    "Partecipante 2": 5,
    "Partecipante 3": 8
    }
# Trova la chiave con il valore minimo
minimo = min(dati, key=dati.get) # .get() restituisce il valore associato alla chiave
# Stampa la chiave con il valore minimo
print(minimo)  # Output: 'Partecipante 2'

# Rubrica Telefonica
# Obiettivo: Salvare e cercare numeri di telefono in base al nome della persona (chiedi all’utente un nome e stampa il numero di telefono)
rubrica = {
    "Partecipante 1": "1234567890",
    "Partecipante 2": "0987654321",
    "Partecipante 3": "1122334455"
}
# Stampa la rubrica
print(rubrica.keys())  # Output: dict_keys(['Partecipante 1', 'Partecipante 2', 'Partecipante 3'])
# Chiedi all'utente di inserire un nome
nome = input("Inserisci il nome del partecipante: ")
# Verifica se il nome è presente nella rubrica
if nome in rubrica:
    print(f"Il numero di telefono di {nome} è: {rubrica[nome]}")
else:
    print(f"{nome} non è presente nella rubrica.")
    
# Voti degli studenti
# Obiettivo: Creare un dizionario per memorizzare i voti degli studenti e calcolare la media
studenti = {
    "Studente 1": [8, 9, 7],
    "Studente 2": [6, 7, 8],
    "Studente 3": [9, 10, 8]
}
for studente, voti in studenti.items(): # uso studenti.items ed non studenti perche voglio sia le chiavi che i valori
    media = sum(voti) / len(voti)  # Calcola la media dei voti (sum() calcola la somma e len() restituisce il numero di elementi)
    print(f"La media dei voti di {studente} è: {media}")