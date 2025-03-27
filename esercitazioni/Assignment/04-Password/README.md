# GENERATORE PASSWORD (V 1.0) 

Creare un programma che genera una password sicura basata sui seguiti criteri:
 - La lunghezza della password deve essere compesa tra 8 e 12 caratteri. 
 - La password deve contenere almeno:
   - 1 lettera maioscola
   - 1 lettera minoscola
   - 1 numero
   - 1 carattere specile (Es: @, #, !, ecc.)  

La password generata non deve contenere spazi.

## Suggerimenti
 - usa la classe random in modo da generare caratteri casuali. 
 - puoi creare gruppi di caratteri (lettere minuscole, maiuscole, numeri, e caratteri speciali) e selezionare manualmente un carattere da ciascun gruppo

Puoi utilizzare il modulo 'string' in modo a generare i caratteri da selezionare casualmente
```python

import string

alfabeto_minuscole = string.ascii_lowercase
alfabeto_maiuscole = string.ascii_uppercase
numeri = string.digits
caratteri_speciali = string.punctuation

```
## Implementazione 
```python 

# Import 
import string
import random

# Generiamo le liste per ogni categoria di caratteri.
lettere_minuscole = string.ascii_lowercase
lettere_maiuscole = string.ascii_uppercase
numeri = string.digits
caratteri_speciali = string.punctuation

# Tutti i caratteri
tutti_caratteri = lettere_maiuscole + lettere_minuscole + numeri + caratteri_speciali

# Inizializzo la password
password = []

# Genero casualmente la lunghezza della password tra 8 e 12
lunghezza_password = random.randint(8, 12)

# Aggiungo un carattere per gruppo
password.append(random.choice(lettere_maiuscole))
password.append(random.choice(lettere_minuscole))
password.append(random.choice(numeri))
password.append(random.choice(caratteri_speciali))

while len(password) < lunghezza_password + 1:
    password.append(random.choice(tutti_caratteri))

random.shuffle(password)
password = "".join(password)

print(f"Lunghezza della password generata: {lunghezza_password}")
print(f"La password generata è: {password}")

```
# GENERATORE PASSWORD (V 2.0) 

Creare un programma che genera una password sicura basata sui precedenti criteri, minimizzando al massimo il numero di righe del codice.

```python 
import random,string
password = []
lunghezza_password = random.randint(8, 12)
password.append(random.choice(string.ascii_lowercase))
password.append(random.choice(string.ascii_uppercase))
password.append(random.choice(string.digits))
password.append(random.choice(string.punctuation))
while len(password) < lunghezza_password + 1:
    password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
random.shuffle(password)
print(f"La password generata è: {"".join(password)}")

```

