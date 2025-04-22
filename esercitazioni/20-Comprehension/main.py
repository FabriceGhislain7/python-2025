# Comprehesions

# List Comprehensions
# Senza comprehesions
numeri = [1, 2, 3, 4]
quadrati = []
for numero in numeri:
    quadrati.append(numero**2)
print(quadrati)

quadrati2 = [num**2 for num in numeri]
print(quadrati2)