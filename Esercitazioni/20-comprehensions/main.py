# Comprehensions
# Si usano quando vuoi trasformare o filtrare elementi in un ciclo
# Sintassi
# [espressione for elemento in collezione if condizione]

# List Comprehensions
# Esempio 1: Creare una lista di quadrati
# senza comprehensions
numeri = [1, 2, 3, 4, 5]
quadrati = []
for numero in numeri:
    quadrati.append(numero ** 2)
print(quadrati)  # Output: [1, 4, 9, 16, 25]
# con comprehensions
quadrati = [q**2 for q in range(5)]
print(quadrati)  # Output: [1, 4, 9, 16, 25]