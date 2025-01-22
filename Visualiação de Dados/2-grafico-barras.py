import matplotlib.pyplot as plt

# Dados - Quantidade de produtos vendidos por vendedor
vendedores = ['João', 'Maria', 'Pedro', 'Ana']
quantidade_vendida = [45, 60, 30, 55]

#plt.figure(figsize=)
plt.bar(
    vendedores,
    quantidade_vendida,
    color = 'green'
)

plt.xlabel('Vendedores')
plt.ylabel('Quantidade vendida')
plt.title('Quantidade de produtos vendidos por vendedor')

plt.show()
