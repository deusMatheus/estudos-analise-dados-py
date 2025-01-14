from mongoClientPy import mongoClientPy as m

#from pymongo import MongoClient
import pprint

'''
# Estabelecendo conexão com MongoDB e DB
client = MongoClient() # Instancia o MongoDB através da variável client
db = client['nobel'] # Instancia o db Nobel

# Para acessar os documetnos da coleção
prizes = db['prizes']
laureates = db['laureates']
'''
# Buscando documento

walter = m.db.laureates.find_one({
    'firstname': 'Walter',
    'surname': 'Kohn'
})

pprint.pprint(walter)

# Pesquisando em subestrutura
uni_california = m.db.laureates.count_documents({
    'prizes.affiliations.name': 'University of California'
})
pprint.pprint(uni_california)

san_francisco = m.db.laureates.count_documents({
    'prizes.affiliations.city': 'San Francisco, CA'
})
pprint.pprint(san_francisco)

# Lista documento com informações pendentes através do exists: False
no_country = m.db.laureates.count_documents({
    'bornCountry':{
        '$exists': False
    }
})
pprint.pprint(no_country)

# Verificando quantos lauderados possuem e não possuem prêmios
quantity_prizes = m.db.laureates.count_documents({
    'prizes': {
        '$exists': True
    }
})

quantity_no_prizes = m.db.laureates.count_documents({
    'prizes': {
        '$exists': False
    }
})

pprint.pprint(f'{quantity_prizes} possuem prêmios e {quantity_no_prizes} não possuem prêmios.')

# Verificando quantos prizes estão preenchido
prize_contain = m.db.laureates.count_documents({
    'prizes.0':{
        '$exists': True
    }
})
pprint.pprint(prize_contain)

# Verificando laureados que possuem mais de um prêmio
prize_mult = m.db.laureates.count_documents({
    'prizes.1':{
        '$exists': True
    }
})
pprint.pprint(f'{prize_mult} laureados possuem mais de um prêmio.')