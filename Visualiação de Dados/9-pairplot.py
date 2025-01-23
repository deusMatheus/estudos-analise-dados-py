import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Criando dataframe
data = {
    'Preço': [20,25,30,18,22],
    'Quantidade': [100,120,90,110,105],
    'Receita': [2000,3000,2700,1980,2310]
}

df = pd.DataFrame(data)

# Criando pairplot com Seaborn
sns.set(style='ticks')
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Relação entre Preço, Quantidade e Receita', y=1.02)
plt.show()