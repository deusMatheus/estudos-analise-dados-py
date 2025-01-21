import pandas as pd
import pprint as p

'''
Funcionalidades de Series:
    1 - Armazenamento de dados unidimensionais;
    2 - Utilizado em operações vetoriais;
    3 - Focado em dados estruturados;

Verificando se o pandas está funcionando:
print(f'Versão instalada do pandas: {pd.__version__}')
'''

# Dados dos times de futebol e sua quantidade de títulos
dados = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Liverpool': 19,
    'Juventus': 36,
    'Bayern Munich': 30
}

# Criando uma serie a partir de um dicionário
series_times = pd.Series(dados)
p.pprint(series_times)

# Selecionando time por chave, basta passar a chave entre colchetes
print(series_times['Barcelona'])

# Selecionando time por índice utiliza-se a função iloc
print(series_times.iloc[2])
print('\n------\n')

# Selecionando por fatiamento
print(series_times['Barcelona':'Juventus'])
print('\n------\n')

# Selecionando por condição
p.pprint(series_times[series_times > 30])