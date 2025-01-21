import pandas as pd
import pprint as pp
from line_breaker import line_breaker as lb

lb.lineBreaker()

arquivo = './data/livros.xlsx'
df = pd.read_excel(arquivo)
pp.pprint(df)
lb.lineBreaker()

# Visão geral dos dados
pp.pprint(df.head())
pp.pprint(df.tail())
lb.lineBreaker()

# Verificando os tipos de dados
pp.pprint(df.dtypes)
lb.lineBreaker()

# Estatística descritiva
pp.pprint(df.describe())
pp.pprint(df[['Preço (R$)', 'Quantidade']].describe())
lb.lineBreaker()
