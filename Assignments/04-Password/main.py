
# Import dei moduli
import string, random

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