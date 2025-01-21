import pandas as pd
import pprint as pp
from line_breaker import line_breaker as lb

lb.lineBreaker()

dados = {
    'Título': ['Aventuras no Espaço', 'O Mistério do Castelo', 'História Antiga', 'A Arte da Guerra'],
    'Autor': ['João', 'Maria', 'Pedro', 'SunTzu'],
    'Gênero': ['Ficção Científica', 'Mistério', 'História', 'Filosofia'],
    'Ano de Publicação': [2015, 2018, 2016, 2014],
    'Preço (R$)': [25.50, 19.99, 30.00, 15.75],
    'Quantidade': [100, 85, 120, 150]
}

df = pd.DataFrame(dados)

pp.pprint(df)

# Exportando para Planilha Excel
arquivo = './data/livros.xlsx'
df.to_excel(arquivo, index=False)