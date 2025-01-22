import matplotlib.pyplot as plt

# Dados - vendas ao longo dos meses
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [150, 200, 180, 300, 250, 400]

# Criando gráfico de linha
plt.figure(figsize=(8, 5))
plt.plot(
    meses,
    vendas,
    marker = 'o',
    linestyle = '-',
    color = 'blue',
    label = 'Vendas'
)

# Adicionando rótulos e título ao gráfico
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Vendas ao longo dos meses')
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()