# gli oggetti vengono aggiunti all'inventario del giocatore nel turno
from utils.interfaccia import InterfacciaUtente

class Turno:
    def __init__(self, giocatore, nemico):
        self.giocatore = giocatore
        self.nemico = nemico
        self.numero_turno = 1

    def mostra_inventario(self):
        print("\n--- Inventario ---")
        if not self.giocatore.inventario.oggetti:
            print("Inventario vuoto.")
        else:
            for idx, oggetto in enumerate(self.giocatore.inventario.oggetti, 1):
                print(f"{idx}) {oggetto.nome}")
        print("-------------------")

    def esegui(self):
        while True:
            print(f"\n--- Turno {self.numero_turno} ---")

            # Mostra inventario
            self.mostra_inventario()

            # Chiedi se vuole usare un oggetto prima di attaccare
            if self.giocatore.inventario.oggetti:
                usa = InterfacciaUtente.conferma("Vuoi usare un oggetto prima di attaccare?")
                if usa:
                    nomi_oggetti = [oggetto.nome for oggetto in self.giocatore.inventario.oggetti]
                    oggetto_scelto = InterfacciaUtente.chiedi_input(
                        "Quale oggetto vuoi usare? Scrivi il nome esatto: ",
                        opzioni=nomi_oggetti
                    )
                    self.giocatore.inventario.usa_oggetto(oggetto_scelto, self.giocatore, self.nemico)

            # Attacco normale
            self.giocatore.attacca(self.nemico)

            if self.nemico.sconfitto():
                print(f"Hai vinto contro {self.nemico.nome}!")
                self.giocatore.recupera_hp()
                self.giocatore.inventario.usa_oggetto("Pozione Rossa", self.giocatore)
                self.giocatore.prendi_inventario(self.nemico)
                break

            # Azioni del nemico
            self.nemico.attacca(self.giocatore)

            if self.giocatore.sconfitto():
                print(f"Sei stato sconfitto da {self.nemico.nome}!")
                break

            self.numero_turno += 1