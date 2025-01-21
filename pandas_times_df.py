from pandas_titulos import titulos
import pandas as pd

class df_times:

    series_titulos = pd.Series(titulos.dados_titulos)
    series_anos = pd.Series(titulos.dados_anos)
        
    data = {
        'Títulos': series_titulos,
        'Anos': series_anos
        }

    dataframe_times = pd.DataFrame(data)