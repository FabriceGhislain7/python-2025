# VERSIONING (**Lavorare senza sovrascrivere il lavoro degli altri.**)

Lavorare senza sovrascrivere il lavoro degli altri in un progetto collaborativo C# (come un’app console con pattern MVC) richiede l'adozione di best practices specifiche per la gestione del codice, in particolare per modelli, controller e viste.

## Best Practices per evitare conflitti

1. Strutturare il progetto in modo modulare
2. Lavorare su file diversi
3. Uso di branch per funzionalità
4. Commit incrementali e descrittivi
5. Aggiornare regolarmente il branch principale

## 1. Strutturare il progetto in modo modulare

**Separazione dei compiti:**

Assegnare specifiche responsabilità ai membri del team.

> Es.: Uno sviluppatore si occupa del modello, un altro del controller, un altro delle viste o dell'output console.

**File separati per componenti:**

Ogni modello, controller o vista dovrebbe avere il proprio file.

> Es.: Non creare un unico file App.cs che contenga tutto il codice. Usa invece:

```bash
Models/
  User.cs
  Product.cs
Controllers/
  UserController.cs
  ProductController.cs
Views/
  ConsoleView.cs
```

## 2. Lavorare su file diversi

Lavorare su file diversi è generalmente preferibile, specialmente se il team sta implementando diverse funzionalità indipendenti.
Questo approccio riduce i conflitti e consente a ciascun membro di lavorare senza dipendere dagli altri.

**Esempio:**

- Dev A lavora su UserController.cs (gestione degli utenti).
- Dev B lavora su ProductController.cs (gestione dei prodotti).

**Vantaggi:**

- Riduce il rischio di conflitti.
- Mantiene il codice leggibile e organizzato.

Ogni sviluppatore è responsabile di un ambito preciso.

## 3. Uso di branch per funzionalità

Adottare un flusso basato sui branch:

**Branch principale:**

- main (codice stabile, pronto per la produzione).
- develop (ultime funzionalità integrate).

**Branch per funzionalità:**

Ogni membro del team crea un branch dedicato per una funzionalità specifica.
bash

```bash
git checkout -b feature/user-management
```

comando rinominare branch (dopo averlo creato con il comando sopra dopo bisogna fare il push del branch)


```bash
git branch -m <nome-vecchio-branch> <nome-nuovo-branch>
```

comando pulisce la cache del branch

```bash
git rm -r --cached .
```

**Esempio:**

- Dev A crea il branch feature/user-management per aggiungere logica di gestione utenti.
- Dev B crea il branch feature/product-management per implementare la gestione prodotti.

## 4. Commit incrementali e descrittivi

Fare commit piccoli e specifici:

```bash
git commit -m "Added User model with basic properties"
git commit -m "Implemented CreateUser method in UserController"
```

Push frequenti per aggiornare il lavoro sul repository remoto.

**Vantaggi:**

- Ogni modifica è chiara e facile da seguire.
- Gli altri sviluppatori possono vedere i tuoi progressi.

## 5. Aggiornare regolarmente il branch principale

Quando lavori su un branch funzionale, assicurati di tenere aggiornato il tuo codice con quello del branch principale (main o develop):

```bash
git checkout feature/user-management
git fetch origin
git merge origin/develop
```

Risolvi i conflitti il prima possibile, evitando problemi più complessi in seguito.

# Processo di Merge dei Contenuti Modificati

Quando tutti hanno completato il lavoro sui propri branch, ecco come procedere per il merge:

**1. Aprire una Pull Request**

Ogni sviluppatore crea una pull request dal proprio branch al branch principale (develop o main).

Le modifiche vengono sottoposte a revisione:

- Controllare che non ci siano duplicazioni di codice.
- Verificare che il codice rispetti le convenzioni del team.

**2. Risoluzione dei conflitti (se lavorate su file simili)**

Se due membri del team hanno lavorato sullo stesso file, Git potrebbe segnalare un conflitto durante il merge.

**Esempio di conflitto:**

File modificato da Dev A (UserController.cs):

```csharp
public void AddUser() {
    // Logica originale
}
```

File modificato da Dev B (UserController.cs):

```csharp
public void AddUser() {
    // Logica ottimizzata
}
```

**Passaggi per risolvere il conflitto:**

> Aprire il file in conflitto: Git indica i conflitti con segnaposti come <<<<<<< e =======.

```csharp
public void AddUser() {
<<<<<<< feature/user-management
    // Logica originale
=======
    // Logica ottimizzata
>>>>>>> feature/product-management
}
```

**Unire manualmente le modifiche: Decidere quale logica mantenere o combinare entrambe.**

```csharp
public void AddUser() {
    // Logica ottimizzata con i miglioramenti di entrambi
}
```

**Confermare la risoluzione:**

```bash
git add UserController.cs
git commit -m "Resolved conflict in UserController.cs"
```

**3. Testare prima del merge finale**

Eseguire i test unitari per assicurarsi che le modifiche non abbiano introdotto bug.
Se possibile, integrare una pipeline CI/CD che esegue automaticamente i test durante il merge.

# COSA FARE SE SI LAVORA SU UNO STESSO FILE

In alcuni casi, può essere necessario lavorare sullo stesso file:

- Piccoli team con stretta collaborazione.
- Parti del file fortemente interdipendenti (es.: una funzione complessa che richiede input da più sviluppatori).

**Best Practices in questo caso:**

- Comunicare chiaramente i cambiamenti al team.
- Utilizzare strumenti di pairing programming o code review.
- Evitare di lavorare contemporaneamente sullo stesso metodo o blocco di codice.

**Strumenti e Workflow Consigliati**

Git:

Usare git stash per salvare temporaneamente il lavoro in corso.

CI/CD:

Automatizzare i test per verificare l’integrità del codice durante i merge.

Code Review:

Assicurarsi che ogni merge sia rivisto da almeno un altro membro del team.

Seguendo queste pratiche, il tuo team sarà in grado di collaborare efficacemente, minimizzando i conflitti e garantendo un codice di alta qualità.

Per approfondire il versioning con più persone in un contesto C# con MVC, è utile esplorare scenari comuni che si adattano alla gestione di team e allo sviluppo collaborativo.

----------------------------------------------------------------------------------------------------------------------------

# Git Stash

git stash è un comando che consente di salvare temporaneamente le modifiche non committate nel tuo repository Git senza applicarle direttamente al branch.

È utile per:

- Passare a un altro branch senza dover committare modifiche incomplete.
- Salvare il lavoro in corso per risolvere un conflitto o aggiornare il branch.
- Mantenere pulito il tuo storico di commit.

Quando esegui git stash, le modifiche vengono salvate in un'area speciale (lo stash), permettendoti di recuperarle in seguito.

Comandi di Base di Git Stash

**Salvare le modifiche nello stash**

```bash
git stash
```

Salva tutte le modifiche (tracked e staged).

Per includere file non tracciati:

```bash
git stash -u
```

**Elencare gli stash salvati**

```bash
git stash list
```

**Applicare uno stash salvato**

```bash
git stash apply
```

**Applica le modifiche salvate nello stash più recente (non rimuove lo stash dallo stack).**

Per applicare uno specifico stash:

```bash
git stash apply stash@{2}
```

**Rimuovere uno stash dallo stack**

Dopo averlo applicato:

```bash
git stash drop
```

**Cancellare tutti gli stash**

```bash
git stash clear
```

# Quando Usare Git Stash

1. Passare a un altro branch

Se hai modifiche non committate e devi cambiare branch:

```bash
git stash
git checkout another-branch
```

Dopo aver lavorato sul nuovo branch, torna indietro e applica lo stash:

```bash
git checkout original-branch
git stash pop
```

# 2. Risolvere un conflitto durante il merge

Se hai modifiche locali ma devi aggiornare il tuo branch con le ultime modifiche dal remoto:

```bash
git stash
git pull origin main
git stash pop
```

Se ci sono conflitti, Git te lo segnalerà e potrai risolverli manualmente.

# 3. Pulire il workspace

Quando vuoi ripulire temporaneamente l'area di lavoro per fare altre operazioni (es.: test di un altro branch), senza perdere le modifiche in corso:

```bash
git stash
```

**Esegui le operazioni necessarie**

```bash
git stash pop
```

**Best Practices per l'uso di Git Stash**

Dai nomi chiari ai tuoi stash Quando salvi uno stash, specifica un messaggio descrittivo per identificare facilmente le modifiche:

```bash
git stash save "WIP: Adding login functionality"
```

**Usa stash solo per lavoro temporaneo**

- Non trattare lo stash come un luogo permanente per memorizzare le modifiche.
- Fai commit delle modifiche appena sono pronte o importanti per evitare di perderle accidentalmente.
- Applica solo stash rilevanti Prima di applicare uno stash, verifica cosa contiene:

```bash
git stash show -p stash@{0}
```

Non abusare di stash con file non tracciati Se possibile, traccia i file prima di stoccarli nello stash.

> Usare git stash -u frequentemente può complicare la gestione dei file.

Verifica lo stato dopo il pop Dopo aver usato git stash pop, controlla sempre l'output per accertarti che non ci siano conflitti o errori.

Mantieni un ambiente pulito Dopo aver risolto un conflitto o applicato uno stash, elimina quelli non più necessari per evitare confusione:

```bash
git stash drop
```

Includi test locali prima di stoccare modifiche Se possibile, esegui test sulle modifiche prima di stoccarle nello stash. Evita di riprendere codice parzialmente funzionante senza testarlo.

**Esempio Pratico di Uso**

Scenario:

Stai lavorando su un controller (UserController.cs) e hai modificato alcune logiche. Ti viene chiesto di passare rapidamente a un altro branch per risolvere un bug urgente.

Stash delle modifiche in corso:

```bash
git stash save "WIP: Updated UserController logic"
```

Passa al branch del bugfix:

```bash
git checkout hotfix/fix-null-exception
```

Risolvi il bug, committa e torna al tuo lavoro:

```bash
git commit -m "Fixed null reference in Login"
git checkout feature/update-user-controller
```

Recupera le modifiche salvate:

```bash
git stash pop
```

Continua il lavoro e committa:

```bash
git commit -m "Completed updates to UserController"
```

----------------------------------------------------------------------------------------------------------------------------

# SCENARI DI VERSIONING

## Scenario 1:

Creazione di una nuova funzionalità in un branch separato

**Situazione:**

Stai lavorando con il team su una nuova funzionalità per l'app, come la gestione degli utenti.

**Passi:**

**Crea un nuovo branch:** Ogni sviluppatore crea un branch con un nome descrittivo, come feature/user-management.

**Sviluppo isolato:**

Gli sviluppatori lavorano sui propri branch, evitando di toccare il codice principale (branch main o develop).

**Commit frequenti:**

Ogni sviluppatore esegue commit frequenti per tracciare i cambiamenti, collegando i commit a task specifici.

> comandi git
```bash
# crea un nuovo branch
git branch feature/user-management
# passa al branch appena creato
git checkout feature/user-management
# crea un nuovo branch e passa a esso
git checkout -b feature/user-management
# aggiungi i file modificati
git add . o git add --all
# esegui il commit delle modifiche
git commit -m "Implement user registration"
# esegui le modifiche sul branch principale
git push origin feature/user-management
```

## Scenario 2:

Merge di un branch di funzionalità

**Situazione:**

Dopo aver completato la funzionalità, è necessario unire il branch nel main o develop.

**Passi:**

Pull Request (PR): Lo sviluppatore apre una PR dal branch feature/user-management verso develop.

**Code Review:**

Il team esegue una revisione del codice per assicurarsi che rispetti gli standard di qualità e non ci siano bug evidenti.

**Risoluzione dei conflitti:**

Se altri sviluppatori hanno modificato la stessa area del codice, potrebbero esserci conflitti che vanno risolti manualmente prima del merge.

**Merge:** Dopo la review e i test, il branch viene unito nel develop.

**Passaggi per eseguire il merge:**
- Vai sul branch principale (main)
- Prima di tutto, assicurati di essere sul branch in cui desideri unire le modifiche, cioè il main.

```bash
git checkout main
```

**Aggiorna il branch main**
- Assicurati che il branch main sia aggiornato con l'ultima versione dei file. Questo comando recupera gli aggiornamenti remoti e li integra nel tuo branch.

```bash
git pull origin main
```

**Unisci il branch features/test nel branch main**
- Ora che sei nel branch main, puoi eseguire il merge del branch features/test.

```bash
git merge features/test
```
Se non ci sono conflitti, il merge sarà completato automaticamente e vedrai un messaggio di successo.
Se ci sono conflitti, Git ti segnalerà i file che devono essere risolti manualmente.

 conflitti (se necessari)
Se ci sono conflitti, dovrai risolverli manualmente aprendo i file segnalati, cercando i segnaposto di conflitto (<<<<, ====, >>>>), e decidendo quali modifiche mantenere.

Dopo aver risolto i conflitti:

```bash
git add <nome_file_conflittato>
```
**Poi conferma il merge:**

```bash
git commit
```
**Spingere le modifiche verso il repository remoto**
- Una volta completato il merge, invia le modifiche al repository remoto.

```bash
git push origin main
```
**Riepilogo comandi:**
```bash
git checkout main
git pull origin main
git merge features/test
```
# Risolvi i conflitti se presenti
```bash
git add <nome_file_conflittato>
git commit
git push origin main
```

> comandi git
```bash
# passa al branch develop
git checkout develop
# esegui il merge del branch feature/user-management
git merge feature/user-management
# push delle modifiche sul branch develop
git push origin develop
```

## Scenario 3:

Gestione di bugfix su un'app in produzione

**Situazione:**

Un bug viene rilevato nell'ambiente di produzione e deve essere risolto urgentemente, mentre altri sviluppatori stanno lavorando su nuove funzionalità.

**Passi:**

Creazione di un hotfix branch: Crea un branch hotfix/bugfix-name partendo dal branch main o master.

**Risoluzione del bug:**

Lavora sul bug in isolamento dal lavoro di sviluppo corrente.

**Test del fix:**

Una volta risolto, esegui i test necessari per verificare che la correzione funzioni senza introdurre nuovi bug.

**Merge in main:**

Il branch hotfix viene fuso nel branch principale (main) e immediatamente distribuito.

**Merge in develop:**

L'hotfix viene poi unito nel branch develop per mantenere la coerenza tra i branch.

> comandi git
```bash
# crea un nuovo branch hotfix
git checkout -b hotfix/bugfix-name
# esegui il merge del branch hotfix in main
git checkout main
git merge hotfix/bugfix-name
# push delle modifiche sul branch main
git push origin main
# esegui il merge del branch hotfix in develop
git checkout develop
git merge hotfix/bugfix-name
# push delle modifiche sul branch develop
git push origin develop
```

## Scenario 4:

Lavoro su un feature toggle per nuove funzionalità

**Situazione:**

Stai sviluppando una funzionalità che non è ancora pronta per essere distribuita, ma vuoi che sia inclusa nel codice principale per facilitare l'integrazione futura.

**Passi:**

**Creazione di un feature branch:**

Crea un branch per la nuova funzionalità (feature/nuova-funzionalità).

**Implementazione di un feature toggle:**

Usa un toggle per disattivare la funzionalità incompleta nel codice, in modo che possa essere distribuita senza essere visibile all'utente.

**Merge nel main:**

Una volta terminata la parte stabile della funzionalità, puoi fare un merge del branch nel develop, ma la funzionalità rimane nascosta grazie al toggle.

**Attivazione del feature toggle:**

Quando la funzionalità è completa e pronta per essere distribuita, basta attivare il toggle.

> comandi git
```bash
# crea un nuovo branch per la funzionalità
git checkout -b feature/nuova-funzionalità
# esegui il merge del branch feature in develop
git checkout develop
git merge feature/nuova-funzionalità
# push delle modifiche sul branch develop
git push origin develop
```

## Scenario 5:

Release con branch separati per ogni versione

**Situazione:**

Il team vuole mantenere separati i branch di sviluppo e quelli di release, per avere versioni stabili dell'app in produzione.

**Passi:**

Creazione di un branch di release: Quando la funzionalità è pronta per essere distribuita, crea un branch release/v1.0 partendo dal branch develop.

**Stabilizzazione e test:**

Esegui gli ultimi test e correzioni su questo branch.

**Merge in main:**

Quando il branch di release è stabile, effettua il merge nel branch main.

**Tag della versione:**

Crea un tag per la versione rilasciata (v1.0), così da poter tornare a questa versione in futuro, se necessario.

> comandi git
```bash
# crea un nuovo branch di release
git checkout -b release/v1.0
# esegui il merge del branch release in main
git checkout main
git merge release/v1.0
# crea un tag per la versione rilasciata
git tag v1.0
# push delle modifiche sul branch main
git push origin main
# push del tag
git push origin v1.0
```

## Best Practices:

**Commit frequenti e descrittivi:**

Usa messaggi di commit chiari che descrivano cosa è stato fatto.

**Code Review e automazione:**

Esegui code review e integra test automatici per evitare errori.

**Comunicazione:**

Mantieni il team aggiornato sui progressi e sulle decisioni di merge per evitare conflitti inattesi.

Questi scenari aiutano a comprendere come gestire in modo efficace il versioning e la collaborazione su un progetto MVC in C#.