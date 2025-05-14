# Nessun import richiesto

def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")

def mostra_ambiente(ambiente=None):
    if ambiente:
        print("\n=== Condizioni Ambientali ===")
        print(str(ambiente))
        print("=============================")
        
def mostra_missione(missione=None):
    if missione:
        print("\n=== Missione ===")
        print(str(missione))
        print("================")