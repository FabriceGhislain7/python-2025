import os
import random

"""
- il programma prende una parole da una lista contimua in un file txt.
- la parola sorteggiata viene mescolta e chiede all'utente di indovinarla in un numero predefiniti di tentativi.
- Tiene il punteggio e salva i risultati su file.
"""
path_indovina_parola = "indovina_parola.txt"  
with open(path_indovina_parola, "r") as file:  
    content = file.read() 

parola_da_indovinare = random.choice(content.splitlines()).replace(" ", "")  
# print(f"la parola da indovinare è: {parola_da_indovinare}")
lista_parola = list(parola_da_indovinare)
print(f"lista parola: {lista_parola}")
lista_parola_mischiata = random.shuffle(lista_parola)
parola_mischiata = " ".join(lista_parola)   
print(f"la parola mischiata è: {parola_mischiata}")

registro_tentativi = "registro_tentativi.txt"  
if not os.path.exists(registro_tentativi): 
    with open(registro_tentativi, "w") as file:  
        file.write(" Registro delle tentativi dell'utente\n")  

tentativo = 0
MASSIMO_TENTATIVI = 3
punteggio = 10

while True:
    tentativo += 1
    if tentativo > MASSIMO_TENTATIVI:
        print("hai esaurito i tentativi")
        break
   
    parola_utente = input(f"indovina la parola: {parola_mischiata} \n").replace(" ", "")

    with open(registro_tentativi, "a") as file:
        file.write(f"tentativo {tentativo}: {parola_utente}\n")

    if parola_utente == parola_da_indovinare:
        print("hai indovinato la parola")
        break
    else:
        punteggio -= 2
        print("non hai indovinato la parola")
        continue

# Stampo il punteggio finale con il numero di tentativi rimanenti.
print(f"Punteggio finale: {punteggio}")
print(f"Numero di tentativi rimanenti: {MASSIMO_TENTATIVI - tentativo + (1 if tentativo > MASSIMO_TENTATIVI else 0)}")


with open(registro_tentativi, "a") as file:
    file.write(f"Punteggio finale: {punteggio}")
    file.write(f"Numero di tentativi rimanenti: {MASSIMO_TENTATIVI - tentativo + (1 if tentativo > MASSIMO_TENTATIVI else 0)}\n")
