import random
def mostra_benvenuto():
    print("Benvenuto ne gioco di combattimento!")

def crea_personaggio(nome):
    personaggio = {
        "nome": nome,
        "salute": 100,
        "attacco_min": 10,
        "attacco_max": 20
    }
    return personaggio

def esegui_attacco(attacante, difensore):
    danno = random.randint(attacante["attacco_min"], difensore("attacco_max"))

# Stamapa il messaggio di benvenuto
nome1 = input("Inserisci il nome del tuo personaggio: ")
perso1 = crea_personaggio(nome1)
