from pymongo import MongoClient

class mongoClientPy:
    
    # Estabelecendo conexão com MongoDB e DB
    client = MongoClient() # Instancia o MongoDB através da variável client
    db = client['nobel'] # Instancia o db Nobel

    # Para acessar os documetnos da coleção
    prizes = db['prizes']
    laureates = db['laureates']