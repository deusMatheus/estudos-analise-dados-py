import matplotlib.pyplot as plt
import numpy as np

# Dados para os gráficos
x = np.arange(1,6)
y1 = np.array([3,5,9,7,3])
y2 = np.array([1,6,2,8,4])

# Criando subplots
fig, ax = plt.subplots(2,figsize=(8,8))

# Gráfico de barras no subplot superior
ax[0].bar(x,y1,color='skyblue')
ax[0].set_title('Gráfico de barras')

# Gráfico de linha no subplot inferior
ax[1].plot(x, y2, marker='o', linestyle='-', color='limegreen')
ax[1].set_title('Gráfico de linha')

# Ajustando espaçamento entre plots
plt.tight_layout()

plt.show()