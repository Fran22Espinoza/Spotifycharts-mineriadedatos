import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_csv_from_url(url:str) -> pd.DataFrame:
    s=requests.get(url).content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = get_csv_from_url("https://raw.githubusercontent.com/Ivrohm/Mineria/main/Video_Games_Sales_as_at_22_Dec_2016.csv")
print_tabulate(df)
df.to_csv("videojuegos2.csv", index=False)


df = df.dropna(subset=["Critic_Score", "Critic_Count", "User_Score", 'Developer'])

# Guardar el DataFrame limpio en un nuevo archivo CSV

#df.rename(columns={"Name":"Titulo","Platform" :"Plataforma", "Year_of_Release":"Año_de_lanzamiento", "Genre":"Genero", "Publisher":"Pubicador", "NA_Sales":"NA_Ventas",
 #"Global_Sales":"Ventas_Globales"}, inplace=True)

df.to_csv("videojuegos_limpio2.csv", index=False)
print(df)

df = pd.read_csv('videojuegos_limpio2.csv')

print(df)
columnasatratar = df[['NA_Sales','EU_Sales','JP_Sales','Global_Sales','Other_Sales','Name', 'Platform', 'Year_of_Release','Genre',
'Publisher','Developer','Critic_Score']]


print(columnasatratar)
columnasatratar.to_csv("columnas_tratar.csv", index=False)

