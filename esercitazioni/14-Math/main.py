# MATH
# (i metodi con * sono disponibili senza math)

import math

# GESTIONE DI NUMERI E OPERAZIONI MATEMATICHE

# abs - Valore assoluto *
number1 = -10  
abs_number = abs(number1)  
print(abs_number)  # Output: 10

# ceil - Arrotondamento per eccesso  
number2 = 10.1  
ceiling_number = math.ceil(number2)  
print(ceiling_number)  # Output: 11

# floor - Arrotondamento per difetto  
number3 = 10.9  
floor_number = math.floor(number3)  
print(floor_number)  # Output: 10

# round - Arrotondamento *
number4 = 10.574
int_number = round(number4)  # Arrotonda al numero intero più vicino
round_number = round(number4, 2)  # Arrotonda a 2 cifre decimali
print(int_number)  # Output: 11  
print(round_number)  # Output: 10.57

# max - Numero massimo *
number5, number6 = 10, 20  
max_number = max(number5, number6)  
print(f"Il numero più grande è {max_number}")  # Output: 20

# min - Numero minimo *
number7, number8 = 10, 20  
min_number = min(number7, number8)  
print(f"Il numero più piccolo è {min_number}")  # Output: 10

# pow - Potenza  
number9, number10 = 2.1, 3  
pow_number = math.pow(number9, number10)  
print(pow_number)  # Output: 9.261000000000001

# sqrt - Radice quadrata  
number11 = 17  
sqrt_number = math.sqrt(number11)  
print(sqrt_number)  # Output: 4.123105625617661

# PI - Costanti  
raggio = 5  
area = math.pi * math.pow(raggio, 2)  
circonferenza = 2 * math.pi * raggio  
print(f"Area: {area}, Circonferenza: {circonferenza}")  # 78.53981633974483 31.41592653589793

# ESERCIZI

# Arrotonda una lista di numeri a 2 cifre decimali
numeri = [3.14159, 2.71828, 1.61803]
arrotondati = []
for num in numeri:  
    arrotondati.append(round(num, 2))  # Arrotonda a 2 cifre decimali
print(*arrotondati)  # Stampa i numeri arrotondati")

# Trova il valore max e min in un array
numeri2 = [5, 9, 1, 3, 4]
min_val = min(numeri2)  
max_val = max(numeri2)  
print(f"Il valore min è: {min_val}")  
print(f"Il valore max è: {max_val}")

# Arrotonda per eccesso e per difetto una lis di numeri decimali
numeri3 = [3.14159, 2.71828, 1.61803]
for num in numeri3:  
    per_eccesso = math.ceil(num)  
    per_difetto = math.floor(num)  
    print(f"Arrotondato per eccesso: {per_eccesso}")  
    print(f"Arrotondato per difetto: {per_difetto}")  