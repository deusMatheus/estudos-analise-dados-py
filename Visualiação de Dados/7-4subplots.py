import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./data/Pedidos-1.csv')

fig, ax = plt.subplots(2,2,figsize=(15,15))

# Gráfico 1
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color='skyblue', ax=ax[0,0])
# Quantidade de Unidades vendidas por região
ax[0,0].set_xlabel('Região')
ax[0,0].set_ylabel('Total de Unidades Vendidas')
ax[0,0].set_title('Quantidade de unidas vendidas por região')
ax[0,0].tick_params(axis = 'x', rotation = 45)
#plt.show()

# Gráfico 2 
# Distribuição de vendas por item (pizza)
df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax[0,1])
ax[0,1].set_title('Distribuição das vendas por item')
ax[0,1].axis('equal')

# Gráfico 3
# Relação entre preço unitário e quantidade de unidades vendidas (scatter plot)
ax[1,0].scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
ax[1,0].set_title('Relação entre preço unitário e quantidade de unidades')
ax[1,0].set_xlabel('Preço Unitário')
ax[1,0].set_ylabel('Quantidade de unidades')
ax[1,0].grid(True)

# Gráfico 4
# Quantidade de unidades vendidas ao longo do tempo
# Convertendo DataPedido para o formato de data
df['DataPedido'] = pd.to_datetime(df['DataPedido'])
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green', ax=ax[1,1])
ax[1,1].set_title('Quantidade de unidades vendidas ao longo do tempo')
ax[1,1].set_xlabel('Data do pedido')
ax[1,1].set_ylabel('Unidades vendidas')
ax[1,1].grid(True)

plt.tight_layout()
plt.show()
