import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde el archivo CSV
# Asegúrate de reemplazar 'New_Spotify_Youtube.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# Verificar las columnas disponibles en el DataFrame
print("Columnas disponibles:", df.columns)

# Seleccionar columnas relevantes para la nube de palabras
columns_for_wordcloud = ['Artist', 'Track', 'Album']

# Verificar que las columnas seleccionadas existen en el DataFrame
missing_columns = [col for col in columns_for_wordcloud if col not in df.columns]
if missing_columns:
    print(f"Las siguientes columnas no se encuentran en el DataFrame: {missing_columns}")
else:
    # Convertir todas las celdas a cadenas de texto y concatenarlas
    text_for_wordcloud = ' '.join(df[columns_for_wordcloud].astype(str).apply(lambda x: ' '.join(x), axis=1))

    # Crear la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_wordcloud)

    # Visualizar la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nube de Palabras')
    plt.show()
