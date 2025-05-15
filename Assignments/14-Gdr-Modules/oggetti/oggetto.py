# Nessun import richiesto

class Oggetto:
    def __init__(self, nome):
        self.nome = nome
        self.usato = False

    def usa(self, utilizzatore, bersaglio=None):
        raise NotImplementedError("Questo oggetto non ha effetto definito.")

class PozioneCura(Oggetto):
    def __init__(self, nome="Pozione Rossa", valore=30):
        super().__init__(nome)
        self.valore = valore

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.salute = min(target.salute + self.valore, target.salute_max)
        print(f"{target.nome} usa {self.nome} e recupera {self.valore} salute!")
        self.usato = True

class BombaAcida(Oggetto):
    def __init__(self, nome="Bomba Acida", danno=30):
        super().__init__(nome)
        self.danno = danno

    def usa(self, utilizzatore, bersaglio=None):
        if bersaglio is None:
            print(f"{utilizzatore.nome} cerca di usare {self.nome}, ma non ha un bersaglio!")
            return
        bersaglio.subisci_danno(self.danno)
        print(f"{utilizzatore.nome} lancia {self.nome} su {bersaglio.nome}, infliggendo {self.danno} danni!")
        self.usato = True

class Medaglione(Oggetto):
    def __init__(self):
        super().__init__("Medaglione")

    def usa(self, utilizzatore, bersaglio=None):
        target = bersaglio if bersaglio else utilizzatore
        target.attacco_max += 10
        print(f"{target.nome} indossa {self.nome}, aumentando il suo attacco massimo!")
        self.usato = True