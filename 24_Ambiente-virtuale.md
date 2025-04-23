# Ambiente virtuale

Un ambiente virtuale in Python è uno strumento che consente di creare un'area isolata per il tuo progetto, separata dal sistema Python globale. Questo è particolarmente utile per gestire le dipendenze del progetto e garantire che ogni progetto utilizzi esattamente le librerie di cui ha bisogno, senza conflitti con altre configurazioni o progetti.

### **Vantaggi di un ambiente virtuale**

1. **Isolamento delle dipendenze**  
   * Ogni progetto ha il proprio set di pacchetti Python installati.  
   * Puoi utilizzare versioni diverse della stessa libreria in progetti diversi senza che ci siano conflitti.  
   * Non sovrascrivi le librerie globali di Python sul sistema.

2. **Facilità di gestione delle versioni delle librerie**  
   * Puoi bloccare una specifica versione di una libreria necessaria al progetto, evitando aggiornamenti indesiderati che potrebbero introdurre problemi di compatibilità.

3. **Evita conflitti tra progetti**  
   * Progetti diversi possono richiedere librerie con versioni incompatibili. L'uso di ambienti virtuali elimina questo problema, poiché ogni progetto ha la propria configurazione indipendente.

4. **Portabilità del progetto**  
   * Puoi utilizzare un file requirements.txt per elencare tutte le dipendenze del progetto. Questo file può essere condiviso con altri sviluppatori per ricreare l'ambiente virtuale su un altro sistema.

5. **Compatibilità con il sistema operativo**  
   * L'ambiente virtuale evita di alterare la configurazione di Python installata a livello di sistema, riducendo il rischio di compromettere il funzionamento di altri software.

6. **Pulizia del sistema**  
   * Senza un ambiente virtuale, l'installazione di librerie globalmente può "sporcare" il sistema e occupare spazio con pacchetti non necessari.

---

### **Come funziona un ambiente virtuale?**

Quando attivi un ambiente virtuale:

* Python utilizza i pacchetti installati in una directory locale al progetto invece di quelli installati globalmente.

* Le librerie vengono installate nella cartella dell'ambiente virtuale (di solito chiamata venv) e non interferiscono con altri ambienti.

---

### **Quando usare un ambiente virtuale?**

* **Sempre**, quando lavori su progetti Python. È una buona pratica per mantenere il tuo sistema pulito e il progetto facilmente gestibile.

---

### **Come si crea e usa un ambiente virtuale?**

**Creazione**  
Esegui questo comando nella directory del tuo progetto:  
```bash  
python -m venv venv  
```

Questo creerà una directory chiamata venv che contiene l'ambiente virtuale.

**Attivazione**

Su Windows:  
```bash  
venv\Scripts\activate  
```

Su macOS/Linux:  
```bash  
source venv/bin/activate  
```

**Installazione delle dipendenze**  
Dopo l'attivazione, puoi installare le librerie necessarie usando pip, ad esempio:  
```bash  
pip install numpy pandas  
```

**Disinstallazione delle dipendenze**
Per disinstallare una libreria, usa:  
```bash
pip uninstall nome_libreria  
```

**Aggiornamento delle dipendenze**

**Disattivazione**  
Una volta terminato, disattiva l'ambiente con:  
```bash  
deactivate  
```

**Creazione di un file requirements.txt**  
Per salvare le dipendenze del progetto, usa:  
```bash  
pip freeze > requirements.txt  
```

**Ricreazione di un ambiente virtuale**  
Su un altro sistema, puoi ricreare l'ambiente con:  
```bash  
python -m venv venv  
source venv/bin/activate   # su mac o linux
venv\Scripts\activate  # su windows
pip install -r requirements.txt  
```

Gli ambienti virtuali sono essenziali per lavorare su progetti Python professionali, specialmente in team o per progetti a lungo termine.