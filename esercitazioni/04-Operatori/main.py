# OPERATORI 

"""
I tipi principali di operatori in pyton sono:
- Aritmetici
- Di confronto 
- Logici 
- Di assegnazione
- Di incremento e di decremento (simulati)
- Di concatenazione 
"""

# Operatori aritmetici
numero_a = 10
numero_b = 20 
somma_c = numero_a + numero_b
print(somma_c) # 30

# Modulo 
modulo_d = 10 % 3 # Resto della divisione 
print(modulo_d)

# operatori di confronto
numero_e = 10
numero_f = 20
confronto_g = numero_e == numero_f
print(confronto_g)

# Operatori logici (and, or, not)
condizione_h = True
condizione_i = False 
# and (Entrambe condizioni devono essere vere),
risultato_j = condizione_h and condizione_i
print(risultato_j) # False
# or (Almeno una delle condizioni deve essere vera)
risultato_k = condizione_h or condizione_i
print(risultato_k)
# not (negazione, quindi se la condizione è vera allora diventa falsa e viceversa)
risultato_l = not condizione_h
print(risultato_l)

# Operatori di assegnazioni (0, +=, -=, *=, /=, %=)
numero_m = 10
numero_m += 5 
print (numero_m)

# Operatori di incremento e di decremento (simulati)
numero_n = 10
numero_n += 1
print(numero_n)

# Operatori di concatenazione 
striga_o = "Ciao"
striga_p = "mondo"
striga_q = striga_o + " " + striga_p
print(striga_q)

print(f"{striga_o} {striga_p}")



