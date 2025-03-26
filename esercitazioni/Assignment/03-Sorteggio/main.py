import random

partecipante = ""
lista_partecipanti = []
j = 1
while True:
    while True:
        partecipante = input("Inserisci il nome del partecipante")
        lista_partecipanti.append(partecipante)
        if partecipante.lower != "ok": 
            break
    numero_squadre = int(input("Inserisci il numero di squadre desiderate: "))

    if not numero_squadre.is_integer() or numero_squadre == 0:
        print("Il numero deve essere un intero diverso da 0: ")
        continue

# generare n liste di dei partecipanti
squadre_numeri_pari = len(lista_partecipanti) // numero_squadre

# Diczionario delle squadre
squadre = {}
for i in range (1, numero_squadre):
    squadre["{i}"] = []

    

"""

 - l'enlenco dei partecipanti è inizialmente memorizzata su una lista.
 - il programma chiede all'utente il numero di squadra in cui dividerli.
 - Successivamente, genera un numero casuale di partecipanti e li assegna alle squadre in modo casuale.
 - il programma genera le liste delle squadre e le stampa a video.

Se i partecipanti sono 10 , il programma farà due squadre di 3 poi una squadra di 4

"""