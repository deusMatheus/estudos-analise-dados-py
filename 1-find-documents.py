from mongoClientPy import mongoClientPy as m
import pprint

'''
from pymongo import MongoClient
import pprint

# Estabelecendo conexão com MongoDB e DB
client = MongoClient() # Instancia o MongoDB através da variável client
db = client['nobel'] # Instancia o db Nobel

# Para acessar os documetnos da coleção
prizes = db['prizes']
laureates = db['laureates']
'''

# Filtrando e contando documentos por gênero
# Se não passar nenhum argumento dentro das chaves {}, será contado o número total de documentos dentro de laureates.
# Senso assim, o filtro funciona na forma de dicionário.
print(f"Número de laureados do gênero feminino: {m.db.laureates.count_documents({'gender':'female'})}")
print(f"Número de laureados do gênero masculino: {m.db.laureates.count_documents({'gender':'male'})}")

# Contar documentos pelo país de sua morte.

print(f"Número de laureados que morreram no Brasil: {m.db.laureates.count_documents({'diedCountry':'Brazil'})}")
print(f"Número de laureados que morreram na França: {m.db.laureates.count_documents({'diedCountry':'France'})}")

# Filtro composto com dados
filter_doc = {
    'diedCountry': 'France',
    'gender': 'female',
    'bornCity': 'Warsaw'
}
print(f"Laureados que morreram na França, do gênero Feminino nascidas em Varsóvia: {m.db.laureates.count_documents(filter_doc)}")

pprint.pprint(m.db.laureates.find_one(filter_doc))

# Utilizandon operador in
# Permite verificar diferentes valores para uma mesma consulta através de uma lista
filter_in = m.db.laureates.count_documents(
    {
        'diedCountry': {
            '$in': ['France', 'USA', 'Poland', 'Mexico']
        }
    }
)

print(filter_in)

# Utilizando operador ne - not equal
# De maneira semelhante ao in, mas não inclui os registros do valor passado. Neste caso, não consulta os mortos nos EUA. 
filter_ne = m.db.laureates.count_documents(
    {
        'diedCountry': {
            '$ne': ['USA']
        }
    }
)

print(filter_ne)