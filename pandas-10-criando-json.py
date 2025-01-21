import pandas as pd
import pprint as pp
import json
from line_breaker import line_breaker as lb

lb.lineBreaker()

# Dados
dados_series = {
    'series':[
        {
            'titulo':'Stranger Things',
            'genero':'Ficção Científica',
            'ano_lançamento':'2016',
            'temporadas':[
                {'numero':1,'episodios':8},
                {'numero':2,'episodios':9},
                {'numero':3,'episodios':8},
                {'numero':4,'episodios':9}
            ]
        },
                {
            'titulo':'Breaking Bad',
            'genero':'Drama',
            'ano_lançamento':'2008',
            'temporadas':[
                {'numero':1,'episodios':7},
                {'numero':2,'episodios':13},
                {'numero':3,'episodios':13},
                {'numero':4,'episodios':13},
                {'numero':5,'episodios':16}
            ]
        }
    ]
}

# Exportando para arquivo JSON

with open('data/series.json', 'w') as file:
    json.dump(dados_series, file)