import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde el archivo CSV
# Asegúrate de reemplazar 'New_Spotify_Youtube.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# Agregar una nueva columna 'Tiempo' basada en la posición de las filas
df['Tiempo'] = np.arange(len(df)) + 1

# Función para realizar forecasting con ARIMA y visualizar los resultados
def arima_forecasting_and_plot(series, title):
    # Dividir la serie temporal en conjunto de entrenamiento y prueba
    train_size = int(len(series) * 0.8)
    train, test = series[0:train_size], series[train_size:]

    # Entrenar el modelo ARIMA
    model = ARIMA(train, order=(1, 1, 1))  # Parámetros (p, d, q) para ARIMA
    model_fit = model.fit()

    # Pronosticar valores futuros
    forecast = model_fit.forecast(steps=len(test))

    # Visualizar los resultados con gráfico de líneas
    plt.figure(figsize=(10, 6))
    plt.plot(train.index, train, label='Entrenamiento', color='blue', linestyle='-')
    plt.plot(test.index, test, label='Prueba', color='orange', linestyle='-')
    plt.plot(test.index, forecast, label='Pronóstico', color='green', linestyle='--')
    plt.title(title)
    plt.xlabel('Tiempo')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

# Ejemplo 1: Forecasting para 'Danceability'
arima_forecasting_and_plot(df['Danceability'], 'ARIMA Forecasting para Danceability (Ejemplo 1)')

# Ejemplo 2: Forecasting para 'Energy'
arima_forecasting_and_plot(df['Energy'], 'ARIMA Forecasting para Energy (Ejemplo 2)')

# Ejemplo 3: Forecasting para 'Valence'
arima_forecasting_and_plot(df['Valence'], 'ARIMA Forecasting para Valence (Ejemplo 3)')

# Ejemplo 4: Forecasting para 'Tempo'
arima_forecasting_and_plot(df['Tempo'], 'ARIMA Forecasting para Tempo (Ejemplo 4)')

# Ejemplo 5: Forecasting para 'Loudness'
arima_forecasting_and_plot(df['Loudness'], 'ARIMA Forecasting para Loudness (Ejemplo 5)')
