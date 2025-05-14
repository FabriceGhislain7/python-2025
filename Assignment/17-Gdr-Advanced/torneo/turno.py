# gli oggetti vengono aggiunti all'inventario del giocatore nel turno
from utils.interfaccia import InterfacciaUtente
from utils.log import Log

class Turno:
    def __init__(self, giocatore, nemico, ambiente=None):
        self.giocatore = giocatore
        self.nemico = nemico
        self.numero_turno = 1
        self.ambiente = ambiente

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
            
            # Log
            log = Log()

            # Mostra inventario
            self.mostra_inventario()

            # Chiedi se vuole usare un oggetto prima di attaccare
            if self.giocatore.inventario.oggetti:
                usa = InterfacciaUtente.conferma("Vuoi usare un oggetto prima di attaccare?")
                if usa:
                    numero = InterfacciaUtente.chiedi_input(
                        "Scegli un oggetto da usare (inserisci il numero): ",
                        opzioni=[str(i) for i in range(1, len(self.giocatore.inventario.oggetti) + 1)]
                    )
                    oggetto = self.giocatore.inventario.oggetti[int(numero) - 1]

                    # Determina il bersaglio
                    if oggetto.tipo == "curativo":
                        bersaglio = self.giocatore
                    elif oggetto.tipo == "offensivo":
                        bersaglio = self.nemico
                    else:
                        bersaglio = None

                    # Usa l'oggetto
                    self.giocatore.inventario.usa_oggetto(oggetto.nome, self.giocatore, bersaglio, ambiente=self.ambiente)
                    

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
            
            # Log
            log.registra(f"{self.giocatore.nome} attacca {self.nemico.nome}")
            log.salva_su_file()

            self.numero_turno += 1
