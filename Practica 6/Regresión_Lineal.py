import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

# Cargar el conjunto de datos desde el archivo CSV
# Asegúrate de reemplazar 'nombre_del_archivo.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# Función para realizar la regresión lineal y generar gráficos
def linear_regression_and_plot(X, y, xlabel, ylabel, title, filename):
    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predecir en el conjunto de prueba
    y_pred = model.predict(X_test)

    # Calcular el coeficiente de determinación (R2 Score)
    r2_score = metrics.r2_score(y_test, y_pred)

    # Crear un gráfico de dispersión con la línea de regresión
    plt.scatter(X_test, y_test, color='blue', label='Datos reales')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Línea de regresión')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    
    # Mostrar el coeficiente de determinación en el gráfico
    plt.text(np.max(X_test), np.max(y_test), f'R2 Score: {r2_score:.2f}', horizontalalignment='right')

    # Guardar el gráfico como imagen
    plt.savefig(f'{filename}.png')
    
    # Mostrar el gráfico
    plt.show()

# Ejemplo 1: Energía vs. Tempo
linear_regression_and_plot(df[['Tempo']], df['Energy'], 'Tempo', 'Energy', 'Regresión Lineal para Energía vs. Tempo', 'regression_example_1')

# Ejemplo 2: Valence vs. Danceability
linear_regression_and_plot(df[['Danceability']], df['Valence'], 'Danceability', 'Valence', 'Regresión Lineal para Valence vs. Danceability', 'regression_example_2')

# Ejemplo 3: Stream vs. Duration_ms
linear_regression_and_plot(df[['Duration_ms']], df['Stream'], 'Duration (ms)', 'Stream', 'Regresión Lineal para Stream vs. Duration', 'regression_example_3')

# Ejemplo 4: Likes vs. Comments
linear_regression_and_plot(df[['Comments']], df['Likes'], 'Comments', 'Likes', 'Regresión Lineal para Likes vs. Comments', 'regression_example_4')

# Ejemplo 5: Loudness vs. Acousticness
linear_regression_and_plot(df[['Acousticness']], df['Loudness'], 'Acousticness', 'Loudness', 'Regresión Lineal para Loudness vs. Acousticness', 'regression_example_5')
