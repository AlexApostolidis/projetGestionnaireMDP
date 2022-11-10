import json

def connection(username, connection_password):
    with open("connexionId.json") as file : 
        doc = json.load(file)
    return doc['user']['username'] == username and doc['user']['password'] == connection_password