# GENERATORE DI PASSWORD

# Import i moduli random e string
import random,string

# Inizializziamo la lunghezza della password
lunghezza_password = random.randint(8, 12)

password = [random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)] 

while len(password) < lunghezza_password + 1:
    password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
random.shuffle(password)
print(f"La password generata è: {"".join(password)}")