from mongoClientPy import mongoClientPy as m
from pprint import pprint as p
from collections import OrderedDict

cursor = m.db.laureates.find(
    filter = {'bornCountry': 'USA'},
    projection = {'prizes.year': 1},
    limit = 3
)

for doc in cursor:
    p(doc['prizes'])

# Refatorando consulta com agregações
print('\n---\n')

cursor = m.db.laureates.aggregate([
    {'$match' : {'bornCountry':'USA'}},
    {'$project' : {'prizes.year':1}},
    {'$limit':3}
])

for doc in cursor:
    p(doc['prizes'])

# Adicionando etapas
print('\n---\n')

p(list(m.db.laureates.aggregate([
    {'$match' : {'bornCountry':'USA'}},
    {'$project' : {'prizes.year':1, '_id':0}},
    {'$sort' : OrderedDict([('prizes.year', 1)])},
    {'$limit' : 3},
    {'$skip' : 1}
])))

# Laureados nascidos nos EUA
print('\n---\n')
p(list(m.db.laureates.aggregate([
    {'$match': {'bornCountry': 'USA'}},
    {'$count': 'qtd_born_USA'}
])))
