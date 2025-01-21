import pandas as pd
import pprint as pp
from pandas_titulos import titulos
from pandas_times_df import df_times

dataframe = df_times.dataframe_times

pp.pprint(dataframe)
titulos.printLineBreak()

# Média de títulos
media_titulos = dataframe['Títulos'].mean() #mean() retorna a média
pp.pprint(f'Média de títulos: {media_titulos}')
titulos.printLineBreak()

# Time com mais títulos
mais_titulos = dataframe['Títulos'].idxmax() # idxmax() retorna o time com maior índice
qtd_titulos = dataframe['Títulos'].max() #max() retorna o valor com maior índice
pp.pprint(f'O {mais_titulos} possui a maior quantidade de títulos, marcando {qtd_titulos} no total')
titulos.printLineBreak()

# Ano com mais títulos
todos_anos = dataframe['Anos'].explode() # explode() tira do formato de lista
ano_mais_titulos = todos_anos.mode() #mode() retorna a moda
pp.pprint(ano_mais_titulos[0]) # Para pegar o primeiro lugar, basta colocar o índice 0
titulos.printLineBreak()