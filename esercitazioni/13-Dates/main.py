# DATES
from datetime import datetime, timedelta

# Creare una data specifica  
birth_date = datetime(1990, 1, 1)
print(f"Sei nato il {birth_date.strftime('%d/%M/%Y')}")  # Stampa la data di nascita formattata

# FORMATTAZIONE
print(f"Formato lungo: {birth_date.strftime('%A, %d %B %Y')}")  # %A indica il giorno in forma estesa %B indica il mese in forma estesa
print(f"Formato corto: {birth_date.strftime('%d/%m/%Y')}")

# Ottenere la data di oggi
today = datetime.today()
print(f"Oggi è {today.strftime('%d/%m/%Y')}")

# Calcolare l'età  
age_days = (today - birth_date).days
print(f"Hai {age_days // 365} anni")  # / / e l operatore di divisione intera

# Giorni mancanti ad una data
next_year = datetime(today.year + 1, 1, 1)  # il primo di gennaio dell anno prossimo
days_to_new_year = (next_year - today).days
print(f"Mancano {days_to_new_year} giorni a Capodanno")

# Giorni mancanti alla prossima settimana
next_week = today + timedelta(weeks=1)  # timedelta per aggiungere settimane
print(f"Mancano {next_week - today} giorni alla prossima settimana")

# Giorni mancanti al prossimo mese
next_month = birth_date + timedelta(days=30)  # timedelta per aggiungere giorni
days_to_next_month = (next_month - today).days
print(f"Mancano {days_to_next_month} giorni al prossimo mese")

# Indice numerico del giorno della settimana  
print(f"Il giorno della settimana è: {birth_date.weekday()}")  # Lunedì è 0

# Giorno dell'anno  
print(f"Il giorno dell'anno è: {birth_date.timetuple().tm_yday}")  # tm_yday indica il giorno dell'anno

# CONVERSIONI

# Convertire una stringa in una data  
date = datetime.strptime("2024-12-31", "%Y-%m-%d")  # strptime per convertire una stringa in una data
print(f"La data convertita è: {date.strftime('%d/%m/%Y')}")
# trovare e stampare il tipo della variabile date
print(f"Il tipo della variabile date è: {type(date)}")

# Convertire una data in una stringa  
date_string = date.strftime("%d/%m/%Y")  
print(f"La data in formato stringa è: {date_string}")
# stampare il tipo della variabile date_string
print(f"Il tipo della variabile date_string è: {type(date_string)}")