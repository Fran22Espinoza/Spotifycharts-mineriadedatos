import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde el archivo CSV
# Asegúrate de reemplazar 'nombre_del_archivo.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# Función para realizar KNN y mostrar resultados
def knn_classification_and_plot(X, y, title, filename, k=3):
    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar y entrenar el clasificador KNN
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)

    # Predecir en el conjunto de prueba
    y_pred = knn_classifier.predict(X_test)

    # Imprimir el informe de clasificación
    print(f"Informe de clasificación para {title}:\n")
    print(classification_report(y_test, y_pred))

    # Crear un gráfico de dispersión
    plt.scatter(X_test[y_test == y.unique()[0]].iloc[:, 0], X_test[y_test == y.unique()[0]].iloc[:, 1], color='blue', label=y.unique()[0])
    plt.scatter(X_test[y_test == y.unique()[1]].iloc[:, 0], X_test[y_test == y.unique()[1]].iloc[:, 1], color='red', label=y.unique()[1])
    plt.scatter(X_test[y_test == y.unique()[2]].iloc[:, 0], X_test[y_test == y.unique()[2]].iloc[:, 1], color='green', label=y.unique()[2])
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()

    # Guardar el gráfico como imagen
    plt.savefig(f'{filename}.png')

    # Mostrar el gráfico
    plt.show()

# Ejemplo 1: Clasificación basada en 'Danceability' y 'Energy'
knn_classification_and_plot(df[['Danceability', 'Energy']], df['Artist'], 'KNN para Artista basado en Danceability y Energy', 'knn_example_1')

# Ejemplo 2: Clasificación basada en 'Valence' y 'Loudness'
knn_classification_and_plot(df[['Valence', 'Loudness']], df['Album'], 'KNN para Álbum basado en Valence y Loudness', 'knn_example_2')

# Ejemplo 3: Clasificación basada en 'Tempo' y 'Acousticness'
knn_classification_and_plot(df[['Tempo', 'Acousticness']], df['Track'], 'KNN para Track basado en Tempo y Acousticness', 'knn_example_3')

