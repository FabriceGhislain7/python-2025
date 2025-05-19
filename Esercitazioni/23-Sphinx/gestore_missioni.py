from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import random
    from missioni.missione import Missione
    from ambienti.ambiente import Vulcano,Foresta,Palude
    from personaggi.classi import Mago, Guerriero, Ladro
    from oggetti.oggetto import Oggetto, PozioneCura, BombaAcida, Medaglione

#Lista delle missioni
class GestoreMissioni:
    """
    E' un gestore di istanze della classe Missione , e le gestisce con diversi metodi
    """

    def __init__(self)->None:
        #La proprietà principale di Missioni sarà una lista di oggetti Missione
        self.lista_missioni = self.setup()

    def setup(self)->list['Missione']:
        """
        Istanzio le Missioni da fornire al GestoreMissioni
        """
         #Istanzio le missioni
        imboscata = Missione("Imboscata", Foresta(), [Guerriero("Robin Hood"), Guerriero("Little Jhon")], [PozioneCura(),PozioneCura(),BombaAcida()])
        salva_principessa = Missione("Salva la principessa", Palude(),[Ladro("Megera furfante")],[Medaglione()])
        culto = Missione("Sgomina il culto di Graz'zt sul vulcano Gheemir", Vulcano(),[Mago("Cultista"), Mago("Cultista"), Mago("Cultista")],[PozioneCura(),Medaglione()])
        return [imboscata, salva_principessa, culto]

    def mostra(self)->None:
        """
        Mostra le missioni disponibili
        """
        print("Missioni disponibili:")
        for missione in self.lista_missioni:
            print(f"-{missione.nome}")
        #print(f"-{indx}  {missione.nome}" for indx, missione in enumerate(self.lista_missioni, start=1) if not missione.completata)

    def finita(self)->bool:
        """
        Controlla se in Missioni ci sono ancora missioni non completate in
        tal caso ritorna False, se tutte le missioni sono state completate
        ritorna True
        """
        esito = True
        for missione in self.lista_missioni :
            if missione.completata == False :
                esito = False
        return esito

    def sorteggia(self)->Missione:
        """
        Sorteggia una missione a caso tra quelle non completate in missioni e
        la ritorna , se non ci sono missioni non copletate ritorna False.
        """
        random.shuffle(self.lista_missioni)
        for missione in self.lista_missioni :
            if not missione.completata :
                return missione
        #Se non ci sono missioni che non siano state completate
        raise ValueError("Non ci sono missioni non completate")
