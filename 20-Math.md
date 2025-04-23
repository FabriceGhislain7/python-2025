# MATH

La libreria math serve a gestire numeri e operazioni matematiche in Python. Fornisce funzioni per calcolare valori assoluti, arrotondamenti, potenze, radici, funzioni trigonometriche e costanti matematiche come π.

```python  
import math

# GESTIONE DI NUMERI E OPERAZIONI MATEMATICHE

# abs - Valore assoluto  
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

# round - Arrotondamento  
number4 = 10.574  
int_number = round(number4)  # Arrotonda al numero intero più vicino  
round_number = round(number4, 2)  # Arrotonda a 2 cifre decimali  
print(int_number)  # Output: 11  
print(round_number)  # Output: 10.57

# max - Numero massimo  
number5, number6 = 10, 20  
max_number = max(number5, number6)  
print(f"Il numero più grande è {max_number}")  # Output: 20

# min - Numero minimo  
number7, number8 = 10, 20  
min_number = min(number7, number8)  
print(f"Il numero più piccolo è {min_number}")  # Output: 10

# media aritmetica
numeri = [10, 20, 30]
media = sum(numeri) / len(numeri)
print(f"La media è: {media}")  # Output: 20.0
# varianza (cioe la media dei quadrati delle differenze dalla media che serve in modo da capire quanto sono distanti i numeri dalla media)
varianza = sum((x - media) ** 2 for x in numeri) / len(numeri)
print(f"La varianza è: {varianza}")  # Output: 66.66666666666667
# deviazione standard (cioe la radice quadrata della varianza che serve a capire quanto sono distanti i numeri dalla media)
deviazione_standard = math.sqrt(varianza)
print(f"La deviazione standard è: {deviazione_standard}")  # Output: 8.16496580927726

# pow - Potenza  
number9, number10 = 2.1, 3  
pow_number = math.pow(number9, number10)  
print(pow_number)  # Output: 9.261

# sqrt - Radice quadrata  
number11 = 17  
sqrt_number = math.sqrt(number11)  
print(sqrt_number)  # Output: 4.123

# cos, sin, tan - Funzioni trigonometriche  
angle = math.radians(45)  # Convertire in radianti  
cos_number = math.cos(angle)  
sin_number = math.sin(angle)  
tan_number = math.tan(angle)  
print(f"Coseno: {cos_number}, Seno: {sin_number}, Tangente: {tan_number}")

# PI - Costanti  
raggio = 5  
area = math.pi * math.pow(raggio, 2)  
circonferenza = 2 * math.pi * raggio  
print(f"Area: {area}, Circonferenza: {circonferenza}")

# ESERCIZI

# Arrotonda un array di numeri decimali alla seconda cifra decimale  
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

# Arrotonda per eccesso e per difetto un array di numeri decimali  
numeri3 = [3.14159, 2.71828, 1.61803]  
for num in numeri3:  
    per_eccesso = math.ceil(num)  
    per_difetto = math.floor(num)  
    print(f"Arrotondato per eccesso: {per_eccesso}")  
    print(f"Arrotondato per difetto: {per_difetto}")  
```

### **Adattamenti specifici per Python**

1. **Arrotondamento**:  
   * math.ceil() e math.floor() per arrotondamenti rispettivamente per eccesso e per difetto.  
   * round() per arrotondamenti a un numero specifico di cifre decimali.  
2. **Valore massimo e minimo**:  
   * Python utilizza max() e min() per ottenere il massimo e il minimo di un elenco o due valori.  
3. **Potenza e radice quadrata**:  
   * math.pow() per le potenze.  
   * math.sqrt() per la radice quadrata.  
4. **Trigonometria**:  
   * math.cos(), math.sin(), e math.tan() accettano angoli in radianti.  
   * Usa math.radians() per convertire i gradi in radianti.  
5. **Costanti matematiche**:  
   * math.pi fornisce il valore di π.