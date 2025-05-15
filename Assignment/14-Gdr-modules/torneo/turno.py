# gli oggetti vengono aggiunti all'inventario del giocatore nel turno
from oggetti.oggetto import PozioneCura, BombaAcida, Medaglione

class Turno:
    def __init__(self, giocatore, nemico):
        self.giocatore = giocatore
        self.nemico = nemico
        self.numero_turno = 1

    def esegui(self):
        while True:
            print(f"--- Turno {self.numero_turno} ---")

            # Azioni del giocatore
            self.giocatore.inventario.aggiungi(PozioneCura())
            self.giocatore.inventario.aggiungi(BombaAcida())
            self.giocatore.inventario.aggiungi(Medaglione())

            # Usa bomba acida contro il nemico
            self.giocatore.inventario.usa_oggetto("Bomba Acida", self.giocatore, self.nemico)
            self.giocatore.attacca(self.nemico)
            print("Storico danni subiti dal nemico:", self.nemico.storico_danni_subiti)

            if self.nemico.sconfitto():
                print(f"Hai vinto contro {self.nemico.nome}!")
                self.giocatore.recupera_hp()
                self.giocatore.inventario.usa_oggetto("Pozione Rossa", self.giocatore)
                
                # Prendi l'inventario del nemico
                self.giocatore.prendi_inventario(self.nemico)
                
                break

            # Azioni del nemico
            self.nemico.attacca(self.giocatore)
            print("Storico danni subiti dal giocatore:", self.giocatore.storico_danni_subiti)

            if self.giocatore.sconfitto():
                print(f"Sei stato sconfitto da {self.nemico.nome}!")
                break

            self.numero_turno += 1