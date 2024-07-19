# Esercizio Integrato su Pandas e Numpy

# Scenario: Una azienda vuole analizzare la performance giornaliera delle vendite e delle ore lavorative dei suoi dipendenti per ottimizzare le operazioni.
# Obiettivo: Utilizzare Pandas e Numpy per calcolare le vendite medie per ora lavorativa e identificare giorni di alta e bassa efficienza.
# Compiti:
# Generazione dei Dati:
# Utilizza numpy per generare un array di date per 30 giorni.
# Genera dati casuali per "Vendite" e "Ore Lavorative" utilizzando numpy per ciascun giorno.
# Crea un DataFrame pandas con colonne "Data", "Vendite", "Ore Lavorative".
# Analisi delle Vendite:
# Calcola le vendite medie per ora lavorativa per ogni giorno.
# Identifica i giorni con la massima e la minima
# Salva tutti i valori e i risultati su un nuovo file(ES: csv).

import numpy as np
import pandas as pd

# Numero di giorni
num_giorni = 30

# Genera date come stringhe per 30 giorni 
start_date_str = '2024-01-01'
dates = np.array([np.datetime64(start_date_str) + np.timedelta64(i, 'D') for i in range(num_giorni)])

# Genera dati casuali per "Vendite" e "Ore Lavorative"
vendite = np.random.uniform(low=1000, high=5000, size=num_giorni)  # Vendite tra 1000 e 5000
ore_lavorative = np.random.uniform(low=6, high=10, size=num_giorni)  # Ore lavorative tra 6 e 10

#Crea un DataFrame pandas
data = {
    'Data': dates,
    'Vendite': vendite,
    'Ore Lavorative': ore_lavorative
}
df = pd.DataFrame(data)

#Calcola le vendite medie per ora lavorativa
df['Vendite per Ora'] = df['Vendite'] / df['Ore Lavorative']

# Identifica i giorni con la massima e minima vendite per ora lavorativa
giorno_max_efficienza = df.loc[df['Vendite per Ora'].idxmax()]
giorno_min_efficienza = df.loc[df['Vendite per Ora'].idxmin()]

print("Vendite medie per ora lavorativa per ogni giorno:")
print(df)

print("\nGiorno con la massima efficienza:")
print(giorno_max_efficienza)

print("\nGiorno con la minima efficienza:")
print(giorno_min_efficienza)

#Salva i Risultati in un file CSV
df.to_csv('analisi_vendite.csv', index=False)
print("\nFile CSV salvato come 'analisi_vendite.csv'.")