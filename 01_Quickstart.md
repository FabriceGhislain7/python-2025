# QUICKSTART

### **Python in Visual Studio Code \- Quickstart**

Per utilizzare Python in Visual Studio Code, segui questi passaggi:

1. **Assicurati di aver installato Python sul tuo computer**  
   Puoi scaricare l'ultima versione di Python dal sito ufficiale:  
   [https://www.python.org/downloads](https://www.python.org/downloads)  
2. **Installa Visual Studio Code sul tuo computer**  
   Puoi scaricarlo dal sito ufficiale di Visual Studio Code:  
   [https://code.visualstudio.com/](https://code.visualstudio.com/)  
3. **Configura Visual Studio Code per lavorare con Python**  
   * Apri Visual Studio Code.  
   * Vai al menu "Extensions" sulla sinistra (icona dei quadratini).  
   * Cerca e installa l'estensione "Python" sviluppata da Microsoft.  
     Quest'estensione fornisce funzionalità essenziali come IntelliSense, debugging, e la gestione degli ambienti virtuali.

### **Estensioni consigliate per Python**

Ecco alcune estensioni utili per lavorare con Python in Visual Studio Code:

* **Python** (di Microsoft):  
  Questa è l'estensione principale per Python. Fornisce funzionalità come il supporto per IntelliSense, il debugging, la gestione degli ambienti virtuali e l'integrazione con strumenti di linting e formattazione.  
* **Pylance**:  
  Offre un supporto avanzato per IntelliSense, con analisi del codice più veloce e migliore esperienza di completamento del codice.  
* **Python Docstring Generator**:  
  Genera automaticamente commenti e documentazione Python per le funzioni e le classi seguendo lo standard di docstring desiderato.  
* **Jupyter**:  
  Questa estensione consente di lavorare con file .ipynb (notebook Jupyter) direttamente in Visual Studio Code, utile per data analysis e machine learning.  
* **Black Formatter**:  
  Uno strumento di formattazione automatica per il codice Python. Aiuta a mantenere uno stile di codifica uniforme.  
* **Flake8**:  
  Uno strumento di linting per identificare errori e migliorare lo stile del codice Python.  
* **isort**:  
  Riordina automaticamente gli import in base alle convenzioni di Python.  
* **Python Test Explorer**:  
  Consente di eseguire e visualizzare i risultati dei test unitari direttamente in Visual Studio Code.

### **Primi passi con Python in Visual Studio Code**

**Apri un terminale** e digita:  
```bash  
python3 --version  
```
Se Python è installato, vedrai la versione stampata nel terminale. Se non è installato o desideri aggiornarlo:  
```bash  
sudo apt update  
sudo apt install python3 python3-pip
```
### **Passo 2: Installare PIP**

PIP è il gestore di pacchetti per Python, che ti permetterà di installare e gestire le librerie Python. Se non è già installato:

```bash  
sudo apt install python3-pip
```
### **Passo 3: Installare le Librerie Python**

In base al tipo di progetto che intendi sviluppare, potresti aver bisogno di diverse librerie. Per esempio, se lavori su un progetto di data science, potresti aver bisogno di pandas e NumPy. Per installare librerie Python, usa pip3:

```bash  
pip3 install nome_lib
```
Esempi comuni includono:

**Flask** per applicazioni web:  
```bash  
pip3 install flask
```
**Requests** per fare richieste HTTP:  
```bash  
pip3 install requests
```
**Pandas** per l'analisi dei dati:  
```bash  
pip3 install pandas
```
**NumPy** per il calcolo numerico:  
```bash  
pip3 install numpy
```
**Matplotlib** per grafici:  
```bash  
pip3 install matplotlib
```
### **Passo 4: Configurare l'ambiente di sviluppo in VS Code**

Quando lavori con Python in VS Code, è una buona pratica configurare un ambiente virtuale per ogni progetto. Questo consente di gestire le dipendenze in modo isolato. Ecco come puoi configurare un ambiente virtuale sul tuo Raspberry Pi:

**Crea un ambiente virtuale**:  
```bash  
python3 -m venv myenv
```
1. myenv è il nome della cartella per l'ambiente virtuale.  
2. **Attiva l'ambiente virtuale**:

Su Linux:  
```bash  
source myenv/bin/activate
```
3. Ora sei nell'ambiente virtuale e puoi installare le librerie che saranno isolate da altre installazioni.  
4. **Configura VS Code per usare l'interprete dell'ambiente virtuale**:  
   * Apri la Command Palette (Ctrl+Shift+P).  
   * Digita e seleziona "Python: Select Interpreter".  
   * Scegli l'interprete che si trova nel tuo ambiente virtuale, di solito si trova sotto myenv/bin/python.