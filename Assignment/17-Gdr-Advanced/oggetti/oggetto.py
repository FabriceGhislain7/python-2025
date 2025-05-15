# Nessun import richiesto

class Oggetto:
    def __init__(self, nome, tipo="neutro"):
        self.nome = nome
        self.tipo = tipo
        self.usato = False

    def usa(self, utilizzatore, bersaglio=None):
        raise NotImplementedError("Questo oggetto non ha effetto definito.")

class PozioneCura(Oggetto):
    def __init__(self, nome="Pozione Rossa", valore=30):
        super().__init__(nome, tipo="curativo")
        self.valore = valore
        self.tipo = "curativo"
        
    def usa(self, utilizzatore, bersaglio=None, ambiente=None):
        base = self.valore
        if ambiente:
            valore_effettivo = ambiente.modifica_cura(base)
        else:
            valore_effettivo = base

        target = bersaglio if bersaglio else utilizzatore
        target.salute = min(target.salute + valore_effettivo, target.salute_max)
        print(f"{target.nome} usa {self.nome} e recupera {valore_effettivo} salute!")
        self.usato = True

class BombaAcida(Oggetto):
    def __init__(self, nome="Bomba Acida", danno=30):
        super().__init__(nome)
        self.danno = danno
        self.tipo = "offensivo"

    def usa(self, utilizzatore, bersaglio=None, ambiente=None):
        if bersaglio is None:
            print(f"{utilizzatore.nome} cerca di usare {self.nome}, ma non ha un bersaglio!")
            return

        danno = self.danno
        if ambiente:
            danno = ambiente.modifica_danno(danno)

        bersaglio.subisci_danno(danno)
        print(f"{utilizzatore.nome} lancia {self.nome} su {bersaglio.nome}, infliggendo {danno} danni!")
        self.usato = True

class Medaglione(Oggetto):
    def __init__(self):
        super().__init__("Medaglione")
        self.tipo = "offensivo"

    def usa(self, utilizzatore, bersaglio=None, ambiente=None):
        target = bersaglio if bersaglio else utilizzatore
        target.attacco_max += 10
        print(f"{target.nome} indossa {self.nome} e aumenta il suo attacco massimo di 10!")
        self.usato = True
