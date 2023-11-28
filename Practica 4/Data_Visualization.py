import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos desde el archivo CSV
# Asegúrate de reemplazar 'nombre_del_archivo.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# 1. Histograma de Tempo de Canciones
plt.hist(df['Tempo'], bins=20, edgecolor='black')
plt.title('Histograma de Tempo de Canciones')
plt.xlabel('Tempo')
plt.ylabel('Frecuencia')
plt.show()

# 2. Gráfico de Dispersión: Danceability vs. Energy
sns.scatterplot(x='Danceability', y='Energy', data=df)
plt.title('Gráfico de Dispersión: Danceability vs. Energy')
plt.show()

# 3. Boxplot de Energy por Tono de las Canciones
plt.figure(figsize=(12, 6))
sns.boxplot(x='Key', y='Energy', data=df, palette='viridis')
plt.title('Boxplot de Energy por Tono de las Canciones')
plt.show()

# 4. Gráfico de violín de la transmisión de las canciones
plt.figure(figsize=(12, 8))
sns.violinplot(y='Stream', data=df, palette='muted')
plt.title('Gráfico de Violín de Transmisión de Canciones')
plt.ylabel('Transmisión')
plt.show()
