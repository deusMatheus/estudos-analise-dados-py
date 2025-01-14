from mongoClientPy import mongoClientPy as m
import pprint as p

# Mapeando os gêneros 
# Agregação processar os dados em uma coleção e produzir o resultado

p.pprint(m.db.laureates.distinct('gender'))

p.pprint(m.db.laureates.count_documents({'gender':'female'}))
p.pprint(m.db.laureates.count_documents({'gender':'male'}))
p.pprint(m.db.laureates.count_documents({'gender':'org'}))
p.pprint(m.db.prizes.count_documents(({'category':'physics'})))

# Mapeando as categorias dos prêmios
p.pprint(m.db.laureates.distinct('prizes.category'))

# Prêmios  compartilhados
# Quais categorias, além de física, possuem laureados com ações trimestrais?
print(m.db.laureates.distinct(
    'prizes.category',
    {
        'prizes.share': '4'
    }
))

p.pprint(m.db.prizes.distinct(
    'category',
    {'laureates.share': '4'}
))

# Quais categorias de laureados possuem mais de um prêmio?
p.pprint(m.db.laureates.distinct(
    'prizes.category',
    {
        'prizes.1':{
            '$exists': True
        }
    }
))