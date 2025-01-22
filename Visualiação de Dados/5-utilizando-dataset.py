import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from line_breaker import line_breaker as lb
from pprint import pprint as pp

df = pd.read_csv('./data/Pedidos-1.csv')

'''
#pp(df)
#lb.lineBreaker()
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color='skyblue')
# Quantidade de Unidades vendidas por região
plt.xlabel('Região')
plt.ylabel('Total de Unidades Vendidas')
plt.title('Quantidade de unidas vendidas por região')
plt.xticks(rotation = 45)
#plt.show()

# Distribuição de vendas por item (pizza)
plt.figure(figsize=(8,6))
df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das vendas por item')
plt.axis('equal')
plt.show()

# Relação entre preço unitário e quantidade de unidades vendidas (scatter plot)
plt.figure(figsize=(8,6))
plt.scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
plt.title('Relação entre preço unitário e quantidade de unidades')
plt.xlabel('Preço Unitário')
plt.ylabel('Quantidade de unidades')
plt.grid(True)
plt.show()

# Quantidade de unidades vendidas ao longo do tempo
# Convertendo DataPedido para o formato de data
df['DataPedido'] = pd.to_datetime(df['DataPedido'])
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green')
plt.title('Quantidade de unidades vendidas ao longo do tempo')
plt.xlabel('Data do pedido')
plt.ylabel('Unidades vendidas')
plt.grid(True)
plt.show()
'''

# Quantidade de unidades vendidas por estado em cada região
pivot = df.pivot_table(
    index='Estado',
    columns='Regiao',
    values='Unidades',
    aggfunc='sum',
    fill_value=0
)
pivot.plot(kind='bar', stacked=True)
plt.title('Quantidade de unidades vendidas por estado em cada região')
plt.xlabel('Estado')
plt.ylabel('Unidades vendidas')
plt.legend(title='Região', loc='upper left', bbox_to_anchor=(1.05,1))
plt.xticks(rotation=45)
plt.show()