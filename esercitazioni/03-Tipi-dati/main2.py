# TIPI DI DATI COMPLESSI

# lista = Struttura dati ordinata e mutabile che può contenere elementi duplicati.
# set (insiemi) = Struttura dati non ordinata e mutabile che non permette elementi duplicati.
# Tuple = Struttura dati ordinata e immutabile che può contenere elementi duplicati.
# Dizionari = Struttura dati non ordinata (in versioni più vecchie di Python) e mutabile che memorizza coppie chiave-valore uniche.

# LISTA
frutta = ["Mela", "Banana", "Ciliegia"]

print("Stampa tutti gli elementi della lista")
print(frutta)   
print("-" * 40)

print("Stampa il primo elemento")
print(frutta[0])   
print("-" * 40)

print("Stampa l'ultimo elemento")
print(frutta[-1])                        
print("-" * 40)

print("Stampa il penultimo elemento")
print(frutta[-2])                        
print("-" * 40)

print("Stampa tutti gli elementi con slicing")
print(frutta[::])                        
print("-" * 40)

print("Stampa gli elementi con indice pari")
print(frutta[::2])                       
print("-" * 40)

print("Stampa dal secondo al terzo elemento")
print(frutta[1:3])                       
print("-" * 40)

print("Stampa tutti gli elementi con un ciclo for")
for frutto in frutta:
    print(frutto)                        
print("-" * 40)

print("Stampa gli elementi uniti con join")
print(",".join(frutta))                  
print("-" * 40)

print("Mostra i metodi disponibili per la lista")
print(dir(frutta))                        
print("-" * 40)

print("Mostra la lunghezza della lista")
print(len(frutta))                        
print("-" * 40)

print("Verifica se 'mela' è presente nella lista")
print("mela" in frutta)                   
print("-" * 40)

print("Verifica se 'Mela' è presente nella lista")
print("Mela" in frutta)                   
print("-" * 40)

print("Aggiunta di un elemento alla fine della lista")
frutta.append("Fragola")                  
print(frutta)
print("-" * 40)

print("Estensione della lista con più elementi")
frutta.extend(["Kiwi", "Ananas"])         
print(frutta)
print("-" * 40)

print("Rimuove il primo elemento 'Banana' trovato")
frutta.remove("Banana")                    
print(frutta)
print("-" * 40)

print("Rimuove l'ultimo elemento della lista")
frutta.pop()                               
print(frutta)
print("-" * 40)

print("Controlla se 'Banana' è nella lista prima di rimuoverla")
if "Banana" in frutta:                     
    frutta.remove("Banana")
print(frutta)
print("-" * 40)

print("Aggiunta multipla dell'elemento 'Banana'")
frutta.append("Banana")
frutta.append("Banana")
frutta.append("Banana")
frutta.append("Banana")
print(frutta)
print("-" * 40)

print("Eliminazione dei duplicati convertendo la lista in un set")
frutta = list(set(frutta))                 
print(frutta)
print("-" * 40)

print("Inserisce 'Pera' all'indice 0")
frutta.insert(0, "Pera")                   
print(frutta)
print("-" * 40)

print("Ordina la lista in ordine alfabetico")
frutta.sort()                              
print(frutta)
print("-" * 40)

print("Inverte l'ordine della lista")
frutta.reverse()                           
print(frutta)
print("-" * 40)

print("Ordina la lista in ordine alfabetico inverso")
frutta.sort(reverse=True)                  
print(frutta)
print("-" * 40)

print("Restituisce l'indice della prima occorrenza di 'Pera'")
print(frutta.index("Pera"))                
print("-" * 40)

print("Copia della lista")
frutta2 = frutta.copy()                    
print(frutta2)
print("-" * 40)

print("Svuotamento della lista")
frutta.clear()                             
print("-" * 40)

# Stampa scritta SET al centro
print(f"{'SET':^40}")
print("-" * 40)

print("4")
print("-" * 40)
