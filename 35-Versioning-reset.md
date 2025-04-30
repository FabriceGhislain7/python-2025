# Ripristinare commit

## L'area di staging

### Per capire come funziona bisogna avere chiaro il concetto di area di staging

L'**area di staging** (detta anche "index") in Git è una sorta di "zona intermedia" dove vengono preparate le modifiche prima di essere confermate (committed). È una delle tre aree principali del flusso di lavoro di Git, che include:

1. **Working Directory** (Directory di lavoro):  
   Qui ci sono i tuoi file attuali, cioè i file su cui stai lavorando.  
2. **Staging Area** (Area di staging):  
   Un'area temporanea dove specifichi quali modifiche vuoi includere nel prossimo commit.  
3. **Repository**:  
   La cronologia dei commit salvata in modo permanente.

---

### **Come funziona l'area di staging?**

1. **Modifica i file nella directory di lavoro**:  
   Quando modifichi un file, questo rimane nella working directory, ed è considerato **non tracciato o modificato** fino a quando non lo aggiungi allo staging.

**Aggiungi i file all'area di staging**:  
Quando decidi che un file o un gruppo di modifiche sono pronti per essere salvati (committed), li aggiungi all'area di staging usando:  
```bash  
git add <file>  
```  
Oppure, per aggiungere tutte le modifiche:  
```bash  
git add .  
```

2. **Commit**:  
   Quando esegui il comando git commit, tutte le modifiche presenti nell'area di staging vengono salvate nel repository come un nuovo commit.

---

### **Perché esiste l'area di staging?**

L'area di staging offre flessibilità, permettendoti di:

* **Selezionare solo alcune modifiche** da includere nel commit, lasciando altre fuori.  
* **Preparare commit organizzati**, includendo solo le modifiche pertinenti.  
* **Gestire in modo chiaro il flusso di lavoro**, evitando di commettere accidentalmente file non pronti.

---

### **Comandi utili per l'area di staging**

**Mostrare lo stato attuale (modifiche tracciate e non):**  
```bash  
git status  
```

**Visualizzare cosa c’è nello staging:**  
```bash  
git diff --cached  
```

**Rimuovere un file dallo staging senza cancellare le modifiche:**  
```bash  
git reset <file>  
```

**Aggiungere tutte le modifiche al prossimo commit:**  
```bash  
git add .  
```

---

## Ripristinare commit

### **1\. Ripristinare un commit (soft reset)**

Se vuoi ripristinare il tuo progetto a uno stato specifico **senza perdere le modifiche successive (mantenerle nello staging)**:

```bash  
git reset --soft <commit-hash>  
```

* Questo sposta il branch al commit specificato.  
* Le modifiche dei commit successivi rimarranno nell'area di staging.

---

### **2\. Ripristinare un commit (mixed reset)**

Se vuoi ripristinare a uno stato specifico, **annullando i commit successivi ma mantenendo le modifiche non tracciate**:

```bash  
git reset --mixed <commit-hash>  
```

* I file modificati rimangono nella working directory (non nello staging).

---

### **3\. Ripristinare un commit (hard reset)**

Se vuoi ripristinare il repository a uno stato specifico **perdendo tutte le modifiche successive (attenzione: irreversibile)**:

```bash  
git reset --hard <commit-hash>  
```

* Questo annulla tutti i commit successivi e cancella le modifiche locali.

---

### **4\. Creare un nuovo commit che annulla un commit specifico**

Se hai bisogno di **annullare le modifiche di un commit specifico ma mantenerle tracciate nella cronologia**, usa revert:

```bash  
git revert <commit-hash>  
```

* Questo crea un nuovo commit che annulla le modifiche del commit specificato.  
* Utile per ambienti condivisi.

---

### **5\. Tornare temporaneamente a un commit (detached HEAD)**

Se vuoi semplicemente tornare a uno stato passato, senza modificare il branch attuale:

```bash  
git checkout <commit-hash>  
```

* Questo sposta la HEAD sul commit selezionato, senza cambiare la cronologia del branch.  
* Ricorda che non puoi fare commit permanenti in questo stato senza creare un nuovo branch.

---

### **Trovare il commit hash**

Per identificare il commit che vuoi ripristinare, usa:

```bash  
git log  
```

* Ti verranno mostrati tutti i commit con hash, autore, data e messaggi.

---

### **Salvare le modifiche prima del ripristino (opzionale)**

Se non sei sicuro del risultato, salva le modifiche attuali con uno stash prima del ripristino:

```bash  
git stash  
```

Dopo il reset, puoi recuperare le modifiche con:  
```bash  
git stash apply  
```  
---

### **Esempio pratico**

1. Modifichi tre file: file1.txt, file2.txt, file3.txt.

Decidi che solo file1.txt e file3.txt sono pronti per essere salvati. Quindi:  
```bash  
git add file1.txt file3.txt  
```

2 Ora file1.txt e file3.txt sono nello staging, ma file2.txt no.

Esegui il commit:  
```bash  
git commit -m "Aggiunto file1 e file3"  
```

4. Il commit include solo file1.txt e file3.txt, mentre file2.txt rimane nella directory di lavoro.

