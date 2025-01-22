import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Gerando dados aleatórios
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

plt.scatter(
    x,
    y
)
plt.title('Gráfico de dispersão com dados aleatórios')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()

# Criando gráfico 3d
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
ax.set_xlabel('Eixo x')
ax.set_ylabel('Eixo y')
ax.set_zlabel('Eixo z')
ax.set_title('Scatter plot 3d')
plt.show()