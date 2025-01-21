import pandas as pd
import pprint as pp
import json
from line_breaker import line_breaker as lb

# Importando arquivo JSON
df = pd.read_json('data/series.json')

# Desta maneira, o print sai bugado. Precisaria de for's acoplados para mostrar os dados de maneira mais legível. Pode-se contornar este problema utilizando json_normalize. 
pp.pprint(df)
lb.lineBreaker()

df_series = pd.json_normalize(
    df['series'], 
    'temporadas',
    ['titulo', 'genero', 'ano_lançamento']
)

pp.pprint(df_series)
lb.lineBreaker()

# Agora, façamos iterando os dados para obter o número total de episódios de uma série.
temporadas_expandidas = []
for serie in df['series']:
    total_episodios = sum(temporada['episodios'] for temporada in serie['temporadas'])
    serie_info = {
        'titulo': serie['titulo'],
        'genero': serie['genero'],
        'total_episodios': total_episodios
    }
    temporadas_expandidas.append(serie_info)

pp.pprint(temporadas_expandidas)
lb.lineBreaker()

df_expandido = pd.DataFrame(temporadas_expandidas)
pp.pprint(df_expandido)
lb.lineBreaker()