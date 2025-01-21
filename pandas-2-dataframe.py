import pandas as pd
import pprint as pp
from pandas_titulos import titulos

# Criando as series

series_titulos = pd.Series(titulos.dados_titulos)
series_anos = pd.Series(titulos.dados_anos)

pp.pprint(series_titulos)
titulos.printLineBreak()
pp.pprint(series_anos)

# Criando dataframe combinando as series

data = {
    'Títulos': series_titulos,
    'Anos': series_anos
    }

dataframe_times = pd.DataFrame(data)
titulos.printLineBreak()
pp.pprint(dataframe_times)