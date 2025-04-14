
Il  dove ogni conttato è rapresentato da un file json separato.
Ogni file json deve contenere le seguenti informazioni:
```json
{
    "nome": "Nome1",
    "cognome": "Cognome1",
    "telefono": [
        {
            "tipo": "casa",
            "numero": "2478382394"
        },
        {
            "tipo": "cellulare",
            "numero": "351838000"
        }
    ],
    "attivo": true,
    "attivita": ["programatore", "web deseign", "Custumer care"],
    "note": "Note1"
}
``` 
Deve essere presente una cartella chiamata `contatti` nella quale deve essere inserite i file json.
- Gli utenti devono poter:
    . aggiungere un conttato.
    - Modificare un contatto
    - Eliminare un contatto
    - Visualizzare i contatti attivi
 Deve essere presente il file README.md con il floatchart