# MATH
import math

# GESTONE DI NUMERI E OPERATORI MATEMATICI
# i metodi con * sono 

# abs - Valore assoluto *
numero1 = -10
abs_numero1 = abs(numero1)  # Valore assoluto di numero1
print(abs_numero1)  # Stampa: 10
print(abs(abs_numero1))  # Stampa: 10

# ceil - Arrotondamento per eccesso *
numero2 = 10.1
ceiling_numero2 = math.ceil(numero2)  # Arrotonda per eccesso
print(ceiling_numero2)  # Stampa: 4

# floor - Arrotondamento per difetto *
numero3 = 10.9
floor_numero3 = math.floor(numero3)  # Arrotonda per difetto
print(floor_numero3)  # Stampa: 10

# round - Arrotondamento *
numero4 = 10.576
int_numero4 = round(numero4)  # Arrotonda al numero intero più vicino
print(int_numero4)  # Stampa: 11
round_numero4 = round(numero4, 2)  # Arrotonda a 2 decimali
print(round_numero4)  # Stampa: 10.57

# max - numero massimo *
numero5, numero6 = 10, 20
max_numero = max(numero5, numero6)  # Restituisce il numero massimo
print(f"il numero più grande è {max_numero}")  # Stampa: 20

# min - numero minimo 
numero7, numero8 = 10, 20
min_numero = min(numero7, numero8)  # Restituisce il numero minimo
print(f"il numero più piccolo è {min_numero}")  # Stampa: 10

# pow - Potenza 
numero9, numero10 = 2, 3
power_numero = pow(numero9, numero10)  # Restituisce il risultato di 2^3  
print(power_numero)

# sqrt - Radice quadrata *
numero11 = 17
sqrt_numero = math.sqrt(numero11)  # Restituisce la radice quadrata di 17
print(sqrt_numero)  # Stampa: 4.123105625617661 

# PI - Costante pi greco *
raggio = 5
area = math.pi * math.pow(raggio, 2)  # Calcola l'area di un cerchio
circonferenza = 2 * math.pi * raggio  # Calcola la circonferenza di un cerchio
print(f"l'area del cerchio è {area}")  # Stampa: 78.53981633974483
print(f"la circonferenza del cerchio è {circonferenza}")  # Stampa: 31.41592653589793   

# Esercizi 
# Arrontondare una lista di numeri decimali a 2 decimali
print("*" * 20)
numeri = [10.123456, 20.654321, 30.987654]  
numeri_arrotondati = [round(num, 2) for num in numeri]  
print("lista dei numeri da arrontondare a 2 decimali:")
print(numeri) 
print("lista dei numeri arrotondati:")
print(*numeri_arrotondati)  

# Trovare il numero massimo e minimo di una array.
print("*" * 20)
numeri2 = [5, 9, 1, 3, 4]
print(f"lista dei numeri: {numeri2}")
print(f"il numero massimo dell'array è: ", max(numeri2))  
print(f"il numero minimo dell'array è: ", min(numeri2))  

# Arronda per eccesso e per difetto una lista dei numeri decimali.
print
lista = [3.14159, 2.71828, 1.61803]
print(f"Lista dei numeri da arrondare: {lista}")
lista_arrondata_eccesso = [math.ceil(num) for num in lista] 
print(f"Lista dei numeri arrotondati per eccesso: {lista_arrondata_eccesso}")
lista_arrondata_difetto = [math.floor(num) for num in lista]
print(f"Lista dei numeri arrotondati per difetto: {lista_arrondata_difetto}")
print(type(lista_arrondata_difetto))  # Stampa: <class 'list'>