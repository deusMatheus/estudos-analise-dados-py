from mongoClientPy import mongoClientPy as m
from pprint import pprint as p
import timeit

def get_all_prizes_economics():
    return list(m.db.prizes.find(
        {'category':'economics'},
        {'year': 1, '_id': 0}
    ))

# Buscando prêmios de 1910
def get_prizes():
    return list(m.db.prizes.find({'year':'1910'}))

# Função para medir o tempo de execução
def measure_execution_time(function):
    executionTime = timeit.timeit(function, globals=globals(), number=1)*1000
    p(f'Tempo de execução:{executionTime:.2f} milisegundos')

# Sem índice
measure_execution_time('get_prizes()')

# Com índice
m.db.prizes.create_index([('year',1)])
measure_execution_time('get_prizes()')

# Criando índice composto
m.db.prizes.create_index([('category', 1), ('year', 1)])
measure_execution_time('get_all_prizes_economics')
