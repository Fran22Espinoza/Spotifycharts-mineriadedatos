import pandas as pd

# Ruta al archivo CSV
csv_file_path = "Spotify_Youtube.csv"

# Cargar el conjunto de datos CSV en un DataFrame de Pandas
df = pd.read_csv(csv_file_path)

# Mostrar las primeras filas del DataFrame
print(df.head())
