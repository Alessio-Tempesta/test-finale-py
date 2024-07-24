# Esercizio su Numpy
# Scenario: Un laboratorio scientifico registra le temperature ogni ora.
# Obiettivo: Utilizzare numpy per calcolare la temperatura media, minima e massima registrata.
# Dati: Un array numpy di temperature registrate in una giornata.
# Compiti:
# Crea una dataset di dati da almeno 24 posizioni
# Calcola la temperatura media 
# Trova la temperatura massima e minima.
# Determina la temperatura più probabile per le prossime 4 posizioni rispetto a un aumento costante di 0,2 gradi al giorno ogni settimana.


import numpy as np

#  Creazione di un dataset di dati 24 ore con valori specifici:
temperature = np.array([
    22.0, 21.5, 21.0, 20.8, 20.5, 20.0, 19.8, 19.6, 19.5, 19.4, 19.3, 19.2,
    19.0, 19.1, 19.2, 19.3, 19.5, 19.6, 19.8, 20.0, 20.2, 20.5, 20.8, 21.0
])
print("Temperature registrate:")
print(temperature)

#  Calcolo della temperatura media
media_temp = np.mean(temperature)     #calcolo media dei valori array temperature
print("\nTemperatura media:")
print(media_temp)

# Trova la temperatura massima e minima
max_temp = np.max(temperature)       #temperatura massima
min_temp = np.min(temperature)         #temperatura minima
print("\nTemperatura massima:")
print(max_temp)
print("Temperatura minima:")
print(min_temp)


# Giorni aggiuntivi dalla fine del dataset esistente
incremento = 0.2  # Aumento per giorno
num_ore_aumentare = 4

# Calcolo della temperatura futura

ultim_temperatura = temperature[-1]  # Ultima temperatura registrata
future_temperatures = [ultim_temperatura + incremento * i for i in range(1, num_ore_aumentare + 1)]

print("\nTemperature previste per le prossime 4 ore:")
print(future_temperatures)