from mongoClientPy import mongoClientPy as m
import pprint as p

# 1 - valor incluído
# 0 - valor não incluído
docs = m.db.laureates.find( # docs é um cursor, o que indica que temos que iterar os dados para obter as informações
    filter = {}, # filtro vazio/sem argumentos indica todos os dados da projeção 
    projection = {
        'prizes.affiliations': 1, # quero incluir este valor na projeção
        '_id': 0 # não quero incluir este valor na projeção
    }
)

# p.pprint(docs) - não funciona por docs ser um cursor, é necessário iterar sobre cada um dos valores deste cursor 
#for doc in docs:
#    p.pprint(doc)

# De maneira semelhante, caso não queira iterar em cada um dos itens, pode-se transformar em lista:

p.pprint(list(docs))

#############################################3
# Projeção com campos ausentes
docs_2 = m.db.laureates.find(
    filter = {'gender':'org'},
    projection = ['bornCountry', 'firstname'] # Neste caso aqui não trás bornCountry porque esta informação é vazia no db!
)

for doc in docs_2:
    p.pprint(doc)

#####

docs_3 = m.db.laureates.find(
    filter = {'gender':'female'},
    projection = ['bornCountry', 'firstname'] 
)

for doc in docs_3:
    p.pprint(doc)