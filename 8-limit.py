from mongoClientPy import mongoClientPy as m
from pprint import pprint as p

# Todos os prêmios compartilhados entre 3 pessoas
for doc in m.db.prizes.find({
    'laureates.share': '3'
}):
    p('{year} {category}'.format(**doc))

print('\n---\n')

# Utilizando limit para limitar o número de registros diretamente pelo db, aumentando desempenho e diminuindo tempo de execução de código
for doc in m.db.prizes.find({
    'laureates.share': '3'
},limit=10):
    p('{year} {category}'.format(**doc))

# Utilizando skip para pular os n primeiros resultados

print('\n---\n')

for doc in m.db.prizes.find({
    'laureates.share': '3'
},limit=5, skip=5):
    p('{year} {category}'.format(**doc))

# Refatorando / Ordenação ascendente

print('\n---\n')

for doc in m.db.prizes.find({
    'laureates.share':'3'}) \
    .sort([('year',1)]) \
    .limit(3) \
    .skip(3):
    p('{year} {category}'.format(**doc))