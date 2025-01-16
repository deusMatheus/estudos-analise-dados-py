from mongoClientPy import mongoClientPy as m
import pprint as p

# Ordenação ascendente
cursor = m.db.prizes.find(
    {'category':'physics'},
    ['year'],
    sort=[('year',1)] # Ascendente: 1; Descentende: -1
    
)

p.pprint([doc['year'] for doc in cursor])


# Ordenação descendente
cursor2 = m.db.prizes.find(
    {'category':'physics'},
    ['year'],
    sort=[('year',-1)] # Ascendente: 1; Descentende: -1
    
)

p.pprint([doc['year'] for doc in cursor2])

# Prêmios concedidos entre 1966 e 1977
for doc in m.db.prizes.find(
    {'year': {'$gt':'1966', '$lt':'1977'}},
    ['category', 'year'],
    sort = [('year',1)]
):
    p.pprint('{year} {category}'.format(**doc)) #kwargs, estudar isso com mais calma posteriormente