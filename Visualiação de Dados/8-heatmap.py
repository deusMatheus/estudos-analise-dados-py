import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Dados de preços de ações para diferentes empresas ao longo de trimestres

empresas = ['Google', 'Microsoft', 'Sony', 'Samsung']
trimestres = ['T1', 'T2', 'T3', 'T4']

dados = np.random.rand(4,4) * 100

df = pd.DataFrame(
    dados,
    columns=trimestres,
    index=empresas
)

print(df)

# Criando heatmap com seaborn

sns.heatmap(df, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Utilizaçao do heatmap')
plt.xlabel('Trimestre')
plt.ylabel('Empresas')
plt.show()