import requests
url = 'https://www.kaggle.com/datasets/prathamsaraf1389/spotify-global-top-50-daily-update/download?datasetVersionNumber=183'
response = requests.get(url)
if response.status_code == 200:
    with open('DataSet.csv', 'wb') as file:
        file.write(response.content)
        print("El dataset ha sido descargado exitosamente.")
else:
    print("Se tuvo un error al descargar el dataset, el codigo obtenido es el siguiente: ", response.status_code)