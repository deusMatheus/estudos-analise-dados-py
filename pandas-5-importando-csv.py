import pandas as pd
import pprint as pp

def lineBreaker():
    print(f'{"x ---------- "*5}x')

# Importando dataset com delimitador vírgula
df = pd.read_csv('./data/Pedidos-1.csv')
#pp.pprint(df)
lineBreaker()

# Importando dataset com delimitador ponto-vírgula
df2 = pd.read_csv('./data/Pedidos-2.csv', delimiter=';')
pp.pprint(df2)
lineBreaker()

# Leitura dos primeiros registros utilizando o método head(n), onde n representa a quantidade de registros.
pp.pprint(df.head(7))
lineBreaker()

# O método tail(n) mostra os últimos n registros, semelhante à head(n)
pp.pprint(df.tail(6))
lineBreaker()

# O método shape retorna uma tupla que representa a dimensionalidade do df. Neste caso, retornará algo como (43 linhas x 7 colunas)
pp.pprint(df.shape)
lineBreaker()

# O método dtypes trás os tipos de cada coluna
pp.pprint(df.dtypes)
lineBreaker()

# Ordenação de valores
pp.pprint(df.sort_values(by='Unidades', ascending=True)) # Ordenação crescente
lineBreaker()
pp.pprint(df.sort_values(by='Unidades', ascending=False)) # Ordenação descendente
lineBreaker()

# Contando os valores da coluna estado para obter os estados que mais venderam
pp.pprint(df['Estado'].value_counts())
lineBreaker()
