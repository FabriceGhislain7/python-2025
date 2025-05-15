# Setup.py
# Perché è meglio installare il tuo progetto con pip install . invece di copiare i file manualmente?

- Separi codice sorgente dal codice installato
- Verifichi che il pacchetto funziona come un vero modulo Python
- Eviti errori strani tipo "sta ancora usando i file locali"
- È la pratica standard usata anche su GitHub e PyPI
- Sei pronto se vuoi pubblicarlo o condividerlo

Situazione | Azione consigliata
---|---
Stai ancora sviluppando il codice | Lavori dentro progetto/
Vuoi testare l'installazione reale | Crei cartella test/, fai pip install ../progetto/ dentro l'env