import pandas as pd
import pprint as pp
from line_breaker import line_breaker as lb

lb.lineBreaker()

arquivo = './data/livros.xlsx'
df = pd.read_excel(arquivo)

# Gênero - quantidade de livros - preço médio por gênero
genero_info = df.groupby('Gênero').agg({
    'Título': 'count',
    'Preço (R$)': 'mean'
})

pp.pprint(genero_info)
lb.lineBreaker()

# Livro mais caro e mais barato
livro_mais_caro = df[df['Preço (R$)'] == df['Preço (R$)'].max()]
livro_mais_barato = df[df['Preço (R$)'] == df['Preço (R$)'].min()]
pp.pprint('Livro mais caro:')
pp.pprint(livro_mais_caro)
pp.pprint('Livro mais barato:')
pp.pprint(livro_mais_barato)
lb.lineBreaker()

# Distribuição por ano de publicação
pp.pprint(df['Ano de Publicação'].value_counts())
lb.lineBreaker()

# Relação entre preço e quantidade
correlacao = df['Preço (R$)'].corr(df['Quantidade'])
pp.pprint(correlacao)
lb.lineBreaker()
