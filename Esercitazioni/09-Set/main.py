# SET

# Union
# union si puo fare con il metodo union() o con l'operatore | in modo da ottenere un nuovo set che contiene gli elementi di entrambi i set
# Definizione dei set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Utilizzando l'operatore |
result_operator = set1 | set2
# Utilizzando il metodo union()
result_method = set1.union(set2)
print("Union con operatore |:", result_operator)
print("Union con metodo union():", result_method)
# posso unire piu set cosi
# usando l'operatore
set3 = {7, 8, 9}
set4 = {10, 11, 12}
result_multiple = set1 | set2 | set3 | set4
print("Union con piu set:", result_multiple)  # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# usando il metodo union
result_multiple_method = set1.union(set2, set3, set4)
print("Union con piu set (metodo):", result_multiple_method)  # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# Intersection
# Usa l'operatore & oppure il metodo intersection() per ottenere un nuovo set contenente solo gli elementi comuni
# Definizione dei set
set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
# Utilizzando l'operatore &
result_intersection_operator = set3 & set4
# Utilizzando il metodo intersection()
result_intersection_method = set3.intersection(set4)
print("Intersezione con operatore &:", result_intersection_operator)  # output: {3, 4}
print("Intersezione con metodo intersection():", result_intersection_method)  # output: {3, 4}

# Difference
# Usa l'operatore - oppure il metodo difference() per ottenere un nuovo set contenente gli elementi che sono in set5 ma non in set6
# Definizione dei set
set5 = {1, 2, 3, 4}
set6 = {3, 4, 5, 6}
# Utilizzando l'operatore -
result_difference_operator = set5 - set6
# Utilizzando il metodo difference()
result_difference_method = set5.difference(set6)
print("Differenza con operatore -:", result_difference_operator)  # output: {1, 2}
print("Differenza con metodo difference():", result_difference_method)  # output: {1, 2}

# Update
# serve per modificare direttamente il set originale, anziché creare un nuovo set
# Questo può essere utile se non hai bisogno di conservare il set iniziale separatamente oppure se vuoi risparmiare memoria evitando la creazione di un nuovo oggetto
# se usi set1.update(set2), stai aggiungendo in-place gli elementi di set2 a set1
# copare il set originale di solito è una best practice ma non è necessario infatti posso fare:
# set_originale.update(set_aggiunta)
# print("Set originale dopo update:", set_originale)  # Mostrerà {1, 2, 3, 4, 5}
# se vuoi avere ancora il set iniziale disponibile, usa una copia; altrimenti, l'aggiornamento diretto va benissimo

# Union con Update
# Utilizza il metodo update() per aggiungere in-place gli elementi di set2 a set1
# Creiamo una copia per non modificare l'originale
set1_copy = set1.copy()  # Copia di set1
set1_copy.update(set2)  # Unione in-place
print("Set1 dopo update con set2:", set1_copy)

# Intersection con Update
# Utilizza il metodo intersection_update() per aggiornare in-place set3 mantenendo solo gli elementi comuni con set4
# Creiamo una copia per non modificare l'originale
set3_copy = set3.copy()
set3_copy.intersection_update(set4)
print("Set3 dopo intersection_update con set4:", set3_copy)

# Difference con Update
# Utilizza il metodo difference_update() per aggiornare in-place set5 rimuovendo gli elementi presenti anche in set6 in pratica li sottraiamo
# Creiamo una copia per non modificare l'originale
set5_copy = set5.copy()
set5_copy.difference_update(set6)
print("Set5 dopo difference_update con set6:", set5_copy)