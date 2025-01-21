import pandas as pd
import pprint as pp
from line_breaker import line_breaker as lb

lb.lineBreaker()
df = pd.read_csv('./data/Pedidos-1.csv')

# Convertendo os dados para tipo numérico
df['Unidades'] = pd.to_numeric(df['Unidades'])
df['PrecoUnidade'] = pd.to_numeric(df['PrecoUnidade'])

# Desempenho de vendas por região
# Primeiro agrupa-se por região e depois agregação por unidades
vendas_regiao = df.groupby('Regiao')['Unidades'].sum()
pp.pprint(vendas_regiao)
lb.lineBreaker()

# Desempenho por vendedor
melhor_vendedor = df.groupby('Vendedor')['Unidades'].sum()
pp.pprint(melhor_vendedor)
pp.pprint(f'Melhor vendedor: {melhor_vendedor.idxmax()}')
lb.lineBreaker()

# Itens mais vendidos
total_unidades = df.groupby('Item')['Unidades'].sum()
pp.pprint(total_unidades)
lb.lineBreaker()

# Preço médio por item
media_preco = df.groupby('Item')['PrecoUnidade'].mean()
pp.pprint(media_preco)
lb.lineBreaker()

# Correlação entre Unidade Vendida e Preço Unitário
'''
A correlação pode variar entre -1 e 1, indicando a direção e força da relação linear entre as variáveis.
~ 1: correlação positiva forte.
~ -1: correlação negativa forte.
~ 0: correlação fraca.
'''
correlacao = df['Unidades'].corr(df['PrecoUnidade'])
pp.pprint(correlacao)
lb.lineBreaker()
# Neste caso o resultado foi -0.11, o que indica uma correlação fraca entre Unidades e PrecoUnidade.

# Exportando para CSV
vendas_regiao_df = vendas_regiao.reset_index()
vendas_regiao_df.columns = ['Regiao', 'TotalUnidadesVendidas']
try:
    vendas_regiao_df.to_csv('./data/vendas_regiao.csv', index=False)
    print('Sucesso!')
    lb.lineBreaker()
except:
    print('Deu erro!')
    lb.lineBreaker()