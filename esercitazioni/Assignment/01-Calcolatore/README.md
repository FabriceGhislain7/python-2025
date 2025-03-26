# SEMPLICE CALCOLATORE (V 1.0)
## Realizzare un semplice calcolatore che permettere di eseguire le seguente operazioni:
 - Addizione
 - Sottrazione
 - Moltiplicazione
 . Divisione 

## Implementazione 
 - il programma deve chiedere all'utente di inserire due numeri poi cgiedere l'operazione
 - Successivamente deve stampare il risultato ottenuto
 
```python 

numero1 = float(input("inserisci il primo numero: "))
numero2 = float(input("inserisci il secondo numero: "))

scelta_operazione = input("Inserisci il segno per l'operazione desiderata: +, -, *, / : ")
operazioni = ["+", "-", "/", "*"]
while not scelta_operazione in operazioni:
    scelta_operazione = input("Inserisci di nuovo il segno per l'operazione desiderata: +, -, *, / : ")


while numero2 == 0 and scelta_operazione == "/":
    numero2 = float(input("il secondo valore deve essere diverso da zero. inserisci di nuovo il secondo numero: "))
    

if scelta_operazione == "+":
    print(numero1 + numero2)
elif scelta_operazione == "-":
    print(numero1 - numero2)
elif scelta_operazione ==  "*":
    print(numero1 * numero2)
else:
    print(numero1/numero2)


```

# SEMPLICE CALCOLATORE (V 2.0)
Contiinuare nella stessa logica chiedendo all'utente di inserire nuovi numeri finché decida di uscire. 
Implemetare il codice.