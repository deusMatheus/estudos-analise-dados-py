import pandas as pd
import pprint as pp
from line_breaker import line_breaker as lb
from sqlalchemy import create_engine

lb.lineBreaker()

engine = create_engine('sqlite:///pedidos.db')

df = pd.read_csv('data/Pedidos-1.csv')

# Exportando para tabela
#df.to_sql('pedidos', engine, index=False)

# Total de vendas por região
consulta_1 = 'SELECT Regiao, SUM (Unidades) AS "Total de Unidades" FROM pedidos GROUP BY Regiao'
resultado_1 = pd.read_sql_query(consulta_1, engine)

pp.pprint('Total de vendas por região:')
pp.pprint(resultado_1)
lb.lineBreaker()

consulta_2 = 'SELECT Vendedor, SUM (Unidades) AS "Total de Unidades" FROM pedidos GROUP BY Vendedor ORDER BY "Total de Unidades" DESC' # Inserindo  LIMIT 1 no final deste código retorna apenas o 1º resultado
resultado_2 = pd.read_sql_query(consulta_2, engine)

pp.pprint('Total de vendas por vendedor:')
pp.pprint(resultado_2)
lb.lineBreaker()

# Total de vendas por item
consulta_3 = 'SELECT Item, SUM(Unidades) AS "Total de Unidades" FROM pedidos GROUP BY Item ORDER BY "Total de Unidades" DESC'
resultado_3 = pd.read_sql_query(consulta_3, engine)

pp.pprint('Total de vendas por item:')
pp.pprint(resultado_3)
lb.lineBreaker()

# Média de preço por item
consulta_4 = 'SELECT Item, AVG(PrecoUnidade) AS "Média de Preços" FROM pedidos GROUP BY Item'
resultado_4 = pd.read_sql_query(consulta_4, engine)

pp.pprint('Média de preços por item:')
pp.pprint(resultado_4)
lb.lineBreaker()
