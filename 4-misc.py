from mongoClientPy import mongoClientPy as m
import pprint as p

# Informação dos laureados em física que possuem prêmio  compartilhado 

# Essa consulta não funcinou! 
p.pprint(m.db.laureates.count_documents({
    'prizes':{
        'category': 'physics',
        'share': '1'
    }
}))

# Essa abaixo funciona por conta da chave elenMath, um elemento de combinação
p.pprint(m.db.laureates.count_documents({
    'prizes': {
        '$elemMatch': {
            'category': 'physics',
            'share': '1'
        }
    }
}))

# Laureados que possuem prêmio em física compartilhado antes de 1945
p.pprint(m.db.laureates.count_documents({
    'prizes': {
        '$elemMatch': {
            'category': 'physics',
            'share': '1',
            'year': {'$lt': '1945'} #less-than: lt, greater-than: gt
        }
    }
}))