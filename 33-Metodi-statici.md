# METODI STATICI
- I metodi statici sono metodi che appartengono a una classe piuttosto che a un'istanza di essa.
- Possono essere chiamati senza creare un'istanza della classe.
- Vengono definiti utilizzando il decoratore `@staticmethod`.
- I metodi statici non possono accedere a `self` o `cls`, quindi non possono modificare lo stato dell'oggetto o della classe.
- Sono utili per raggruppare funzioni che hanno una logica comune ma non necessitano di accedere a dati specifici dell'istanza o della classe.
- Possono essere utilizzati per creare funzioni di utilità che non dipendono dallo stato dell'oggetto o della classe.
- I metodi statici possono essere chiamati direttamente sulla classe o su un'istanza della classe.

> @staticmethod = funzione dentro una classe, ma senza self e cls

## Uso della classe statica nel GDR (InterfacciaUtente)
- Creazione di un interfaccia utente
- I metodi come chiedi_input, chiedi_numero, conferma non hanno bisogno di dati dell'utente (self)
- Sono solo funzioni di utilità
- Sono meglio organizzati dentro una classe (InterfacciaUtente) piuttosto che sparsi ovunque

## Quando usare @staticmethod
- Quando vuoi creare una funzione utile collegata a una classe, ma che non ha bisogno di sapere nulla:
- né sull'istanza (self)
- né sulla classe (cls)

Serve solo per organizzazione, chiarezza e ordine
