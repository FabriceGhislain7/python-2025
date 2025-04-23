# DATES 

La gestione delle date è un aspetto importante della programmazione, e Python offre una serie di funzionalità integrate per lavorare con date e orari. Questo include la creazione di date, la formattazione, la conversione, il calcolo delle differenze e molto altro.

```python  
from datetime import datetime, timedelta

# GESTIONE DELLE DATE

# Creare una data specifica  
birth_date = datetime(1990, 1, 1)  # Inserisci la tua data di nascita  
print(f"Sei nato il {birth_date.strftime('%d/%m/%Y')}")  # Stampa la data di nascita formattata

# Ottenere la data di oggi  
today = datetime.today()  
print(f"Oggi è {today.strftime('%d/%m/%Y')}")  # Stampa la data odierna

# Calcolare l'età  
age_days = (today - birth_date).days  
print(f"Hai {age_days // 365} anni")  # Calcolo approssimativo dell'età in anni

# Giorni mancanti a Capodanno  
next_year = datetime(today.year + 1, 1, 1)  
days_to_new_year = (next_year - today).days  
print(f"Mancano {days_to_new_year} giorni a Capodanno")

# Giorni mancanti al prossimo mese  
next_month = today + timedelta(days=30)  
days_to_next_month = (next_month - today).days  
print(f"Mancano {days_to_next_month} giorni al prossimo mese")

# Giorni mancanti alla prossima settimana  
next_week = today + timedelta(weeks=1)  
print(f"Mancano {next_week - today} giorni alla prossima settimana")

# CONVERSIONI

# Convertire una stringa in una data  
date = datetime.strptime("2024-12-31", "%Y-%m-%d")  
print(f"La data convertita è: {date.strftime('%d/%m/%Y')}")

# Convertire una data in una stringa  
date_string = date.strftime("%d/%m/%Y")  
print(f"La data in formato stringa è: {date_string}")

# Gestire errori durante la conversione  
try:  
    parsed_date = datetime.strptime("2024-12-31", "%Y-%m-%d")  
    print(parsed_date)  
except ValueError:  
    print("Errore nella conversione della data")

# FORMATTAZIONE

# Formati lunghi e corti  
print(f"Formato lungo: {birth_date.strftime('%A, %d %B %Y')}")  
print(f"Formato corto: {birth_date.strftime('%d/%m/%Y')}")

# Giorno della settimana in italiano  
print(f"Il giorno della settimana è: {birth_date.strftime('%A')}")

# Indice numerico del giorno della settimana  
print(f"Il giorno della settimana è: {birth_date.weekday()}")  # Lunedì è 0

# Giorno dell'anno  
print(f"Il giorno dell'anno è: {birth_date.timetuple().tm_yday}")

# OPERAZIONI CON LE DATE

# Sommare o sottrarre giorni  
tomorrow = today + timedelta(days=1)  
yesterday = today - timedelta(days=1)  
print(f"Domani è: {tomorrow.strftime('%A')}")  
print(f"Ieri era: {yesterday.strftime('%A')}")

# Calcolare i giorni mancanti al prossimo compleanno  
next_birthday = datetime(today.year, 1, 1)  
if next_birthday < today:  
    next_birthday = next_birthday.replace(year=today.year + 1)  
days_until_birthday = (next_birthday - today).days  
print(f"Mancano {days_until_birthday} giorni al tuo prossimo compleanno")

# Confronto tra date  
date1 = datetime.today()  
date2 = datetime(2024, 12, 31)  
if date1 < date2:  
    print("La prima data viene prima della seconda data")  
elif date1 > date2:  
    print("La seconda data viene prima della prima data")  
else:  
    print("Le due date sono uguali")

# Calcolare la differenza tra due date  
start = datetime(2024, 1, 1)  
end = datetime(2024, 12, 31)  
difference = end - start  
print(f"La differenza tra le due date è di {difference.days} giorni")

# Aggiungere un intervallo di tempo a una data  
time_span = timedelta(days=5, hours=3, minutes=5, seconds=10)  
result_date = today + time_span  
print(f"La data risultante è: {result_date.strftime('%d/%m/%Y %H:%M:%S')}")  
```

### **Adattamenti specifici per Python**

1. **Creazione e manipolazione delle date**:  
   * In Python, utilizziamo datetime per rappresentare date e ore.  
   * Operazioni come somma o sottrazione sono possibili con timedelta.  
2. **Conversioni e parsing**:  
   * datetime.strptime() converte una stringa in un oggetto datetime.  
   * datetime.strftime() formatta un oggetto datetime in una stringa.  
3. **Differenze di tempo**:  
   * La sottrazione tra due oggetti datetime restituisce un oggetto timedelta.  
   * Puoi accedere a days, total_seconds, ecc., dall'oggetto timedelta.  
4. **Formattazione delle date**:  
   * I metodi strftime e strptime supportano vari formati, come %d per il giorno, %m per il mese, %Y per l'anno, ecc.