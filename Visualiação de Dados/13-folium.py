import folium

# Criando mappa centrado em uma localização específica

mapa = folium.Map(Location=[-23.5505, -46.6333], zoom_start = 12)

# Marcações para cafeterias
cafeterias = [
    {'localizacao': [-23.5673, -46.6483], 'nome': 'Cafeteria A'},
    {'localizacao': [-23.5685, -46.6621], 'nome': 'Cafeteria B'},
    {'localizacao': [-23.5489, -46.6366], 'nome': 'Cafeteria C'},
    {'localizacao': [-23.5550, -46.6250], 'nome': 'Cafeteria D'},
]

for cafe in cafeterias:
    folium.Marker(
        location=cafe['localizacao'],
        popup=cafe['nome'],
        icon=folium.Icon(color='blue', icon='coffee')
    ).add_to(mapa)

mapa.save('./data/mapa.html')
