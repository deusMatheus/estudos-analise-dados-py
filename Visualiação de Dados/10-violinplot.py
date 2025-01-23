import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Criando dataframe
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros']
vendas = {
    'Categoria': np.random.choice(categorias, 1000),
    'Vendas': np.random.normal(loc=50, scale=20, size=1000)
}

df = pd.DataFrame(vendas)

plt.figure(figsize=(10,10))
sns.violinplot(
    x='Categoria',
    y='Vendas',
    data=df,
    palette='muted'   
)
plt.title('Distribuição de vendas por categoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.show()