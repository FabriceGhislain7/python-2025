# 🔄 Sincronizzare il proprio repository con quello del docente

Questa guida mostra come aggiornare la tua branch `main` con le ultime modifiche del docente, **senza sovrascrivere o perdere il tuo lavoro**.

---

## ✅ 0. Aggiungere il repository remoto del docente (una sola volta)

```bash
git remote add docente https://github.com/NOME-UTENTE-DEL-DOCENTE/NOME-REPO-DEL-DOCENTE.git
````

> Puoi verificare che sia stato aggiunto con:

```bash
git remote -v
```

---

## ✅ 1. Scaricare gli aggiornamenti del docente

```bash
git fetch docente
```

---

## ✅ 2. Creare una branch basata sul `main` del docente

```bash
git checkout -b docente-update docente/main
```

> Ora sei su una branch `docente-update` che contiene **esattamente il lavoro aggiornato del docente**.

---

## ✅ 3. Tornare sulla propria branch `main`

```bash
git checkout main
```

---

## ✅ 4. Unire gli aggiornamenti del docente nella propria branch

```bash
git merge docente-update
```

> ⚠️ Se ci sono **conflitti**, Git li segnalerà. Risolvili manualmente, poi esegui:

```bash
git add .
git commit
```

---

## ✅ 5. (Facoltativo) Pubblicare la propria branch `main` aggiornata su GitHub

```bash
git push origin main
```

---

## 🧠 Riepilogo comandi

| Azione                             | Comando                                       |
| ---------------------------------- | --------------------------------------------- |
| Aggiungi il remoto del docente     | `git remote add docente URL_DEL_DOCENTE`      |
| Scarica aggiornamenti              | `git fetch docente`                           |
| Crea branch con il codice del prof | `git checkout -b docente-update docente/main` |
| Torna alla tua branch `main`       | `git checkout main`                           |
| Unisci aggiornamenti               | `git merge docente-update`                    |
| Risolvi conflitti (se ci sono)     | `git add . && git commit`                     |
| Pusha su GitHub (facoltativo)      | `git push origin main`                        |

---
