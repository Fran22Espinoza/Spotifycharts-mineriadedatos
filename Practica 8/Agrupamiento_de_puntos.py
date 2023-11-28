import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos desde el archivo CSV
# Asegúrate de reemplazar 'New_Spotify_Youtube.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# Función para realizar K-Means y visualizar los resultados
def kmeans_clustering_and_plot(X, title, num_clusters=3):
    # Inicializar el modelo K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    
    # Ajustar el modelo a los datos
    kmeans.fit(X)

    # Obtener las etiquetas de los clústeres y los centros de los clústeres
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    # Agregar las etiquetas de los clústeres al DataFrame original
    df['Cluster'] = labels

    # Crear un gráfico de dispersión con los clústeres resaltados
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X.iloc[:, 0], y=X.iloc[:, 1], hue=labels, palette='bright', marker='o', s=100)
    sns.scatterplot(x=centers[:, 0], y=centers[:, 1], marker='X', s=200, color='red', label='Centroides')
    plt.title(title)
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.legend(title='Cluster', loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Mostrar el gráfico
    plt.show()

# Ejemplo 1: Agrupamiento basado en 'Danceability' y 'Energy' con datos diferentes
kmeans_clustering_and_plot(df[['Danceability', 'Energy']], 'K-Means para Danceability y Energy (Ejemplo 1)')

# Ejemplo 2: Agrupamiento basado en 'Valence' y 'Loudness' con datos diferentes
kmeans_clustering_and_plot(df[['Valence', 'Loudness']], 'K-Means para Valence y Loudness (Ejemplo 2)')

# Ejemplo 3: Agrupamiento basado en 'Tempo' y 'Acousticness' con datos diferentes
kmeans_clustering_and_plot(df[['Tempo', 'Acousticness']], 'K-Means para Tempo y Acousticness (Ejemplo 3)')

# Ejemplo 4: Agrupamiento basado en 'Duration_ms' y 'Speechiness' con datos diferentes
kmeans_clustering_and_plot(df[['Duration_ms', 'Speechiness']], 'K-Means para Duration_ms y Speechiness (Ejemplo 4)')

# Ejemplo 5: Agrupamiento basado en 'Liveness' y 'Valence' con datos diferentes
kmeans_clustering_and_plot(df[['Liveness', 'Valence']], 'K-Means para Liveness y Valence (Ejemplo 5)')
