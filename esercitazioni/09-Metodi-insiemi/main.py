# SET 
# Union 
# union si può fare con il metodo union() o con l'operatore |in modo da ottenere un nuovo set che contiene gli elementi di entrambi i set.
# Definizione di un set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)  # Output: {1, 2, 3, 4, 5}
print("Set 2:", set2)  # Output: {4, 5, 6, 7, 8}

# Utilizzando l'operatore |
result_operator = set1 | set2
# Utilizzando il metodo union()
result_method = set1.union(set2)
print("\nUnione dei set con l'operatore |:", result_operator)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("Unione dei set con il metodo union():", result_method)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersezione
# usare l'operatore & o il metodo intersection() per ottenere un nuovo set che contiene solo gli elementi comuni a entrambi i set.
# Definiamo di un set
set3 = {7, 8, 9}
set4 = {10, 11}
# Utilizzando l'operatore &
result_intersection_operator = set3 & set4
# Utilizzando il metodo intersection()
result_intersection_method = set3.intersection(set4)
print("\nIntersezione dei set con l'operatore &:", result_intersection_operator)  # Output: set()
print("Intersezione dei set con il metodo intersection():", result_intersection_method)  # Output: set()    

# Difference 
# Usa l'operatore - o il metodo difference() per ottenere un nuovo set che contiene gli elementi che sono in set5 ma non in set6.
# Definiamo dei set
set5 = {1, 2, 3, 4, 5}      
set6 = {4, 5, 6, 7, 8}
# Utilizzando l'operatore -
result_difference_operator = set5 - set6
# Utilizzando il metodo difference()                
result_difference_method = set5.difference(set6)
print("\nDifferenza dei set con l'operatore -:", result_difference_operator)  # Output: {1, 2, 3}
print("Differenza dei set con il metodo difference():", result_difference_method)  # Output: {1, 2, 3}

# Update
# Serve per modificare direttamente il set originale, anziché creare un nuovo set.
# Questo può essere utile se non hai bisogno di mantenere il set originale e vuoi risparmiare memoria evitando la creazione di un nuovo oggetto.
# Se usi set1.update(set2) o set1 |= set2, il set originale set1 verrà aggiornato per includere gli elementi di set2.

# Union con Update
# Utilizza il metodo update() per aggiungere in-place gli elementi di set2 a set1.
# Creamo una copia di set1 per non modificare il set originale
set1_copy = set1.copy() # Copia di set1
set1_copy.update(set2) # Aggiorniamo set1_copy con gli elementi di set2
print("\nSet 1 originale:", set1_copy)  # Output: {1, 2, 3, 4, 5}
print("Set 2:", set2)  # Output: {4, 5, 6, 7, 8}

# Intersezione con Update
# Utilizza il metodo intersection_update() per aggiornare in-place set3 con gli elementi comuni a set4.
# Creiamo una copia di set3 per non modificare il set originale
set3_copy = set3.copy() # Copia di set3
set3_copy.intersection_update(set4) # Aggiorniamo set3_copy con gli elementi comuni a set4
print("\nSet 3 originale aggiornato con set4:", set3_copy)  # Output: set()

# Difference con Update
# Utilizza il metodo difference_update() per aggiornare in-place set5 con gli elementi di set5 che non sono in set6.
# Creiamo una copia di set5 per non modificare il set originale
set5_copy = set5.copy() # Copia di set5
set5_copy.difference_update(set6) # Aggiorniamo set5_copy con gli elementi di set5 che non sono in set6         
print("\nSet 5 originale aggiornato con set6:", set5_copy)  # Output: {1, 2, 3}
