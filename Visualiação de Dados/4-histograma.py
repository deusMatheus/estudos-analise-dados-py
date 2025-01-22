import matplotlib.pyplot as plt
import numpy as np

# Gerando os dados
pontuacoes = np.random.randint(0, 100, 1000)

plt.hist(
    pontuacoes,
    bins=10,
    color='skyblue',
    edgecolor = 'black'
)

plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.title('Distribuição das pontuações do teste')
plt.show()