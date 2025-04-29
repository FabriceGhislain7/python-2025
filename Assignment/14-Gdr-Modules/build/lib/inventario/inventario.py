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
        
    def prendi_inventario(self, altro_inventario):
        if altro_inventario.oggetti:
            print(f"\n{self.nome} ottiene l'inventario di {altro_inventario.nome}:")
            for oggetto in altro_inventario.oggetti:
                print(f" - {oggetto.nome}")
                self.aggiungi(oggetto)
            altro_inventario.oggetti.clear()
        else:
            print(f"{altro_inventario.nome} non aveva oggetti nell'inventario.")