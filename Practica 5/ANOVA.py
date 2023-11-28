import pandas as pd
from scipy.stats import f_oneway

# Cargar el conjunto de datos desde el archivo CSV
# Asegúrate de reemplazar 'nombre_del_archivo.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('New_Spotify_Youtube.csv')

# Realizar el ANOVA 1: Comparar la Energía entre Diferentes Álbumes
anova_result_1 = f_oneway(df[df['Album'] == 'Demon Days']['Energy'],
                           df[df['Album'] == 'Californication (Deluxe Edition)']['Energy'],
                           df[df['Album'] == 'Intimo']['Energy'])
print("Resultado del ANOVA para la Energía entre Álbumes:")
print("Estadística F:", anova_result_1.statistic)
print("Valor p:", anova_result_1.pvalue)

# Realizar el ANOVA 2: Comparar la Duration_ms entre Diferentes Artistas
anova_result_2 = f_oneway(df[df['Artist'] == 'Nicky Jam']['Duration_ms'],
                           df[df['Artist'] == 'The Beatles']['Duration_ms'],
                           df[df['Artist'] == 'Machine Gun Kelly']['Duration_ms'])
print("\nResultado del ANOVA para la Duración entre Artistas:")
print("Estadística F:", anova_result_2.statistic)
print("Valor p:", anova_result_2.pvalue)

# Realizar el ANOVA 3: Comparar la Speechiness entre Diferentes Albumes
anova_result_3 = f_oneway(df[df['Album'] == 'Planet Pit (Deluxe Version)']['Speechiness'],
                           df[df['Album'] == 'Mad Love The Prequel']['Speechiness'],
                           df[df['Album'] == 'All Eyez On Me']['Speechiness'])
print("\nResultado del ANOVA para la Speechiness entre Álbumes:")
print("Estadística F:", anova_result_3.statistic)
print("Valor p:", anova_result_3.pvalue)

# Realizar el ANOVA 4: Comparar la Liveness entre Diferentes Artistas
anova_result_4 = f_oneway(df[df['Artist'] == '2Pac']['Liveness'],
                           df[df['Artist'] == 'Snoop Dogg']['Liveness'],
                           df[df['Artist'] == 'Elvis Presley']['Liveness'])
print("\nResultado del ANOVA para la Liveness entre Artistas:")
print("Estadística F:", anova_result_4.statistic)
print("Valor p:", anova_result_4.pvalue)

# Realizar el ANOVA 5: Comparar la Tempo entre Diferentes Albumes
anova_result_5 = f_oneway(df[df['Album'] == 'mainstream sellout']['Tempo'],
                           df[df['Album'] == 'Everyday Is Christmas (Deluxe Edition)']['Tempo'],
                           df[df['Album'] == 'Christmas Songs by Sinatra']['Tempo'])
print("\nResultado del ANOVA para el Tempo entre Álbumes:")
print("Estadística F:", anova_result_5.statistic)
print("Valor p:", anova_result_5.pvalue)
