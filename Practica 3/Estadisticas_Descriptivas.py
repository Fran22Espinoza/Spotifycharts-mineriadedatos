import pandas as pd
import numpy as np

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# Estadísticas descriptivas básicas
print("Estadísticas descriptivas básicas:")
print(df.describe())

from scipy.stats import shapiro

# Realizar la prueba de normalidad para una variable específica (por ejemplo, 'Danceability')
stat, p_value_normalidad = shapiro(df['Danceability'])

print("\nPrueba de normalidad para 'Danceability':")
print("Estadístico de prueba:", stat)
print("Valor p:", p_value_normalidad)

import matplotlib.pyplot as plt

# Histograma de la duración de las canciones
plt.hist(df['Duration_ms'], bins=20, edgecolor='black')
plt.title('Histograma de Duración de Canciones')
plt.xlabel('Duración (ms)')
plt.ylabel('Frecuencia')
plt.show()

import seaborn as sns

# Boxplot de la energía de las canciones
sns.boxplot(x='Energy', data=df)
plt.title('Boxplot de Energía de Canciones')
plt.show()

# Countplot del tono de las canciones
sns.countplot(x='Key', data=df)
plt.title('Countplot de Tono de Canciones')
plt.show()

# Matriz de correlación múltiple
corr_matrix = df[['Danceability', 'Energy', 'Valence', 'Loudness', 'Tempo']].corr()
print("Matriz de correlación múltiple:")
print(corr_matrix)

# Gráfico de dispersión de Energía vs. Valence
plt.scatter(df['Energy'], df['Valence'])
plt.title('Gráfico de Dispersión: Energía vs. Valence')
plt.xlabel('Energía')
plt.ylabel('Valence')
plt.show()

