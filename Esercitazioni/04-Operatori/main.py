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

# Operatori aritmetici ( +, -, *, /, %)
numero_a = 10  
numero_b = 20
somma_c = numero_a + numero_b
print(somma_c)  # 30
# modulo
modulo_d = 10 % 3  # Resto della divisione
print(modulo_d)  # 1

# Operatori di confronto ( ==, !=, >, <, >=, <=)
numero_e = 10  
numero_f = 20 
confronto_g = numero_e == numero_f
print(confronto_g)  # False

# Operatori logici ( and, or, not)
condizione_h = True
condizione_i = False
# and (entrambe le condizioni devono essere vere)
risultato_j = condizione_h and condizione_i
print(risultato_j)  # False
# or (almeno una delle condizioni deve essere vera)
risultato_k = condizione_h or condizione_i
print(risultato_k)  # True
# not (negazione cioe' se la condizione e' vera diventa falsa e viceversa)
risultato_l = not condizione_h
print(risultato_l)  # False

# Operatori di assegnazione ( =, +=, -=, *=, /=, %=)
numero_m = 10 # assegno il valore 10 alla variabile numero_m
numero_m += 5  # Equivale a numero_m = numero_m + 5
print(numero_m)  # 15

# Operatori di incremento e decremento (simulati)
numero_n = 10
numero_n += 1  # Incremento di 1
print(numero_n)  # 11

# Operatori di concatenazione ( + )
stringa_o = "Ciao"
stringa_p = "Mondo"
stringa_q = stringa_o + " " + stringa_p
print(stringa_q)  # Ciao Mondo
# abbiamo deciso di usare solo f-string per la stampa invece di concatenare le stringhe (interpolazione di stringhe)
# esempio con interpolazione
print(f"{stringa_o} {stringa_p}")