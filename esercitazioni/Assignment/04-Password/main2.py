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