#import pandas as pd
import matplotlib.pyplot as plt
import pprint as pp
from pandas_exemplo_df import exemplo

df = exemplo.dataframe

pp.pprint(df)
exemplo.lineBreak()

# Visualizando as primeiras lindas do DataFrame
pp.pprint(df.head(2)) # o método head(n) retorna as n primeiras linhas do dataframe
exemplo.lineBreak()

# Informações sobre o DataFrame
pp.pprint(df.info())
exemplo.lineBreak()

# Estatística descritiva
pp.pprint(df.describe())
exemplo.lineBreak()

# Condição dem DataFrame (salário > 5000)
pp.pprint(df[ df['Salario'] > 5000 ])
exemplo.lineBreak()

# Ordenando por idade
pp.pprint('Ordenando do menor para o maior')
pp.pprint(df.sort_values(by='Idade', ascending=True))
exemplo.lineBreak()
pp.pprint('Ordenando do maior para o menor')
pp.pprint(df.sort_values(by='Idade', ascending=False))
exemplo.lineBreak()

# Adicionando novos dado
df['BonusSalarial'] = df['Salario'] * 0.1
df['SalarioLiquido'] = df['Salario'] + df['BonusSalarial']
pp.pprint(df)
exemplo.lineBreak()

# Agrupamento e agregação
pp.pprint(df.groupby('Cargo')['Salario'].mean())
exemplo.lineBreak()

# Visualização gráfica
df.plot(
    kind='bar',
    x = 'Nome',
    y = 'Salario',
    title = 'Salário dos Funcionários',
    rot=45
)
plt.show()