# Nessun import richiesto

class Inventario:
    def __init__(self):
        self.oggetti = []
    
    def aggiungi(self, oggetto):
        self.oggetti.append(oggetto)

    def usa_oggetto(self, nome_oggetto, utilizzatore, bersaglio=None):
        for oggetto in self.oggetti:
            if oggetto.nome == nome_oggetto:
                oggetto.usa(utilizzatore, bersaglio)
                self.oggetti.remove(oggetto)
                return
        print(f"{utilizzatore.nome} non ha un oggetto chiamato {nome_oggetto}.")
        
    def prendi_inventario(self, altro_personaggio):
        if altro_personaggio.inventario.oggetti:
            print(f"\n{self.nome} ottiene l'inventario di {altro_personaggio.nome}:")
            for oggetto in altro_personaggio.inventario.oggetti:
                print(f" - {oggetto.nome}")
                self.inventario.aggiungi(oggetto)
            altro_personaggio.inventario.oggetti.clear()
        else:
            print(f"{altro_personaggio.nome} non aveva oggetti nell'inventario.")