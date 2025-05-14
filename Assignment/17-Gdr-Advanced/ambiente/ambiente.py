class Ambiente:
    """Classe che rappresenta un ambiente di gioco, con modificatori e oggetti vietati."""
    def __init__(self, nome, modificatori=None, oggetti_vietati=None, descrizione=""):
        self.nome = nome
        self.descrizione = descrizione
        self.modificatori = modificatori or {}  # es: {"cura": -0.2, "danno": +0.1}
        self.oggetti_vietati = oggetti_vietati or []  # es: ["Pozione Rossa"]

    def modifica_cura(self, base_cura):
        """Modifica la cura in base all'ambiente."""
        fattore = self.modificatori.get("cura", 0)
        return int(base_cura * (1 + fattore))

    def modifica_danno(self, base_danno):
        """Modifica il danno in base all'ambiente."""
        fattore = self.modificatori.get("danno", 0)
        return int(base_danno * (1 + fattore))

    def oggetto_consentito(self, nome_oggetto):
        """Controlla se l'oggetto è vietato nell'ambiente."""
        return nome_oggetto not in self.oggetti_vietati

    def __str__(self):  # __str__ e un __repr__ per la rappresentazione dell'oggetto cioè per la stampa
        """Restituisce una stringa che rappresenta l'ambiente."""
        descr = f"Ambiente: {self.nome}"
        if self.descrizione:
            descr += f" - {self.descrizione}"
        if self.modificatori:
            modifiche = [f"{chiave}: {int(val*100)}%" for chiave, val in self.modificatori.items()]
            descr += "\n Modificatori: " + ", ".join(modifiche)
        if self.oggetti_vietati:
            descr += "\n Oggetti vietati: " + ", ".join(self.oggetti_vietati)
        return descr
    
def ambienti_standard():
    """Restituisce una lista di ambienti standard."""
    return [
        Ambiente(
            nome="Vulcano",
            modificatori={"danno": 0.2, "cura": -0.3},
            oggetti_vietati=["Pozione Blu"],
            descrizione="Un luogo rovente. Le cure sono meno efficaci, i danni aumentano."
        ),
        Ambiente(
            nome="Foresta",
            modificatori={"cura": 0.2},
            descrizione="La natura aiuta la rigenerazione. Le cure sono più efficaci."
        ),
        Ambiente(
            nome="Palude",
            modificatori={"danno": -0.2},
            oggetti_vietati=["Bomba Acida"],
            descrizione="Un terreno viscido. I danni fisici sono ridotti."
        )
    ]