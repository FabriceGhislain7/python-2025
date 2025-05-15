# TECNICHE DI VERSIONING

## creazione di un branch "develop"

Comandi:
```
git checkout -b develop
```
Il comando ha creato un branch "develop" e ci ha spostato su di esso. Ora possiamo lavorare su questo branch senza influenzare il branch principale (main).
> Il branch develop e in locale, quindi non è visibile su GitHub. Per renderlo visibile dobbiamo fare un push.
```
git push origin develop
```
## eliminazione di un branch
Comandi:
```
git branch -d nome_branch
```
Il comando elimina il branch "nome_branch" in locale. Se vogliamo eliminare anche il branch su GitHub dobbiamo usare:
```
git push origin --delete nome_branch
```
## guardare i branch
Comandi:
```
git branch
```
Il comando mostra i branch in locale. Se vogliamo vedere anche i branch remoti dobbiamo usare:
```
git branch -r
```
## passare da un branch all'altro
Comandi:
```
git checkout nome_branch
```
## creazione di un branch in "develop"
Comandi:
```
git checkout -b nome_branch develop
```
Il comando crea un branch "nome_branch" a partire dal branch "develop" e ci sposta su di esso. Ora possiamo lavorare su questo branch senza influenzare il branch develop.
Il brach e in locale, quindi non è visibile su GitHub. Per renderlo visibile dobbiamo fare un push.
```
git push origin nome_branch
```
## pulizia della cache del branch
Comandi:
```
git fetch --prune
```

Il comando pulisce la cache del branch. Se vogliamo pulire anche il branch su GitHub dobbiamo usare:
```
git gc
```
## unione di un branch in "develop"
Comandi:
```
git checkout develop
git merge nome_branch
```
Il comando unisce il branch "nome_branch" in "develop". Ora possiamo eliminare il branch "nome_branch" se non ci serve più.
```
git branch -d nome_branch
```
## unione di un branch in "main"
Comandi:
```
git checkout main
git merge nome_branch
```
Il comando unisce il branch "nome_branch" in "main". Ora possiamo eliminare il branch "nome_branch" se non ci serve più.
## fare il pull di un branch
Comandi:
```
git pull origin nome_branch
```
Il comando fa il pull del branch "nome_branch" da GitHub. Se vogliamo fare il pull di un branch remoto dobbiamo usare:
```
git pull origin nome_branch:branch_remoto
```
## fare il pull di un branch su un altro branch
Comandi:
```
git pull origin nome_branch
```
## verificare la struttura dei branch
Comandi:
```
git log --oneline --graph --decorate --all
```
Il comando mostra la struttura dei branch in locale. Se vogliamo vedere anche i branch remoti dobbiamo usare:
```
git log --oneline --graph --decorate --all --remotes
```
> premere "q" per uscire
## verificare tramite l editor grafico
Comandi:
```
gitk --all
```
# verificare se un branch e stato generato da un altro
Vuoi sapere se feature-x è stato creato da develop? Fai così:
Comandi:
```
git merge-base feature develop
```