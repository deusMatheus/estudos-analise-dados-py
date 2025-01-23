import pandas as pd
import folium 
from pprint import pprint as pp

# Importando o dataset
dados_terremotos = pd.read_csv('./data/all_week.csv')

# Filtrando os dados para obter terremotos mais intensos (mag >= 5.5)
terremotos = dados_terremotos[dados_terremotos['mag'] >= 5.5]

# Criando o mapa 
mapa_terremotos = folium.Map(location=[0,0], zoom_start=2)

# Adicionando marcadores
for index, terremoto in terremotos.iterrows():
    folium.Marker(
        location = [terremoto['latitude'], terremoto['longitude']],
        popup = f'Magitude:{terremoto["mag"]}, Profundidade: {terremoto["depth"]}',
        icon = folium.Icon(color='red', icon='info-sign')
    ).add_to(mapa_terremotos)

mapa_terremotos.save('data/mapa_terremotos.html')