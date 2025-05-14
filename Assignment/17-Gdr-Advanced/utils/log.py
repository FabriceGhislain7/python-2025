from datetime import datetime

class Log:
    def __init__(self):
        self.eventi = []

    def registra(self, messaggio):
        timestamp = datetime.now().strftime("%H:%M:%S")
        voce = f"[{timestamp}] {messaggio}"
        self.eventi.append(voce)
        print(voce)  # opzionale: stampa a schermo in tempo reale

    def mostra(self):
        print("\nRegistro eventi:")
        for evento in self.eventi:
            print(" -", evento)

    def salva_su_file(self, filename="registro.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for evento in self.eventi:
                f.write(evento + "\n")
        print(f"\nRegistro salvato su file: {filename}")