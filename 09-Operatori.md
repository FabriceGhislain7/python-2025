# OPERATORI

Gli operatori sono simboli speciali che eseguono operazioni su uno o più operandi. In Python, gli operatori sono suddivisi in diverse categorie, tra cui:

```python  
# OPERATORI  
"""  
I tipi principali di operatori in Python sono:  
- Aritmetici  
- Di confronto  
- Logici  
- Di assegnazione  
- Di incremento e decremento (simulati)  
- Di concatenazione  
"""

# ESEMPIO DI OPERATORI ARITMETICI  
# Pulire la console (in modo semplice per Python)  
import os  # Importa il modulo os che serve a interagire con il sistema operativo in modo indipendente dalla piattaforma
os.system('cls' if os.name == 'nt' else 'clear')  # Clear console (Windows e Unix-like)

# Operatori aritmetici  
numero_a = 10  
numero_b = 20  
somma_c = numero_a + numero_b  # Somma
print(somma_c)  # 30

# Modulo  
modulo_d = 10 % 3  # Resto della divisione  
print(modulo_d)  # 1

# Capire se un numero è pari o dispari  
e = 10 % 2  # 0 indica pari  
print(e)  # 0

# ESEMPIO DI OPERATORI DI CONFRONTO  
f = 10  
g = 20  
h = f == g  # Confronto di uguaglianza  
print(h)  # False  
i = f != g  # Confronto di disuguaglianza  
print(i)  # True  
l = f > g  # Maggiore di  
print(l)  # False  
m = f < g  # Minore di  
print(m)  # True  
n = f >= g  # Maggiore o uguale  
print(n)  # False  
o = f <= g  # Minore o uguale  
print(o)  # True

# ESEMPIO DI OPERATORI LOGICI  
p = True  
q = False  
r = p and q  # AND: restituisce True se entrambe le condizioni sono vere  
print(r)  # False  
s = p or q  # OR: restituisce True se almeno una delle condizioni è vera  
print(s)  # True  
t = not p  # NOT: inverte il valore booleano  
print(t)  # False

# ESEMPIO DI OPERATORI DI ASSEGNAZIONE  
u = 10  
u += 5  # u = u + 5  
print(u)  # 15  
u -= 5  # u = u - 5  
print(u)  # 10

# ESEMPIO DI INCREMENTO E DECREMENTO (simulato)  
# Python non ha operatori di incremento (++) o decremento (--), ma possiamo ottenere lo stesso risultato:  
v = 10  
v += 1  # Incremento  
print(v)  # 11  
v -= 1  # Decremento  
print(v)  # 10

# ESEMPIO DI OPERATORI DI CONCATENAZIONE  
w = "ciao"  
x = " mondo"  
y = w + x  # Concatenazione di stringhe  
print(y)  # ciao mondo  
```