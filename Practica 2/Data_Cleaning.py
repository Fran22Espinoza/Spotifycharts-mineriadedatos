import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('Spotify_Youtube.csv')

# 1. Exploración inicial
print("Exploración inicial del DataFrame:")
print(df.head())
print(df.info())
print(df.describe())

# 2. Manejo de valores nulos
print("\nManejo de valores nulos:")
print("Valores nulos antes de la limpieza:")
print(df.isnull().sum())

# Eliminar filas con valores nulos
df = df.dropna()

print("Valores nulos después de la limpieza:")
print(df.isnull().sum())

# 3. Manejo de duplicados
print("\nManejo de duplicados:")
print("Duplicados antes de la limpieza:", df.duplicated().sum())

# Eliminar filas duplicadas
df = df.drop_duplicates()

print("Duplicados después de la limpieza:", df.duplicated().sum())

# 4. Corrección de tipos de datos (si es necesario)
# df['columna'] = df['columna'].astype(nuevo_tipo)

# 5. Manejo de valores atípicos (opcional)
# ... (puedes agregar código para identificar y manejar valores atípicos)

# 6. Normalización o estandarización (si es necesario)
# ... (puedes agregar código para normalizar o estandarizar columnas)

# Guardar el DataFrame limpio en un nuevo archivo CSV
df.to_csv('New_Spotify_Youtube.csv', index=False)
