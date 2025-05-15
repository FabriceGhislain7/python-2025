class Missione:
    def __init__(self, nome, ambienti, oggetti_iniziali=None, nemici=None, premio=None, descrizione=""):
        self.nome = nome
        self.ambienti = ambienti
        self.oggetti_iniziali = oggetti_iniziali or []
        self.nemici = nemici or []
        self.premio = premio
        self.descrizione = descrizione
        self.tornei_vinti = 0
        self.completata = False

    def registra_vittoria(self):
        self.tornei_vinti += 1
        print(f"Torneo vinto! ({self.tornei_vinti}/3)")
        if self.tornei_vinti >= 3:
            self.completata = True
            print(f"\nMissione '{self.nome}' completata!")
            if self.premio:
                print(f"Hai ottenuto il premio: {self.premio.nome}")

    def get_ambiente_random(self):
        import random
        return random.choice(self.ambienti)

    def __str__(self):
        info = f"{self.nome}"
        if self.descrizione:
            info += f"{self.descrizione}"
        info += f"Tornei richiesti: 3 - Completati: {self.tornei_vinti}"
        if self.premio:
            info += f"\nPremio finale: {self.premio.nome}"
        return info