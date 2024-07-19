# # Esercizio su Pandas

# Scenario: Una catena di ristoranti vuole analizzare le vendite giornaliere in diverse filiali.
# Obiettivo: Utilizzare pandas per calcolare le vendite medie giornaliere per ogni filiale.
# Dati: Il dataset contiene colonne "Data", "Filiale" e "Vendite".

# Compiti:
# Genera i dati da un file CSV.
# Utilizza groupby() per raggruppare i dati per "Data" e "Filiale".
# Calcola la media delle vendite giornaliere per filiale
# Calcola quale filiale ha venduto di più
# Salva tutti i valori e i risultati su un nuovo file(ES: csv).

import pandas as pd

# Creazione dei dati di esempio e salvataggio in un file CSV
dati = {
    'Data': ['2024-07-01', '2024-07-01', '2024-07-01',
             '2024-07-02', '2024-07-02', '2024-07-02',
             '2024-07-03', '2024-07-03', '2024-07-03'],
    'Filiale': ['Filiale_A', 'Filiale_B', 'Filiale_C',
                'Filiale_A', 'Filiale_B', 'Filiale_C',
                'Filiale_A', 'Filiale_B', 'Filiale_C'],
    'Vendite': [200, 150, 180,
                220, 160, 190,
                210, 170, 200]
}

df = pd.DataFrame(dati)
df.to_csv('vendite.csv', index=False)
# Carica i dati dal file CSV
df = pd.read_csv('vendite.csv')

# Converti la colonna 'Data' in formato datetime
df['Data'] = pd.to_datetime(df['Data'])

# Raggruppa i dati per 'Data' e 'Filiale' e calcola la media delle vendite giornaliere
media_vendite_giornaliera = df.groupby(['Data', 'Filiale'])['Vendite'].mean().reset_index()

# Raggruppa i dati solo per 'Filiale' e calcola la somma delle vendite per filiale
somma_vendite_per_filiale = df.groupby('Filiale')['Vendite'].sum().reset_index()

# Trova la filiale con le vendite più alte
filiale_max_vendite = somma_vendite_per_filiale.loc[somma_vendite_per_filiale['Vendite'].idxmax()]


# salva i risu. in nuovi file csv
media_vendite_giornaliera.to_csv('media_vendite_giornaliera.csv', index=False)
somma_vendite_per_filiale.to_csv('somma_vendite_per_filiale.csv', index=False)

# stampiamo  i risul.per verifica
print("Media vendite giornaliere per filiale:")
print(media_vendite_giornaliera)

print("\nSomma vendite per filiale:")
print(somma_vendite_per_filiale)

print("\nFiliale con le vendite più alte:")
print(filiale_max_vendite)